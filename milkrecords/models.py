from django.db import models
from farmer.models import Farmer
from cooperative.models import Cooperative

class MilkRecord (models.Model):
    id = models.SmallIntegerField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    milk_delivery_date = models.DateField()
    quantity = models.SmallIntegerField()
    sale = models.SmallIntegerField()
    total = models.SmallIntegerField()
    def __str__(self):
        return f"Milk Record for {self.id}"
