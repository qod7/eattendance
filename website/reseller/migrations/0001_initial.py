# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reseller.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField(default=reseller.models.get_default_expiry_date)),
                ('organization_creation_limit', models.IntegerField(default=1)),
                ('contact', models.CharField(blank=True, default='', max_length=50, verbose_name='Contact Info')),
                ('remarks', models.TextField(blank=True, default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reseller',
                'verbose_name_plural': 'Resellers',
            },
        ),
    ]