# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 20:53
from __future__ import unicode_literals

import booking.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0039_auto_20171008_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, validators=[booking.validators.validate_artist_manager]),
        ),
    ]