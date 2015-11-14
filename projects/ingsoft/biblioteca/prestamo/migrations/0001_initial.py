# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20151113_1100'),
        ('pazys', '0004_auto_20151109_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroPrestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEstudiante', models.CharField(max_length=200)),
                ('fechaInicioPrestamo', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaLimite', models.DateTimeField()),
                ('activo', models.BooleanField(default=True)),
                ('estudiante', models.ForeignKey(to='pazys.Estudiante')),
                ('libro', models.ForeignKey(to='libros.Libro')),
            ],
        ),
    ]
