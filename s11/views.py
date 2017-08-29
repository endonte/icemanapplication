from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from icemanapp.users.models import User
from django.utils import timezone
from .models import Store, StoreRequest
from drivers.models import Drivers
from .forms import StoreForm, StoreRequestForm, StoreConfirmForm

# Create your views here.
class StoreListView(ListView, ModelFormMixin):
    model = Store
    form_class = StoreForm
    template_name = 'store-list.html'

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

            return HttpResponseRedirect('/s11/store-list')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(StoreListView, self).get_context_data(*args, **kwargs)

        context['stores'] = Store.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context


class ActiveRequestListView(ListView, ModelFormMixin):
    model = StoreRequest
    form_class = StoreRequestForm
    second_form_class = StoreConfirmForm
    template_name = 'active-request.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.request_created_by = request.user
            self.object.request_date = timezone.now()
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect('/s11/active-requests')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ActiveRequestListView, self).get_context_data(*args, **kwargs)

        context['storerequests'] = StoreRequest.objects.exclude(request_invoice_no__isnull=False)
        context['form'] = self.form
        context['datenow'] = timezone.now()
        context['errorlist'] = self.form.errors

        return context


class ConfirmRequestListView(ListView, ModelFormMixin):
    model = StoreRequest
    form_class = StoreConfirmForm
    template_name = 'confirm-request.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        record_request_id = StoreRequest.objects.get(id=self.kwargs['pk'])
        self.form = StoreConfirmForm(request.POST, instance=record_request_id)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        record_request_id = StoreRequest.objects.get(id=self.kwargs['pk'])
        self.form = StoreConfirmForm(request.POST, instance=record_request_id)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.request_confirmed_by = request.user
            self.object.request_fulfilled_date = timezone.now()
            self.object.save()

            return HttpResponseRedirect('/s11/active-requests')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ConfirmRequestListView, self).get_context_data(*args, **kwargs)

        context['request_details'] = StoreRequest.objects.get(pk=self.kwargs['pk'])
        context['form'] = self.form

        return context


class RequestHistoryListView(ListView):
    model = StoreRequest
    template_name = 'request-history.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RequestHistoryListView, self).get_context_data(*args, **kwargs)

        context['request_details'] = StoreRequest.objects.exclude(request_invoice_no__isnull=True)

        return context
