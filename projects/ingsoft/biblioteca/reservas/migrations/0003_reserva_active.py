# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_auto_20151114_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
