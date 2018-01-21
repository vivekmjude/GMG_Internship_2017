# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import appone.models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0016_auto_20170726_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productname', models.CharField(max_length=500, serialize=False, primary_key=True)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='casenum',
            field=models.IntegerField(default=appone.models.casenum_generate, verbose_name='Case No.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(max_length=50, choices=[('PFM High Noble', 'PFM High Noble'), ('PFM Non Precious', 'PFM Non Precious'), ('Full Gold Crown', 'Full Gold Crown'), ('Full Cast Semi Precious', 'Full Cast Semi Precious'), ('Full Cast Non Precious', 'Full Cast Non Precious'), ('Crown Fit to Partial', 'Crown Fit to Partial'), ('Metal Occlusal', 'Metal Occlusal'), ('Metal Lingual', 'Metal Lingual'), ('Zirlux Temporary', 'Zirlux Temporary'), ('Cast Coping', 'Cast Coping'), ('PFM High Noble', 'PFM High Noble'), ('PFM Semi Precious', 'PFM Semi Precious'), ('PFM Bridges(Non Precious Alloy)', 'PFM Bridges(Non Precious Alloy)'), ('Emax Bridge', 'Emax Bridge'), ('Bruxzir Crown', 'Bruxzir Crown'), ('Zirconia Crown', 'Zirconia Crown'), ('Lava Crown', 'Lava Crown'), ('Emax Crown', 'Emax Crown'), ('Empress Crown', 'Empress Crown'), ('Zirconia Veneer', 'Zirconia Veneer'), ('Bruxzir Bridge 2', 'Bruxzir Bridge 2'), ('Bruxzir Bridge', 'Bruxzir Bridge'), ('Zirconia Bridge', 'Zirconia Bridge'), ('Lava Bridge', 'Lava Bridge'), ('Emax Bridge', 'Emax Bridge'), ('Empress Bridge', 'Empress Bridge'), ('Custom Abutment Anterior', 'Custom Abutment Anterior'), ('Custom Abutment Posterior', 'Custom Abutment Posterior'), ('Custom Zirconia Abutment Anterior', 'Custom Zirconia Abutment Anterior'), ('Custom Zirconia Abutment Posterior', 'Custom Zirconia Abutment Posterior'), ('Conus Abutment', 'Conus Abutment'), ('Hybrid Bar', 'Hybrid Bar')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='remarks',
            field=models.TextField(default='No remarks', max_length=500, null=True),
        ),
    ]
