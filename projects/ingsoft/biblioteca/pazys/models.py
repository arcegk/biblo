from django.db import models
from django.contrib.auth.models import User
from . import constants

# Create your models here.

class Programa(models.Model):
	nombre_programa = models.CharField(max_length=100)
	codigo = models.CharField(max_length=6)

class Facultad(models.Model):
	nombre_facultad = models.CharField(max_length=50)


class Estudiante(models.Model):
	User = models.ForeignKey(User)
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=7)
	numero_documento = models.CharField(max_length=10)
	programa = models.ForeignKey(Programa)
	Facultad = models.ForeignKey(Facultad)
	nivel = models.CharField(max_length=25,  choices= constants.nivel)


class PazySalvo(models.Model):

	fecha_creacion = models.DateField(auto_now=True)
	estudiante = models.ForeignKey(Estudiante)
	encargado = models.ForeignKey(User, editable=False)
	

