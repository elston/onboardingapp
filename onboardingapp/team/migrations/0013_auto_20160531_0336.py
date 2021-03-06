# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_auto_20160531_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='team_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='org_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='team_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
