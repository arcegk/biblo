from django.db import models
from django.utils import timezone
from pazys.models import Estudiante
from libros.models import Libro

class RegistroPrestamo(models.Model):
    libro = models.ForeignKey(Libro)
    estudiante = models.ForeignKey(Estudiante)
    nombreEstudiante = models.CharField(max_length=200)
    fechaInicioPrestamo = models.DateTimeField(default=timezone.now)
    fechaLimite = models.DateTimeField()

def __str__(self):
    return self.numeroRegistro    