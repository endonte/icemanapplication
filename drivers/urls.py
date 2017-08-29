from django.conf.urls import url
from .views import DriverListView, RegionSearchListView

urlpatterns = [
    url(r'^driver-list/$', DriverListView.as_view(), name='driver-list'),
    url(r'^region-search/$', RegionSearchListView.as_view(), name='region-search'),
]
