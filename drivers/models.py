from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Designation(models.Model):
    designation = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.designation)

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
    )

    def __str__(self):
        if self.nick_name:
            return '{}'.format(self.nick_name)
        return '{}'.format(self.full_name)

    class Meta:
        ordering = ('full_name', )

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
        return self.postal_areas

    class Meta:
        ordering = ('postal_areas', )
