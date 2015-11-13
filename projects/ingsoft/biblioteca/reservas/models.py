from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reserva(models.Model):
	usuario = models.CharField(max_length=20)
	fecha_creacion = models.DateField(auto_now=True)