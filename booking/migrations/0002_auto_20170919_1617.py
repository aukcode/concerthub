# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consert',
            new_name='Concert',
        ),
    ]