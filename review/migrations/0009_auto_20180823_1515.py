# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_demandletter_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandletter',
            name='phone_number',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
