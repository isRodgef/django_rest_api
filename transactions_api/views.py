from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from transactions_api.csv_wrapper import CsvWrapper

class TranactionsNew(APIView):

    def post(self, request):
        filename = request.FILES['csv_file'].temporary_file_path()
        csv_reader  = CsvWrapper()
        transaction_list = csv_reader.create_list(filename=filename)
        import code; code.interact(local=dict(globals(), **locals()))