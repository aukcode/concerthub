# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 12:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20170928_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingoffer',
            name='artist_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
