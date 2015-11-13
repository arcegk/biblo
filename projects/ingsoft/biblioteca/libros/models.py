from django.db import models

# Create your models here.
class Libro(models.Model):
	titulo = models.CharField(max_length=200, null=False)
	autor = models.TextField(max_length=200)
	codigoasignado = models.CharField(null=False, max_length=200)
	temaprincipal = models.CharField(null=False,	max_length=200)
	#nombre = models.CharField(max_length=30, verbose_name=u"first name", error_messages={'required':'A contact needs a first name.'}
	temasecundario = models.CharField(max_length=200, null=False)
	editorial = models.CharField(max_length=200, null=False)
	fechapublicacion = models.CharField(max_length=200, null=False)
	dimensiones= models.CharField(max_length=200, null=False)
	estadofisico= models.CharField(max_length=200, null=False)
	estadodebaja = models.CharField(max_length=200, null=False)
	numeropaginas = models.IntegerField(null=False)
	fechacompra = models.CharField(max_length=200, null=False)
	cantidad = models.IntegerField(null=False)
	preciocompra = models.IntegerField(null=False)
	disponibilidad = models.CharField(max_length=200, null=False)
	lugarpublicacion = models.CharField(max_length=200, null=False)
	Volumen = models.IntegerField(null=False)
	palabrasclave = models.CharField(max_length=500,null=False)
	descripcionfisica = models.CharField(max_length=200, null=False)
	numeroingreso=models.IntegerField(null=False)
	estadomantenimiento = models.CharField(max_length=200, null=False)
	TipodeColeccion = models.CharField(max_length=200,null = False)
	ISBN = models.CharField(max_length = 200, null = False)
	Edicion = models.TextField(max_length = 200, null = False)
