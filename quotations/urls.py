from django.conf.urls import url
from .views import QuoteListView, CreateQuoteListView
from .views import CreateQuoteShippingListView, CreateQuoteProductListView, QuotePreviewListView
from .views import PrintView

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
    ),
    url(
        r'^create-quotation/quotation-preview-(?P<pk>\d+)/$',
        QuotePreviewListView.as_view(),
        name='quotation-preview'
    ),
    url(r'^quotation_list/quotation-id-(?P<pk>\d+)/$', PrintView.as_view(), name='pdf_printer'),
]
