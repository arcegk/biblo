# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0002_remove_registroprestamo_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroprestamo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
