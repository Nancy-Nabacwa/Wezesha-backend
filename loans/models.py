from django.db import models
from farmer.models import Farmer


class Loan(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    sacco_name = models.CharField(max_length=255)
    loan_amount = models.SmallIntegerField()
    loan_start_date = models.DateField()
    interest_rate = models.SmallIntegerField()
    duration = models.SmallIntegerField()
    loan_status = models.CharField(max_length=255)
    repayment_amount = models.SmallIntegerField()
    repayment_date = models.DateField()
    repayment_status = models.CharField(max_length=255)
    def __str__(self):
        return f"Loan {self.id}"
