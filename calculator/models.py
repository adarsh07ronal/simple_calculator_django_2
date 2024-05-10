from django.db import models

# Create your models here.

class Calculator(models.Model):
    input = models.CharField(max_length=255)
    result = models.DecimalField(max_digits=10, decimal_places=2)

