# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 21:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20160113_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
