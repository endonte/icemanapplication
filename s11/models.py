from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator
from icemanapp.users.models import User


class Store(models.Model):
    store_no = models.CharField(
        max_length=4,
        primary_key=True,
        validators=[RegexValidator('[0-9]')],
    )
    store_address1 = models.CharField(
        max_length=100,
        verbose_name='Store Address Line 1',
    )
    store_address2 = models.CharField(
        max_length=100,
        verbose_name='Store Address Line 2',
        blank=True,
        null=True,
    )
    store_postal = models.CharField(
        verbose_name='Store Postal Code',
        max_length=6,
        validators=[RegexValidator('[0-9]')],
    )
    store_contact_no = models.CharField(
        verbose_name='Store Contact No',
        max_length=8,
        validators=[
            RegexValidator(
                regex='^([0-9]{8})$',
                message='8 digit phone number only',
                code='nomatch',
            )
        ]
    )
    store_district_area = models.CharField(
        max_length=2,
        verbose_name='Store District and Area',
    )
    assigned_driver = models.ForeignKey(
        'drivers.Drivers',
        verbose_name='Driver Responsible'
    )

    def __str__(self):
        return '7-11 Store #: {} | Assigned Driver: {}'.format(self.store_no, self.assigned_driver)


class StoreRequest(models.Model):
    requesting_store = models.ForeignKey(
        'Store',
        verbose_name='Requesting Store'
    )
    request_date = models.DateTimeField(
        default=datetime.now,
        verbose_name='Date of Request',
    )
    request_created_by = models.ForeignKey(
        User,
        verbose_name='Created By',
        related_name='+',
    )
    #On Confirmation
    request_fulfilled_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Request Fulfilled Date',
    )
    #On Confirmation
    request_invoice_no = models.CharField(
        max_length=10,
        verbose_name='Invoice No',
        blank=True,
        null=True,
        unique=True,
    )
    #On Confirmation
    request_confirmed_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name='Confirmed By',
        related_name='+',
    )
    assigned_driver = models.ForeignKey(
        'drivers.Drivers',
        verbose_name='Assigned Driver',
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{} Request No: {} Date: {}'.format(self.requesting_store, self.id, self.request_date)
