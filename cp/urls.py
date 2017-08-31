from django.conf.urls import url
from .views import DriverEditListView, S11StoreEditListView,ProductEditListView

urlpatterns = [
    url(r'^edit-driver/$',
        DriverEditListView.as_view(),
        name='edit-driver'
    ),
    url(r'^edit-s11-store/$',
        S11StoreEditListView.as_view(),
        name='edit-s11-store'
    ),
    url(r'^edit-product/$',
        ProductEditListView.as_view(),
        name='edit-product'
    ),
]
