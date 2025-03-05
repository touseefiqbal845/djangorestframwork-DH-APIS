from rest_framework import serializers
from doctorhunt_app.models.diagnosis_offer import DiagnosisOffer

class DiagnosisOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisOffer
        fields = '__all__'
