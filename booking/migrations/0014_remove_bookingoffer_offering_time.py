# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20171003_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingoffer',
            name='offering_time',
        ),
    ]
