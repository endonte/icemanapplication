from django.db import models
from datetime import datetime
from icemanapp.users.models import User

class Orders_Adhoc(models.Model):
	customer = models.ForeignKey(
		'customers.Customer',
		verbose_name='Customer',
		)
	delivery_date = models.DateTimeField(
		default=datetime.now,
		verbose_name='Delivery Date',
		)
	created_date = models.DateTimeField(
		default=datetime.now,
		verbose_name='Creation Date',
		)
	created_by = models.ForeignKey(
		User,
		verbose_name='Created By',
		)
	confirmation_status = models.BooleanField(
		default=False,
		verbose_name='Confirmations Status',
		)
	def __str__(self):
		return '{}'.format(self.id)

class OrderItems(models.Model):
	# Fixed to Order
	order_reference = models.ForeignKey(
		'Orders_Adhoc',
		verbose_name='Order Reference',
		)
	# Selected based on Quoted Products
	order_product = models.ForeignKey(
		'products.Product',
		verbose_name='Product',
		)
	# Keyed in
	order_product_qty = models.IntegerField(
		verbose_name='Order Qty',
		)
	# Fixed to quoted product selection
	order_product_price = models.DecimalField(
		max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='Price',
		)
	# Keyed in
	additional_details = models.CharField(
		max_length=200,
		verbose_name='Additional Details',
		null=True,
		blank=True,
		)

class CustomerItems(models.Model):
	item_reference = models.ForeignKey(
		'products.Product',
		verbose_name='Product',
		blank=True,
		null=True,
		)
	customer_reference = models.ForeignKey(
		'customers.Customer',
		verbose_name='Customer',
		blank=True,
		null=True,
		)
	item_price = models.DecimalField(
		max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name='Price',
        blank=True,
		null=True,
		)
