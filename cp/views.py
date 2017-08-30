from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from .forms import DriverEditForm
from drivers.models import Drivers

class DriverEditListView(ListView, ModelFormMixin):
    model = Drivers
    form_class = DriverEditForm
    template_name = 'edit-driver.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect('/cp/edit-driver')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(DriverEditListView, self).get_context_data(*args, **kwargs)

        context['drivers'] = Drivers.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context
