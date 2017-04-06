# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-06 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0009_auto_20161105_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='funding_round',
        ),
        migrations.AddField(
            model_name='funding',
            name='amount_round',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funding',
            name='investor',
            field=models.CharField(max_length=1000),
        ),
    ]
