from rest_framework import serializers
from django.apps import apps
from doctorhunt_app.models.medical_record import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = MedicalRecord
        fields = '__all__'

    def get_patient(self, obj):
        Patient = apps.get_model('doctorhunt_app', 'Patient')  
        PatientSerializer = type(
            'DynamicPatientSerializer',
            (serializers.ModelSerializer,),
            {'Meta': type('Meta', (), {'model': Patient, 'fields': '__all__'})}
        )  
        return PatientSerializer(obj.patient).data if obj.patient else None
