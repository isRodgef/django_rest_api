from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TranactionsNew(APIView):

    def create(self, request):
        import code; code.interact(local=dict(globals(), **locals()))