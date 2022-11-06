from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import  transactions_api.views as api_views 

urlpatterns = [
    path('processFile/',view=api_views.TranactionsNew.as_view()),
   path('retrieveRows/',view=api_views.TranactionsFetch.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)