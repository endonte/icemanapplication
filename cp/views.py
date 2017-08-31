from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from icemanapp.users.models import User
from .forms import DriverEditForm, S11EditStoreForm, ProductEditForm, CategoryEditForm
from drivers.models import Drivers
from s11.models import Store
from products.models import Product

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

class S11StoreEditListView(ListView, ModelFormMixin):
    model = Store
    form_class = S11EditStoreForm
    template_name = 'edit-s11-store.html'

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

            return HttpResponseRedirect('/cp/edit-s11-store')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(S11StoreEditListView, self).get_context_data(*args, **kwargs)

        context['drivers'] = Drivers.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context


class ProductEditListView(ListView, ModelFormMixin):
    model = Product
    form_class = ProductEditForm
    form_class2 = CategoryEditForm
    template_name = 'edit-product.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        self.form2 = self.get_form(self.form_class2)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        self.form2 = self.get_form(self.form_class2)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.created_by = request.user
            self.object.save()
            self.form = self.get_form(self.form_class)
        elif self.form2.is_valid():
            self.object = self.form2.save(commit=False)
            self.object.save()
            self.form = self.get_form(self.form_class2)

        return HttpResponseRedirect('/cp/edit-product')

    def get_context_data(self, *args, **kwargs):
        context = super(ProductEditListView, self).get_context_data(*args, **kwargs)

        context['products'] = Product.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors
        context['form2'] = self.form2
        context['errorlist2'] = self.form2.errors

        return context
