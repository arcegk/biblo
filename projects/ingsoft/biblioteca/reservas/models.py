from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reserva(models.Model):
	fecha_creacion = models.DateField(auto_now=True)
	User = models.ForeignKey(User)
	#libro = models.ForeignKey(Programa)