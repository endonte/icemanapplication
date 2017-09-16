from django.db import models
from django.core.validators import RegexValidator
from icemanapp.users.models import User

class Customer(models.Model):
    contact_name = models.CharField(
        verbose_name='Contact Name',
        max_length=50,
        help_text='Put Contact Name Here, Do not put business name',
    )
    contact_number = models.CharField(
        verbose_name='Contact Number',
        max_length=17,
        validators=[RegexValidator('[0-9]')],
        help_text='Put 8 digit Singapore Number',
    )
    contact_email = models.EmailField(
        verbose_name='Contact Email',
    )
    company_name = models.CharField(
        verbose_name='Company Name',
        max_length=75,
        help_text='Business Trading Name',
        null=True,
        blank=True,
    )
    company_reg_no = models.CharField(
        verbose_name='Company Registration Number',
        max_length=10,
        null=True,
        blank=True,
    )
    customer_code = models.CharField(
        verbose_name='Customer Code',
        max_length=10,
        null=True,
        blank=True
        )
    created_by = models.ForeignKey(
        User,
        verbose_name='Created By',
    )

    def __str__(self):
        if self.company_name:
            return self.company_name
        return self.contact

class Billing_Details(models.Model):
    customer_id = models.OneToOneField(Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    billing_address_line1 = models.CharField(
        max_length=75,
        verbose_name='Block Number and Street Name',
        blank=True,
        null=True,
    )
    billing_address_line2 = models.CharField(
        max_length=75,
        verbose_name='Unit Number and Building Name',
        blank=True,
        null=True,
    )
    billing_postal = models.CharField(
        verbose_name='Billing Postal Code',
        blank=True,
        null=True,
        validators=[RegexValidator('[0-9]')],
        max_length=6,
    )

class Shipping_Details(models.Model):
    customer_id = models.ForeignKey('Customer',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    shipping_address_line1 = models.CharField(
        max_length=75,
        verbose_name='Block Number and Street Name',
    )
    shipping_address_line2 = models.CharField(
        max_length=75,
        verbose_name='Unit Number and Building Name',
        blank=True,
        null=True,
    )
    shipping_postal = models.CharField(
        verbose_name='Shipping Postal Code',
        validators=[RegexValidator('[0-9]')],
        max_length=6,
    )

    def __str__(self):
        return '{} {} {}'.format(self.shipping_address_line1, self.shipping_address_line2, self.shipping_postal)
