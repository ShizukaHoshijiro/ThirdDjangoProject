# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171017_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('-pub_date', 'title')},
        ),
    ]
