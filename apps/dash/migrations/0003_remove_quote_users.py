# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20161229_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='users',
        ),
    ]