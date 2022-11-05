from pyexpat import model
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from django.core import serializers
from django.core.exceptions import ValidationError
# Create your models here.

import datetime

def validate_year(value):
    if value.year != 2020:
        raise ValidationError(
            ('%(value)s does occur in the year 2020'),
            params={'value': value},
        )

def validate_transact_type(value):
     if value.lower() not in ('sale', 'purchase'):
        raise ValidationError(
            ('%(value)s is not of type sale or purchase'),
            params={'value': value},
        )

class TransactionModel(models.Model):
    date = models.DateField(validators = [validate_year])
    country = models.CharField(max_length=100)
    transact_type = models.CharField(max_length=8,validators=[validate_transact_type])
    currency = models.CharField(max_length=10)
    net = models.FloatField()
    vat = models.FloatField()
