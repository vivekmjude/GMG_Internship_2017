# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import appone.models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0017_auto_20170731_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='casenum',
            field=models.IntegerField(default=appone.models.casenum_generate, verbose_name='Case No.', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(default=appone.models.location_generate, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='provider',
            field=models.CharField(default=appone.models.provider_generate, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(verbose_name='Cost (in $)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(max_length=500, serialize=False, verbose_name='Product Name', primary_key=True),
        ),
    ]
