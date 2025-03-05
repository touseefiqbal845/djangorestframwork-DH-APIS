from django.db import models
from .doctor import Doctor
from .patient import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    time = models.TimeField()
    date = models.DateField()
    location = models.JSONField(default=dict)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("completed", "Completed"), ("cancelled", "Cancelled")],
        default="pending"
    )

    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"
