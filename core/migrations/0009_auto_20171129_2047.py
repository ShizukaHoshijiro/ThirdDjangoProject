# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 17:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20171029_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
    ]
