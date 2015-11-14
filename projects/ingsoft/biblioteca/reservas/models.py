from django.db import models
from django.contrib.auth.models import User
from libros.models import Libro
from pazys.models import Estudiante

# Create your models here.

class Reserva(models.Model):	
	fecha_creacion = models.DateField(auto_now=True)
	libro = models.ForeignKey(Libro)
	estudiante = models.ForeignKey(Estudiante)
	active = models.BooleanField(default=True) 