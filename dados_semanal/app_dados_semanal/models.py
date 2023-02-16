from django.db import models
from django.utils import timezone

# Create your models here.
class Semanal(models.Model):
    data = models.DateField(null= False)
    cliente = models.CharField(max_length = 100, null= False)
    modelo = models.CharField(max_length = 100, null = False)
    projecao_m0 = models.FloatField(null = True, default=0)
    real = models.FloatField(null = True, default=0)
    estoque = models.FloatField(null = True, default=0)
    uploaded = models.DateTimeField(default=timezone.now)

    
