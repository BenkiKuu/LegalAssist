# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20180823_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandletter',
            name='dob',
        ),
    ]
