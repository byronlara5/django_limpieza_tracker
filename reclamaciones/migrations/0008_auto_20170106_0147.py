# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-06 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamaciones', '0007_auto_20170106_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='sectores',
        ),
        migrations.AlterField(
            model_name='reclamacion',
            name='fecha_cierre',
            field=models.DateField(blank=True),
        ),
        migrations.DeleteModel(
            name='Supervisor',
        ),
    ]
