# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_remove_staff_preferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='calendar', to='organization.Organization')),
            ],
            options={
                'verbose_name_plural': 'Calendars',
                'verbose_name': 'Calendar',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='organization.Calendar')),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
        ),
    ]
