# doctorhunt_app/urls/appointment_urls.py
from django.urls import path
from doctorhunt_app.views.appointment_views import AppointmentListCreateView, AppointmentDetailView

urlpatterns = [
    path('', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]
