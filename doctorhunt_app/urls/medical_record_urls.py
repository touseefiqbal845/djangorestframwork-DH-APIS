# doctorhunt_app/urls/medical_record_urls.py
from django.urls import path
from doctorhunt_app.views.medical_record_views import MedicalRecordListCreateView, MedicalRecordDetailView

urlpatterns = [
    path('', MedicalRecordListCreateView.as_view(), name='medical-record-list'),
    path('<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
]
