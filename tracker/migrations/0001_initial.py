# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='opeDuquesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ficha_camion', models.CharField(max_length=15)),
                ('circunscripcion', models.CharField(max_length=2)),
                ('ton', models.IntegerField()),
            ],
        ),
    ]
