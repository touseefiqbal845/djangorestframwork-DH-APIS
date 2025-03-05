from rest_framework import serializers
from doctorhunt_app.models.patient import Patient
from doctorhunt_app.serializers.medical_record_serializer import MedicalRecordSerializer
from doctorhunt_app.serializers.doctor_serializer import DoctorSerializer  

class PatientSerializer(serializers.ModelSerializer):
    medical_records = MedicalRecordSerializer(many=True, read_only=True)  
    doctors = DoctorSerializer(many=True, read_only=True)   

    class Meta:
        model = Patient
        fields = '__all__'
