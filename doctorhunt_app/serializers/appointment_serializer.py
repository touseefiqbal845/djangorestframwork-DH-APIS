from rest_framework import serializers
from doctorhunt_app.models.appointment import Appointment
from doctorhunt_app.serializers.doctor_serializer import DoctorSerializer
from doctorhunt_app.serializers.patient_serializer import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)  
    patient = PatientSerializer(read_only=True)  

    class Meta:
        model = Appointment
        fields = '__all__'
