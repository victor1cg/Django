from django.db import models
from datetime import datetime

# Create your models here.
class Semanal(models.Model):
    data = models.DateField()
    cliente = models.CharField(max_length = 100)
    modelo = models.CharField(max_length = 100)
    projecao_m0 = models.FloatField(null = True)
    real = models.FloatField(null = True)
    estoque = models.FloatField(null = True)
