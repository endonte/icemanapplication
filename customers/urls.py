from django.conf.urls import url
from .views import CustomerListView, CreateCustomerListView, CreateBillingListView

urlpatterns = [
    url(r'^create-customer/$',
        CreateCustomerListView.as_view(),
        name='create-customer'
    ),
    url(r'^create-customer-billing-(?P<pk>\d+)/$',
        CreateBillingListView.as_view(),
        name='create-customer-billing'
    ),
    url(r'^customer-list/$',
        CustomerListView.as_view(),
        name='customer-list'
    ),
]
