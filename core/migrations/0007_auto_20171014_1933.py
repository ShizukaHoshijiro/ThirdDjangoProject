# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171013_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='model_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
    ]
