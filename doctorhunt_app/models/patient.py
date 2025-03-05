from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_info = models.JSONField(default=dict)
    doctors = models.ManyToManyField("doctorhunt_app.Doctor", related_name="patients")
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
