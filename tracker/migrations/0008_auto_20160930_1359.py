# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-30 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20160930_1133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Camiones',
            new_name='Camion',
        ),
        migrations.AlterField(
            model_name='opeduquesa',
            name='ficha_camion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Camiones'),
        ),
    ]