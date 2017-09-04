from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Customer, Billing_Details, Shipping_Details
from .forms import CustomerForm, CustomerBillingForm


class CreateCustomerListView(ListView, ModelFormMixin):
    model = Customer
    form_class = CustomerForm
    template_name = 'create-customer.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.created_by = request.user
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect(reverse(
                'create-customer-billing',
                args=(self.object.pk,)
            ))

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateCustomerListView, self).get_context_data(*args, **kwargs)

        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context

class CreateBillingListView(ListView, ModelFormMixin):
    model = Billing_Details
    form_class = CustomerBillingForm
    template_name = 'create-customer-billing.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        customer = Customer.objects.get(id=self.kwargs['pk'])
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        customer = Customer.objects.get(id=self.kwargs['pk'])
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.customer_id=customer
            self.object.save()

        return HttpResponseRedirect(reverse('customer-list'))

    def get_context_data(self, *args, **kwargs):
        context = super(CreateBillingListView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        context['errorlist'] = self.form.errors
        context['customer'] = Customer.objects.get(pk=self.kwargs['pk'])

        return context

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerListView, self).get_context_data(*args, **kwargs)
        context['customers'] = Customer.objects.all()

        return context
