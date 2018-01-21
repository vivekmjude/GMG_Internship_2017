# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0013_auto_20170725_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Order Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='remarks',
            field=models.CharField(default='No remarks', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Saved', 'Saved'), ('Placed', 'Placed'), ('Received at Lab', 'Received at Lab'), ('Accepted by Lab', 'Accepted by Lab'), ('Rejected by Lab', 'Rejected by Lab'), ('Order Held', 'Order Held'), ('Processing', 'Processing'), ('Shipped from Lab', 'Shipped from Lab'), ('Arriving Today', 'Arriving Today'), ('Received by Provider', 'Received by Provider'), ('Completed', 'Completed')], default='saved', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='teethnum',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32)], default=1, max_length=86, verbose_name='Tooth No.'),
        ),
    ]
