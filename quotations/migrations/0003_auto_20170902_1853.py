# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0002_auto_20170902_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_gst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='GST'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Subtotal'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_type',
            field=models.CharField(choices=[('T1', 'GST Excluded, Quantity Not Required, Total Not Required'), ('T2', 'GST Included, Quantity Not Required, Total Not Required'), ('T3', 'GST Excluded, Quantity Required, Total Shown'), ('T4', 'GST Included, Quantity Required, Total Shown')], default='T1', max_length=2),
        ),
    ]