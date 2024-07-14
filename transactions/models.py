from django.db import models
from farmer.models import Farmer
from cooperative.models import Cooperative


class Transaction(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.SmallIntegerField()
    description = models.TextField()
    total = models.SmallIntegerField()
    def __str__(self):
        return f"Transaction {self.id}"
