# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_remove_bookingoffer_offering_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingoffer',
            name='offering_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.TimeSlot'),
        ),
    ]
