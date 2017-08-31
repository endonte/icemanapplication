from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
	model = Product
	template_name = 'product-list.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)

		context['products'] = Product.objects.all()

		return context
