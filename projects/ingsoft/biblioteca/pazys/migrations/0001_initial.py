# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=7)),
                ('numero_documento', models.CharField(max_length=10)),
                ('nivel', models.CharField(max_length=25, choices=[(b'posgrado', b'Posgrado'), (b'pregrado', b'Pregrado')])),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_facultad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pazy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField()),
                ('consecutivo', models.CharField(max_length=25)),
                ('estudiante', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_programa', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='Facultad',
            field=models.ForeignKey(to='pazys.Facultad'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='User',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(to='pazys.Programa'),
        ),
    ]
