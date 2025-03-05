from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('doctorhunt_app.urls.user_urls')),
    path('doctors/', include('doctorhunt_app.urls.doctor_urls')),
    path('patients/', include('doctorhunt_app.urls.patient_urls')),
    path('medical-records/', include('doctorhunt_app.urls.medical_record_urls')),
    path('appointments/', include('doctorhunt_app.urls.appointment_urls')),
    path('diagnosis-offers/', include('doctorhunt_app.urls.diagnosis_offer_urls')),

    path('doctors-frontend/', include('doctorhunt_app.urls.doctor_frontend_urls')),

]
