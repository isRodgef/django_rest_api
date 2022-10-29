from django.urls import path
from transactions_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('processFile/',view=views.TranactionsNew.as_view()),
    path('retrieveRows/',view=views.TranactionsNew.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)