from django.db import models
from django.core.validators import RegexValidator
from django.core import serializers

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
    delivery_restrictions = models.CharField(
        max_length=200,
        verbose_name='Delivery Restrictions',
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.nick_name:
            return '{}'.format(self.nick_name)
        return '{}'.format(self.full_name)

    def as_dict(self):
        return {
            "full_name": self.full_name,
            "nick_name": self.nick_name,
            "designation": self.designation.designation,
            "phone_number": self.phone_number,
            "wechat_id": self.wechat_id,
            "delivery_areas": serializers.serialize('json',
                self.delivery_areas.filter(id=self.id)
            ),
            "delivery_restrictions": self.delivery_restrictions,
        }
    def column_as_dict(self):
        return {
            {"name": "fullName",
                "title": Drivers._meta.get_field('full_name').verbose_name
            },
            {"name": "nickName",
                "title": Drivers._meta.get_field('nick_name').verbose_name
            },
            {"name": "designation",
                "title": Drivers._meta.get_field('designation').verbose_name
            },
            {"name": "phoneNumber",
                "title": Drivers._meta.get_field('phone_number').verbose_name
            },
            {"name": "wechatId",
                "title": Drivers._meta.get_field('wechat_id').verbose_name
            },
            {"name": "deliveryAreas",
                "title": Drivers._meta.get_field('delivery_areas').verbose_name
            },
            {"name": "deliveryRestrictions",
                "title": Drivers._meta.get_field('delivery_restrictions').verbose_name
            },
        }

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
        return '{} {}'.format(self.postal_areas, self.region_names)

    class Meta:
        ordering = ('postal_areas', )
