# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 07:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('customers', '0002_auto_20170901_0157'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_type', models.CharField(choices=[('T1', 'Template 1: GST Excluded, Quantity Not Required, Total Not Required'), ('T2', 'Template 2: GST Included, Quantity Not Required, Total Not Required'), ('T3', 'Template 3: GST Excluded, Quantity Required, Total Shown'), ('T4', 'Template 4: GST Included, Quantity Required, Total Shown')], default='T1', max_length=2)),
                ('quote_subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Subtotal')),
                ('quote_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Total')),
                ('quote_gst', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='GST')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date of Creation')),
                ('confirmation_status', models.BooleanField(default=False, verbose_name='Confirmation Status')),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Billing_Details', verbose_name='Billing Address')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer', verbose_name='Customer Details')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.Shipping_Details', verbose_name='Shipping Address')),
            ],
        ),
        migrations.CreateModel(
            name='Quote_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_product_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Product Price')),
                ('quote_product_qty', models.IntegerField(blank=True, null=True, verbose_name='Product Qty')),
                ('quote_product_gst', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Product GST')),
                ('quote_product_total', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Product Total')),
                ('quote_product_description', models.CharField(max_length=200, verbose_name='Product Description')),
                ('quote_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('quote_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotations.Quote', verbose_name='Quote ID')),
            ],
        ),
    ]
