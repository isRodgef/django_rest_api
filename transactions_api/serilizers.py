
from rest_framework import serializers
from transactions_api.models import TransactionModel

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ['date', 'country', 'transact_type','currency','net','vat']