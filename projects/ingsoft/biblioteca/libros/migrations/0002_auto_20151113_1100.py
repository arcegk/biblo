# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Edicion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Volumen',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcionfisica',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='libro',
            name='palabrasclave',
            field=models.CharField(max_length=500),
        ),
    ]
