# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160112_1210'),
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
