# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo', '0001_initial'),
        ('multas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='prestamof',
            field=models.ForeignKey(to='prestamo.RegistroPrestamo'),
        ),
    ]
