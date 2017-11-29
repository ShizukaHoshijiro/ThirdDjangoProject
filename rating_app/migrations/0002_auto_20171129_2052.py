# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]