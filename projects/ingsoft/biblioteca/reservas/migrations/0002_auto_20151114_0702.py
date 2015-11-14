# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20151113_1100'),
        ('pazys', '0004_auto_20151109_1741'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='estudiante',
            field=models.ForeignKey(default=None, to='pazys.Estudiante'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='libro',
            field=models.ForeignKey(default=None, to='libros.Libro'),
            preserve_default=False,
        ),
    ]
