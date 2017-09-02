# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_auto_20170901_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='priority',
            field=models.CharField(blank=True, choices=[('1', 'Route Drivers'), ('2', ''), ('3', 'Half-Agent'), ('4', ''), ('5', 'Reserve Drivers'), ('6', 'Reserve Warehouse'), ('7', 'Agent'), ('8', "Agent's Driver"), ('9', 'Unresponsive'), ('10', '')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='delivery_areas',
            field=models.ManyToManyField(blank=True, null=True, to='drivers.Postal_Areas', verbose_name='Regions Served'),
        ),
    ]
