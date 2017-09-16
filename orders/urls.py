from django.conf.urls import url
from .views import CreateOrderListView, ActiveOrderListView, OrderAddProductListView
from .views import OrderListView

urlpatterns = [
    url(
        r'^create-order/$',
        CreateOrderListView.as_view(),
        name='create-order'
    ),
    url(
        r'^active-orders/$',
        ActiveOrderListView.as_view(),
        name='active-orders'
    ),
    url(
        r'^create-order/(?P<pk>\d+)/$',
        OrderAddProductListView.as_view(),
        name='order-add-product'
    ),
    url(
        r'^order-list/$',
        OrderListView.as_view(),
        name='order-list'
    ),
]