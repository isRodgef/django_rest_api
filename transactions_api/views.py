from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from transactions_api.csv_wrapper import CsvWrapper
from transactions_api.models import TransactionModel


class TranactionsNew(APIView):

    def post(self, request):
        #InMemoryUploadedFile for small and medium
        #<class 'django.core.files.uploadedfile.TemporaryUploadedFile'> for large file
        filename = request.FILES['csv_file'].temporary_file_path()
        csv_reader  = CsvWrapper()
        transaction_list = csv_reader.create_list(filename=filename)
    
    def get(self, request):
        country_code = self.request.query_params.get('country_code')
        date = self.request.query_params.get('date')
        data = TransactionModel.objects.all()
        import code; code.interact(local=dict(), **locals())
        return data


