# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20151113_1100'),
        ('pazys', '0004_auto_20151109_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_total', models.CharField(max_length=100)),
                ('causa', models.CharField(max_length=200)),
                ('dias_retraso', models.CharField(max_length=100)),
                ('estudiante', models.ForeignKey(to='pazys.Estudiante')),
                ('libro', models.ForeignKey(to='libros.Libro')),
            ],
        ),
    ]
