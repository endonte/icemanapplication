from django.conf.urls import url
from .views import StoreListView, ActiveRequestListView, RequestHistoryListView, ConfirmRequestListView

urlpatterns = [
    url(r'^store-list/$',
        StoreListView.as_view(),
        name='store-list'
    ),
    url(r'^active-requests/$',
        ActiveRequestListView.as_view(),
        name='active-requests'
    ),
    url(r'^request-history/$',
        RequestHistoryListView.as_view(),
        name='request-history'
    ),
    url(
        r'^storeconfirm-id(?P<pk>\d+)/$',
        ConfirmRequestListView.as_view(),
        name='confirm-request',
    )
]
