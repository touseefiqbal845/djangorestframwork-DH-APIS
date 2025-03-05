from django.urls import path
from rest_framework.routers import DefaultRouter
from doctorhunt_app.views.doctor_views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = router.urls
