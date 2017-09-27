# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, max_length=256, null=True)),
                ('genre', models.CharField(max_length=120)),
                ('tech_needs', models.TextField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('revenue', models.FloatField(blank=True, null=True)),
                ('sold_tickets', models.IntegerField(blank=True, null=True)),
                ('audience_showed_up', models.IntegerField(blank=True, null=True)),
                ('concert_start_time', models.DateTimeField(blank=True, null=True)),
                ('concert_end_time', models.DateTimeField(blank=True, null=True)),
                ('tech_meetup_time', models.DateTimeField(blank=True, null=True)),
                ('tech_done_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('tickets', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, max_length=120, null=True)),
                ('audience_cap', models.IntegerField(blank=True, null=True)),
                ('festival_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Festival')),
            ],
        ),
        migrations.AddField(
            model_name='concert',
            name='festival_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Festival'),
        ),
        migrations.AddField(
            model_name='concert',
            name='stage_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Stage'),
        ),
        migrations.AddField(
            model_name='concert',
            name='technicians',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artist',
            name='concert_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Concert'),
        ),
        migrations.AddField(
            model_name='artist',
            name='festival_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Festival'),
        ),
    ]
