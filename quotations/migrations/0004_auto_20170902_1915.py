# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0003_auto_20170902_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_gst',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='GST'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Subtotal'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Total'),
        ),
    ]
