from django.urls import path, include
from .views import calculate

urlpatterns = [
    path('calculate/', calculate, name='calculate'),
]