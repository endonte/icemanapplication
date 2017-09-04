from django.conf.urls import url
from .views import ProductListView

urlpatterns = [
    url(r'^product-list/$', ProductListView.as_view(), name='product-list'),
]
