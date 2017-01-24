# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms
import phoenix.custom_storages
import pyotp
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('secret_key', models.CharField(default=pyotp.random_base32, max_length=16)),
                ('image', django_resized.forms.ResizedImageField(storage=phoenix.custom_storages.SecureStorage(), upload_to='BadgePictures')),
            ],
            options={
                'permissions': (('view_badge_secret', 'Can view badge secret'),),
            },
        ),
        migrations.CreateModel(
            name='CrawledBadge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('achieved_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crawled', to='boothcrawl.Badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crawledbadges', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
