from django.db import models
from django.utils import timezone
from datetime import datetime
from icemanapp.users.models import User


class Quote(models.Model):
    customer = models.ForeignKey(
        'customers.Customer',
        verbose_name='Customer Details',
    )
    billing_address = models.ForeignKey(
        'customers.Billing_Details',
        verbose_name='Billing Address',
        blank=True,
        null=True,
    )
    shipping_address = models.ForeignKey(
        'customers.Shipping_Details',
        verbose_name='Shipping Address',
        blank=True,
        null=True,
    )
    QUOTE_CHOICES = (
        ('T1','GST Excluded, Quantity Not Required, Total Not Required'),
        ('T2','GST Included, Quantity Not Required, Total Not Required'),
        ('T3','GST Excluded, Quantity Required, Total Shown'),
        ('T4','GST Included, Quantity Required, Total Shown'),
    )
    quote_type = models.CharField(
        max_length=2,
        choices=QUOTE_CHOICES,
        default='T1',
    )
    quote_subtotal = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='Subtotal',
    )
    quote_total = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='Total',
    )
    quote_gst = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='GST',
    )
    created_by = models.ForeignKey(
        User,
        verbose_name='Created By',
    )
    created_date = models.DateTimeField(
        default=datetime.now,
        verbose_name='Date of Creation',
    )
    confirmation_status = models.BooleanField(
        default=False,
        verbose_name='Confirmation Status',
    )
    def __str__(self):
        return 'Quote ID: {} Customer: {}'.format(self.id, self.customer)

class Quote_Products(models.Model):
    quote_reference = models.ForeignKey(
        'Quote',
        verbose_name='Quote ID',
    )
    quote_product = models.ForeignKey(
        'products.Product',
    )
    quote_product_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Product Price',
    )
    quote_product_qty = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Product Qty',
    )
    quote_product_gst = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Product GST',
    )
    quote_product_total = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Product Total',
    )
    quote_product_description = models.CharField(
        max_length=200,
        verbose_name='Product Description',
        blank=True,
        null=True,
    )
