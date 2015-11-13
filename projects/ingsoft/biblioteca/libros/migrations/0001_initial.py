# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Libro',
			fields=[ 
				('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
				('titulo',models.CharField(max_length=200, null=False)),
				('autor', models.TextField(max_length=200)),
				('codigoasignado', models.CharField(max_length =200 ,null=False)),
				('temaprincipal', models.CharField(max_length = 200)),
				('temasecundario', models.CharField(max_length = 200)),
				('editorial', models.CharField(max_length = 200, null = False)),
				('fechapublicacion', models.CharField(max_length = 200, null = False)),
				('dimensiones', models.CharField(max_length=200, null=False)),
				('estadofisico', models.CharField(max_length=200, null=False)),
				('estadodebaja' , models.CharField(max_length=200, null=False)),
				('numeropaginas', models.IntegerField(null=False)),
				('fechacompra', models.CharField(max_length=200, null=False)),
				('cantidad', models.IntegerField(null=False)),
				('preciocompra', models.IntegerField(null=False)),
				('disponibilidad',models.CharField(max_length=200, null=False)),
				('lugarpublicacion', models.CharField(max_length=200, null=False)),
				('Volumen', models.IntegerField(max_length=200, null=False)),
				('palabrasclave', models.CharField(max_length=200, null=False)),
				('descripcionfisica' , models.TextField(max_length=200, null=False)),
				('numeroingreso' , models.IntegerField(null=False)),
				('estadomantenimiento', models.CharField(max_length=200, null=False)),
				('TipodeColeccion' , models.CharField(max_length=200, null=False)),
				('ISBN', models.CharField(max_length=200,null= False)),
				('Edicion' , models.CharField(max_length = 200, null = False)),
			],
		),
	]
