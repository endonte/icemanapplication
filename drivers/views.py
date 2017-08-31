from django.views.generic import ListView
from django.http import HttpResponse
import json
from .models import Drivers, Designation, Postal_Areas
from .forms import DriverForm

# Create your views here.
class DriverListView(ListView):
    model = Drivers
    template_name = 'driver-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DriverListView, self).get_context_data(*args, **kwargs)

        dictionaries = [driver.as_dict() for driver in Drivers.objects.all()]
        dictionaries2 = [
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
            }
        ]

        context['rows_json'] = json.dumps(dictionaries)
        context['columns_json'] = json.dumps(dictionaries2)
        context['drivers'] = Drivers.objects.all()

        return context

class RegionSearchListView(ListView):
    model = Drivers
    template_name = 'region-search.html'
    critical_value = 70
    token = False

    def get_queryset(self):
        invoice = self.request.GET.get('invoice')
        value = self.request.GET.get('value')
        if value:
            if int(value) > self.critical_value:
                self.token = True
            else:
                self.token = False
        if invoice:
            return Drivers.objects.filter(delivery_areas__postal_areas=invoice[0:2])
        else:
            return Drivers.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(RegionSearchListView, self).get_context_data(*args, **kwargs)

        context['designation'] = Designation.objects.all()
        context.update({'drivers': self.get_queryset, 'token': self.token})

        return context
