from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from doctorhunt_app.serializers.user_serializer import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            "token": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth = None
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class ResetPasswordRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        user = User.objects.filter(email=email).first()

        if user:
            user.generate_reset_token()
            reset_link = f"http://localhost:3000/reset-password?token={user.reset_password_token}&email={email}"
            # Send email function (to be implemented)
            return Response({"message": "Password reset link sent"}, status=status.HTTP_200_OK)

        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        token = request.data.get("token")
        password = request.data.get("password")

        user = User.objects.filter(email=email, reset_password_token=token).first()
        if user:
            user.set_password(password)
            user.reset_password_token = None
            user.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid token or email"}, status=status.HTTP_400_BAD_REQUEST)
