from django.db import models
from doctorhunt_app.models.patient import Patient 

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    prescription = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Medical Record of {self.patient.first_name} {self.patient.last_name} - {self.date}"
