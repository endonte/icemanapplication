from django.conf.urls import url
from .views import QuoteListView, CreateQuoteListView, CreateQuoteShippingListView, CreateQuoteProductListView

urlpatterns = [
    url(
        r'^create-quotation/$',
        CreateQuoteListView.as_view(),
        name='create-quotation'
    ),
    url(
        r'^quotation-list/$',
        QuoteListView.as_view(),
        name='quotation-list'
    ),
    url(
        r'^create-quotation/quotation-shipping-(?P<pk>\d+)/$',
        CreateQuoteShippingListView.as_view(),
        name='quotation-shipping-add'
    ),
    url(
        r'^create-quotation/quotation-product-(?P<pk>\d+)/$',
        CreateQuoteProductListView.as_view(),
        name='quotation-product-add'
    )
]
