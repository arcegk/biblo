# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazys', '0003_auto_20151108_0428'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pazy',
            new_name='PazySalvo',
        ),
    ]
