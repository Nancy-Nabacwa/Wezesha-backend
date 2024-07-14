from django.db import models
from farmer.models import Farmer
from cooperative.models import Cooperative

class Sacco(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
