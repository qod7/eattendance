# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-04 01:25
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reseller', '0005_auto_20160119_1218'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('method', models.IntegerField(choices=[(1, 'fingerprint'), (2, 'rfid'), (3, 'password'), (4, 'manual')], default=1)),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Calendar',
                'verbose_name_plural': 'Calendars',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('holiday', models.BooleanField(default=False)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Calendar')),
            ],
            options={
                'verbose_name': 'Day',
                'verbose_name_plural': 'Days',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Day')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('message', models.CharField(max_length=400, verbose_name='Message')),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('contact', models.CharField(max_length=50, verbose_name="Admin's Contact Number")),
                ('reseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reseller.Reseller')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organization',
                'ordering': ('-user__date_joined',),
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the Shift')),
                ('on_duty_time', models.TimeField()),
                ('off_duty_time', models.TimeField()),
                ('late_time', models.TimeField()),
                ('leave_early_time', models.TimeField()),
                ('beginning_in', models.TimeField()),
                ('ending_in', models.TimeField()),
                ('beginning_out', models.TimeField()),
                ('ending_out', models.TimeField()),
                ('check_in', models.TimeField()),
                ('check_out', models.TimeField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shifts', to='organization.Organization')),
            ],
            options={
                'verbose_name': 'Shift',
                'verbose_name_plural': 'Shifts',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField()),
                ('preferences', django.contrib.postgres.fields.jsonb.JSONField()),
                ('photo', models.ImageField(upload_to='')),
                ('contact', models.CharField(blank=True, default='', max_length=50, verbose_name='Contact Info')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='organization.Organization')),
                ('shifts', models.ManyToManyField(related_name='staff', to='organization.Shift')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='organization.Organization'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='calendar',
            name='organization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='calendar', to='organization.Organization'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='organization.Staff'),
        ),
    ]
