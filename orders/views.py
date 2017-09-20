from django.views.generic import ListView, View
from django.shortcuts import render
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from icemanapp.users.models import User
from django.utils import timezone
from .models import Orders_Adhoc, OrderItems, CustomerItems
from .forms import OrderCreateForm, OrderProductForm, OrderConfirmForm
from quotations.models import Quote_Products, Quote
from products.models import Product

class OrderListView(ListView):
	model = Orders_Adhoc
	template_name = 'order-list.html'

	def get_context_data(self, *args, **kwargs):
		context = super(OrderListView, self).get_context_data(*args, **kwargs)
		context['orders'] = Orders_Adhoc.objects.filter(confirmation_status=False)

		return context

class ActiveOrderListView(ListView):
	model = Orders_Adhoc
	template_name = 'active-orders.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ActiveOrderListView, self).get_context_data(*args, **kwargs)
		context['orders'] = Orders_Adhoc.objects.filter(confirmation_status=True)

		return context


class CreateOrderListView(ListView, ModelFormMixin):
	model = Orders_Adhoc
	form_class = OrderCreateForm
	template_name = 'create-order.html'

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
			self.object.save()

			return HttpResponseRedirect(reverse(
				'order-add-product',
				args=(self.object.id,)
				))

		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(CreateOrderListView, self).get_context_data(*args, **kwargs)
		context['form'] = self.form
		return context

class OrderAddProductListView(ListView, ModelFormMixin):
	model = OrderItems
	form_class = OrderProductForm
	form_class2 = OrderConfirmForm
	template_name = 'create-order-products.html'

	def get(self, request, *args, **kwargs):
		self.object = None
		self.order = Orders_Adhoc.objects.get(pk=self.kwargs['pk'])
		self.form = self.get_form(self.form_class)
		self.form2 = self.get_form(self.form_class2)

		return ListView.get(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = None
		self.order = Orders_Adhoc.objects.get(pk=self.kwargs['pk'])
		self.form = OrderProductForm(pk=self.kwargs['pk'])
		self.form2 = self.get_form(self.form_class2)

		if self.form.is_valid():
			self.object = self.form.save(commit=False)
			self.object.order_reference = self.order
			self.object.order_product_price = CustomerItems.objects.get(item_reference=self.object.order_product).item_price
			self.object.save()

			return HttpResponseRedirect(reverse(
				'order-add-product', 
				args=(self.order.pk,)
				))

		if self.form2.is_valid():
			self.order.confirmation_status=True
			self.order.save()

			return HttpResponseRedirect(reverse(
				'active-orders'
				))

		return self.get(request, *args, **kwargs)


	def get_context_data(self, *args, **kwargs):
		context = super(OrderAddProductListView, self).get_context_data(*args, **kwargs)
		context['form'] = self.form
		context['order'] = self.order
		context['order_items'] = OrderItems.objects.filter(
		    order_reference=self.order
		)
		return context


