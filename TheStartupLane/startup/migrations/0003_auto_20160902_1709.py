# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='source',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
