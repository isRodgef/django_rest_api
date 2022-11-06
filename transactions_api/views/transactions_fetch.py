from collections import defaultdict
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from transactions_api.wrappers.csv_wrapper import CsvWrapper
from transactions_api.models import TransactionModel
from transactions_api.serializers import TransactionSerializer
from rest_framework import generics
from django.forms.models import model_to_dict

class TranactionsFetch(APIView):
    #queryset =  TransactionModel.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request):
        # endpoint for country collection
        country_code = self.request.query_params.get('country')
        date = self.request.query_params.get('date')
        data = TransactionModel.objects.filter(date=date,country=country_code)
        return_result = list(map(lambda x : model_to_dict(x),data))
        return Response(return_result)
