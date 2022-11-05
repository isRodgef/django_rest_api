
from dataclasses import dataclass
from threading import local
from rest_framework import serializers
from transactions_api import currency_repository
from transactions_api.models import TransactionModel

from transactions_api.country_repository  import CountryWrapper
from transactions_api.currency_repository import CurrencyWrapper

class TransactionSerializer(serializers.ModelSerializer):
    country_transformer = CountryWrapper()
    currency_transformer = CurrencyWrapper()

    class Meta:
        model = TransactionModel
        fields = ['date', 'country', 'transact_type','currency','net','vat']
    

    def save(self, validated_data):
        transformed_data = validated_data
        iso_code = self.country_transformer.fetch_info(transformed_data['country'])
        self.currency_transformer.get_rate(transformed_data['currency'])
        converted_net = self.currency_transformer.convert(float(transformed_data['net']))
        transformed_data['net'] = converted_net
        transformed_data['country'] = iso_code
        return TransactionModel(**transformed_data)
    #def save(self):
    #    import code; code.interact(local=dict(globals(), **locals()))