from django.views.generic import ListView
from .models import Drivers, Designation, Postal_Areas
from .forms import DriverForm

# Create your views here.
class DriverListView(ListView):
    model = Drivers
    template_name = 'driver-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DriverListView, self).get_context_data(*args, **kwargs)

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
