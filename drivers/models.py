from django.db import models
from django.core.validators import RegexValidator

class Designation(models.Model):
    designation = models.CharField(
        max_length=30,
        unique=True,
    )
    PRIORITY_CHOICES = (
        ('1','Route Drivers'),
        ('2',''),
        ('3','Half-Agent'),
        ('4',''),
        ('5','Reserve Drivers'),
        ('6','Reserve Warehouse'),
        ('7','Agent'),
        ('8','Agent\'s Driver'),
        ('9','Unresponsive'),
        ('10',''),
    )
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{}'.format(self.designation)

    class Meta:
        ordering = ('priority', )

class Drivers(models.Model):
    full_name = models.CharField(
        max_length=75,
        verbose_name='Driver Name (Passport/IC)',
    )
    nick_name = models.CharField(
        max_length=50,
        verbose_name='Driver Nick Name',
        blank=True,
        null=True,
    )
    designation = models.ForeignKey(
        Designation,
        verbose_name='Driver Role'
    )
    phone_number = models.CharField(
        max_length=17,
        verbose_name='Contact Number',
        validators=[RegexValidator('[0-9]')],
    )
    wechat_id = models.CharField(
        max_length=100,
        verbose_name='Driver WeChat ID',
        blank=True,
        null=True,
    )
    delivery_areas = models.ManyToManyField(
        'Postal_Areas',
        verbose_name='Regions Served',
        blank=True,
    )
    delivery_restrictions = models.CharField(
        max_length=200,
        verbose_name='Delivery Restrictions',
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.nick_name:
            return '{} {}'.format(self.nick_name, self.designation.designation)
        return '{} {}'.format(self.full_name, self.designation.designation)

    class Meta:
        ordering = ('designation','full_name', )

class Postal_Areas(models.Model):
    postal_areas = models.CharField(
        max_length=2,
        validators=[RegexValidator('[0-9]')],
    )
    region_names = models.CharField(
        max_length=200,
        verbose_name='Postal Code Region Names'
    )

    def __str__(self):
        return '{} {}'.format(self.postal_areas, self.region_names)

    class Meta:
        ordering = ('postal_areas', )
