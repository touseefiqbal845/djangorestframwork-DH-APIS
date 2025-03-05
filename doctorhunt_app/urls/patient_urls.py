# doctorhunt_app/urls/patient_urls.py
from django.urls import path
from doctorhunt_app.views.patient_views import PatientListCreateView, PatientDetailView

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patient-list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]
