from rest_framework import serializers
from doctorhunt_app.models.doctor import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
