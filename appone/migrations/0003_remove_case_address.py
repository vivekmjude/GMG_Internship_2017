# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_case_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='address',
        ),
    ]
