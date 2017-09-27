from django.views.generic import ListView, View
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from decimal import Decimal
from icemanapp.users.models import User
from django.utils import timezone
from .models import Quote, Quote_Products
from customers.models import Customer, Shipping_Details, Billing_Details
from products.models import Product
from .forms import QuoteCreateForm, QuoteShippingNewForm, QuoteShippingExistingForm
from .forms import QuoteProductTotalForm, QuoteProductNoTotalForm, QuoteConfirmForm
from .utils import render_to_pdf


class QuoteListView(ListView):
    model = Quote
    template_name = 'quotation-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuoteListView, self).get_context_data(*args, **kwargs)
        context['quotations'] = Quote.objects.all()

        return context

class CreateQuoteListView(ListView, ModelFormMixin):
    model = Quote
    form_class = QuoteCreateForm
    template_name = 'create-quotation.html'

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
            self.object.created_date = timezone.now()
            billing_qs = Billing_Details.objects.filter(customer_id=self.object.customer.id)
            if billing_qs:
                self.object.billing_address = Billing_Details.objects.get(customer_id=self.object.customer.id)
            self.object.save()

            return HttpResponseRedirect(reverse('quotation-shipping-add', args=(self.object.pk,)))

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateQuoteListView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context


class CreateQuoteShippingListView(ListView, ModelFormMixin):
    model = Shipping_Details
    form_class = QuoteShippingNewForm
    form_class2= QuoteShippingExistingForm
    template_name = 'create-quotation-shipping.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.quote_id = Quote.objects.get(id=self.kwargs['pk'])
        quote_customer = self.quote_id.customer
        # For existing shipping details
        self.shipping_qs = Shipping_Details.objects.filter(customer_id=quote_customer.id)
        # For new shipping details
        self.form = self.get_form(self.form_class)
        self.form2 = self.get_form(self.form_class2)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.quote_id = Quote.objects.get(id=self.kwargs['pk'])
        quote_customer = self.quote_id.customer
        # For existing shipping details
        self.shipping_qs = Shipping_Details.objects.filter(customer_id=quote_customer.id)
        # For new shipping details
        self.form = self.get_form(self.form_class)
        self.form2 = self.get_form(self.form_class2)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            #self.object.quote_id = Quote.objects.get(pk=self.kwargs['pk'])
            self.object.customer_id=quote_customer

            self.object.save()
            return HttpResponseRedirect(
                reverse('quotation-shipping-add',
                    args=(
                        self.kwargs['pk'],
                    )
                )
            )
        elif self.form2.is_valid():
            self.object = self.form2.save(commit=False)
            self.quote_id.shipping_address=self.object.shipping_address
            self.quote_id.save()
            return HttpResponseRedirect(
                reverse('quotation-product-add',
                    args=(
                        self.kwargs['pk'],
                    )
                )
            )
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateQuoteShippingListView, self).get_context_data(*args, **kwargs)

        self.form2.fields['shipping_address'].queryset = self.shipping_qs
        context['form'] = self.form
        context['form2'] = self.form2
        context['quote_pk'] = self.quote_id

        return context

class CreateQuoteProductListView(ListView, ModelFormMixin):
    model = Quote_Products
    form_class = QuoteProductNoTotalForm
    form_class2 = QuoteConfirmForm
    template_name = 'create-quotation-products.html'
    gst = Decimal(.07)

    def form_type(self, *args, **kwargs):
        quote_id = Quote.objects.get(pk=self.kwargs['pk'])
        template = quote_id.quote_type
        if template == 'T1' or template == 'T2':
            self.form_class = QuoteProductNoTotalForm
        elif template == 'T3' or template == 'T4':
            self.form_class = QuoteProductTotalForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.quote = Quote.objects.get(pk=self.kwargs['pk'])
        self.form_type()
        self.form = self.get_form(self.form_class)
        self.form2 = self.get_form(self.form_class2)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.quote = Quote.objects.get(pk=self.kwargs['pk'])
        self.form_type()
        self.form = self.get_form(self.form_class)
        self.form2 = self.get_form(self.form_class2)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.quote_reference = self.quote
            if self.object.quote_product_qty:
                self.object.quote_product_total = self.object.quote_product_price * self.object.quote_product_qty
                if self.quote.quote_type == 'T3':
                    self.object.quote_product_gst = self.object.quote_product_total * self.gst
                    self.object.quote_product_total += self.object.quote_product_gst
                elif self.quote.quote_type == 'T4':
                    self.object.quote_product_gst = self.object.quote_product_total * self.gst / (Decimal(1) + self.gst)

                self.quote.quote_gst += self.object.quote_product_gst
                self.quote.quote_total += self.object.quote_product_total
                self.quote.quote_subtotal += self.object.quote_product_total/(Decimal(1)+self.gst)
            self.object.save()
            self.quote.save()

            return HttpResponseRedirect(
                reverse('quotation-product-add',
                    args=(
                        self.kwargs['pk'],
                    )
                )
            )
        if self.form2.is_valid():
            self.quote.confirmation_status = True
            self.quote.save()

            return HttpResponseRedirect(
                reverse('quotation-preview',
                    args=(
                        self.kwargs['pk'],
                    )
                )
            )

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateQuoteProductListView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        context['form2'] = self.form2
        context['quote_pk'] = self.quote
        context['quote_products'] = Quote_Products.objects.filter(
            quote_reference=self.quote
        ).order_by('id')
        return context


class QuotePreviewListView(ListView):
    model = Quote
    template_name = 'create-quotation-preview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuotePreviewListView, self).get_context_data(*args, **kwargs)
        context['quote'] = Quote.objects.get(pk=self.kwargs['pk'])
        context['products'] = Quote_Products.objects.filter(
            quote_reference=Quote.objects.get(pk=self.kwargs['pk'])
        )

        return context

class PrintView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'quote_pk': Quote.objects.get(pk=self.kwargs['pk']),
            'quote_products': Quote_Products.objects.filter(
                quote_reference=Quote.objects.get(pk=self.kwargs['pk'])
            ).order_by('id'),
        }
        pdf = render_to_pdf('pdf/quotation-pdf-1.html', data)
        instance = Quote.objects.get(pk=self.kwargs['pk'])
        if instance.quote_type == 'T2':
            pdf = render_to_pdf('pdf/quotation-pdf-2.html', data)
        elif instance.quote_type == 'T3':
            pdf = render_to_pdf('pdf/quotation-pdf-3.html', data)
        elif instance.quote_type == 'T4':
            pdf = render_to_pdf('pdf/quotation-pdf-4.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
