from django.urls import path
from doctorhunt_app.views.user_view import RegisterView, LoginView, LogoutView, ResetPasswordRequestView, ResetPasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset-password-request/", ResetPasswordRequestView.as_view(), name="reset-password-request"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]
