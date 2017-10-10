# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0063_auto_20171010_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingoffer',
            options={'ordering': ('time_slot', 'time_slot__stage')},
        ),
        migrations.RenameField(
            model_name='bookingoffer',
            old_name='offering_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='bookingoffer',
            old_name='offering_time_slot',
            new_name='time_slot',
        ),
    ]
