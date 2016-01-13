# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160111_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.ManyToManyField(to='app.Ingrediente'),
        ),
    ]