from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from doctorhunt_app.models.doctor import Doctor
from doctorhunt_app.models.appointment import Appointment
from doctorhunt_app.models.patient import Patient
from doctorhunt_app.serializers.doctor_serializer import DoctorSerializer
from doctorhunt_app.utils.search_features import SearchFeatures


class DoctorViewSet(viewsets.ViewSet):
    def list(self, request):
        """Get all doctors with search, filter, and pagination."""
        doctors = Doctor.objects.all()
        search_feature = SearchFeatures(doctors, request.GET)
        doctors = search_feature.search().filter().pagination(result_per_page=10).get_queryset()

        serializer = DoctorSerializer(doctors, many=True)
        return Response({
            "success": True,
            "message": "Doctors retrieved successfully",
            "doctors": serializer.data,
            "doctorsCount": Doctor.objects.count(),
            "resultPerPage": 10,
            "filteredDoctorsCount": doctors.count(),
        }, status=status.HTTP_200_OK)
 
    def create(self, request):
        """Create a new doctor."""
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Doctor created successfully", "doctor": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Get doctor by ID."""
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response({"success": True, "message": "Doctor retrieved successfully", "doctor": serializer.data},
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Update doctor by ID."""
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Doctor updated successfully", "doctor": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete doctor by ID."""
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response({"success": True, "message": "Doctor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        """Get doctors sorted by popularity (appointments count, rating, reviews, favorite)."""
        doctors = Doctor.objects.annotate(
            activeAppointmentsCount=Count('appointments', filter=Q(appointments__status__in=['confirmed', 'completed']))
        ).order_by('-rating', '-reviews', '-activeAppointmentsCount', '-is_favourite')[:5]

        serializer = DoctorSerializer(doctors, many=True)
        return Response({
            "success": True,
            "message": "Top 5 doctors fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured doctors."""
        doctors = Doctor.objects.filter(is_featured=True)
        serializer = DoctorSerializer(doctors, many=True)
        return Response({
            "success": True,
            "message": "Featured doctors fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def by_career(self, request):
        """Get doctors by career specialization."""
        career = request.GET.get('career')
        if not career:
            return Response({"error": "Career field is required"}, status=status.HTTP_400_BAD_REQUEST)

        doctors = Doctor.objects.filter(career__iexact=career)
        serializer = DoctorSerializer(doctors, many=True)

        return Response({
            "success": True,
            "message": "Doctors retrieved successfully",
            "doctors": serializer.data
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def favorites(self, request):
        """Get favorite doctors."""
        doctors = Doctor.objects.filter(is_favourite=True)
        serializer = DoctorSerializer(doctors, many=True)

        return Response({
            "success": True,
            "message": "Favorite doctors retrieved successfully",
            "doctors": serializer.data
        }, status=status.HTTP_200_OK)
  