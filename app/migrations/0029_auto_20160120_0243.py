# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20160120_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='unidadeMedida',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidadeMedida',
            field=models.ManyToManyField(to='app.UnidadeMedida'),
        ),
    ]
