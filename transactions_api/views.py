from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from transactions_api import serializers
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
       
        #import code; code.interact(local=dict(globals(), **locals()))

        #serializers = TransactionSerializer(transaction_list)

        return Response(transaction_results)
        #import code; code.interact(local=dict(globals(), **locals()))
    
    def get(self, request):
        serializer_class = TransactionSerializer

        # endpoint for country collection
        #http://api.worldbank.org/v2/country?format=json
        #country_code = self.request.query_params.get('country_code')
        #date = self.request.query_params.get('date')
        data = TransactionModel.objects.all()
        #data = data.filter(country=country_name)
        #import code; code.interact(local=dict(), **locals())
        ret = [] 
        
        

        return Response(data=ret)

