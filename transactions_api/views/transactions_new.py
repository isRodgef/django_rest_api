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
        TransactionModel.objects.bulk_create(transaction_results['Successful'])
        to_be_converted = transaction_results['Successful']
        successes = list(map(lambda x : model_to_dict(x),to_be_converted))
        transaction_results['Successful'] = successes
        return Response(transaction_results)
