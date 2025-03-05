from rest_framework import generics
from doctorhunt_app.models.diagnosis_offer import DiagnosisOffer
from doctorhunt_app.serializers.diagnosis_offer_serializer import DiagnosisOfferSerializer

class DiagnosisOfferListCreateView(generics.ListCreateAPIView):
    queryset = DiagnosisOffer.objects.all()
    serializer_class = DiagnosisOfferSerializer

class DiagnosisOfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiagnosisOffer.objects.all()
    serializer_class = DiagnosisOfferSerializer
