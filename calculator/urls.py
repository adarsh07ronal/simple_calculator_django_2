from django.urls import path, include
from .views import calculate,calculate_and_store, display_results

urlpatterns = [
    path('calculate/', calculate, name='calculate'),
    path('calculate2/', calculate_and_store, name='calculate_and_store'),
    path('results/', display_results, name='display_results'),    
]