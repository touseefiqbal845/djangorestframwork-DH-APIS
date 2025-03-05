from django.urls import path
from doctorhunt_app.views.diagnosis_offer_views import DiagnosisOfferListCreateView, DiagnosisOfferDetailView

urlpatterns = [
    path('', DiagnosisOfferListCreateView.as_view(), name='diagnosis-offer-list'),
    path('<int:pk>/', DiagnosisOfferDetailView.as_view(), name='diagnosis-offer-detail'),
]
