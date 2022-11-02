from collections import defaultdict
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from transactions_api import country_repository, serializers
from transactions_api.csv_wrapper import CsvWrapper
from transactions_api.models import TransactionModel
from transactions_api.serializers import TransactionSerializer
from rest_framework import generics


class TranactionsNew(APIView):
    #queryset =  TransactionModel.objects.all()
    serializer_class = TransactionSerializer



    def post(self, request):

        #InMemoryUploadedFile for small and medium
        #<class 'django.core.files.uploadedfile.TemporaryUploadedFile'> for large file
        filename = request.FILES['csv_file'].temporary_file_path()
        _serializer = self.serializer_class
        csv_reader  = CsvWrapper(_serializer)
        transaction_results = csv_reader.create_list(filename=filename)
        
        return Response(transaction_results)
    
    def get(self, request):
        # endpoint for country collection
        country_code = self.request.query_params.get('country_code')
        date = self.request.query_params.get('date')
        data = TransactionModel.objects.all()
        data = data.filter(date=date)
        data = data.filter(date=country_code)
        return data
