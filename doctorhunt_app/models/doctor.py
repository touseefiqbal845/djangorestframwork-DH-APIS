from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    stories = models.JSONField(default=dict)
    rating = models.FloatField(default=0)
    is_favourite = models.BooleanField(default=False)
    reviews = models.IntegerField(default=0)
    hour_rate = models.DecimalField(max_digits=10, decimal_places=2)
    time_slot = models.JSONField(default=dict)
    details = models.JSONField(default=dict)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
