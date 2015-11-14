from django.db import models
from django.contrib.auth.models import User
from pazys.models import Estudiante
from libros.models import Libro
from prestamo.models import RegistroPrestamo

class Multa(models.Model):
    valor_total = models.CharField(max_length=100)
    causa = models.CharField(max_length = 200)
    dias_retraso = models.CharField(max_length=100)   
    estudiante = models.ForeignKey(Estudiante)
    libro = models.ForeignKey(Libro)

class Devolucion(models.Model):
	estado = models.CharField(max_length=15)
	fecha = models.DateTimeField()
	prestamof = models.ForeignKey(RegistroPrestamo)


