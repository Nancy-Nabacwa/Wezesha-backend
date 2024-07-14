from django.db import models
from cooperative.models import Cooperative

class Farmer(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    loan_status = models.CharField(max_length=255)
    image = models.ImageField()
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"