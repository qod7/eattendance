# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_reseller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='reseller',
        ),
    ]
