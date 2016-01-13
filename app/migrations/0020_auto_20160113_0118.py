# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20160113_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientequantidade',
            name='ingrediente',
        ),
        migrations.RemoveField(
            model_name='ingredientequantidade',
            name='receita',
        ),
        migrations.RemoveField(
            model_name='ingredientequantidade',
            name='unidadeMedida',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='quantidade',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Receita'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidadeMedida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.UnidadeMedida'),
        ),
        migrations.DeleteModel(
            name='IngredienteQuantidade',
        ),
    ]
