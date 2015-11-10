# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazys', '0002_auto_20151108_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pazy',
            name='consecutivo',
        ),
        migrations.AlterField(
            model_name='pazy',
            name='fecha_creacion',
            field=models.DateField(auto_now=True),
        ),
    ]
