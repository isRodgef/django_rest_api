from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class TransactionModel(models.Model):
    date = models.DateField()
    country = models.CharField(max_length=100)
    transact_type = models.CharField(max_length=8)
    currency = models.CharField(max_length=10)
    net = models.FloatField()
    vat = models.FloatField() 