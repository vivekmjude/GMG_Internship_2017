# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 11:29
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0014_auto_20170726_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='teethnum',
            field=multiselectfield.db.fields.MultiSelectField(default=1, max_length=86, verbose_name='Tooth No.'),
        ),
    ]