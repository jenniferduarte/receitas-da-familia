# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160112_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='quantidade',
        ),
    ]
