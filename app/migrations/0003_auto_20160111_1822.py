# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160111_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='tempoPreparo',
            field=models.TimeField(),
        ),
    ]
