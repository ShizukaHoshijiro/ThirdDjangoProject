# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update_dare',
            new_name='update_date',
        ),
    ]
