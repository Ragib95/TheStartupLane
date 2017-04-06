# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_auto_20160902_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='startupname',
            name='industry',
        ),
        migrations.AddField(
            model_name='category',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.StartupName'),
        ),
    ]
