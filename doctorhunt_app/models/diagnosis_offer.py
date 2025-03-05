from django.db import models

class DiagnosisOffer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    tests_offer = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    services = models.JSONField(default=list)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
