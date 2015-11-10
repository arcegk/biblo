# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pazys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pazy',
            name='encargado',
            field=models.ForeignKey(default=None, editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pazy',
            name='estudiante',
            field=models.ForeignKey(to='pazys.Estudiante'),
        ),
    ]
