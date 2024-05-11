from django.db import models

class Calculator(models.Model):
    input_data = models.CharField(max_length=255)
    result = models.DecimalField(max_digits=10, decimal_places=2)

