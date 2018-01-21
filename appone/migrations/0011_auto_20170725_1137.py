# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0010_auto_20170725_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='remarks',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Saved', 'Saved'), ('Placed', 'Placed'), ('Received at Lab', 'Received at Lab'), ('Accepted by Lab', 'Accepted by Lab'), ('Order Held', 'Order Held'), ('Processing', 'Processing'), ('Shipped from Lab', 'Shipped from Lab'), ('Received by Provider', 'Received by Provider'), ('Completed', 'Completed')], default='saved', max_length=50),
        ),
    ]