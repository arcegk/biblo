from django.db import models
from django.utils import timezone
from pazys.models import Estudiante

class Libro(models.Model):
    codigoDewey = models.CharField(max_length=200)
    tituloLibro = models.CharField(max_length=200)
    volumenLibro = models.CharField(max_length=200)
    edicionLibro = models.CharField(max_length=200)

    def __unicode__(self):
        return self.codigoDewey

    published_date = models.DateTimeField(
        blank=True, null=True)

    

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class RegistroPrestamo(models.Model):
    libro = models.ForeignKey(Libro)
    estudiante = models.ForeignKey(Estudiante)
    nombreEstudiante = models.CharField(max_length=200)
    fechaInicioPrestamo = models.DateTimeField(default=timezone.now)
    fechaLimite = models.DateTimeField()

def __str__(self):
    return self.numeroRegistro    