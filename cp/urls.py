from django.conf.urls import url
from .views import DriverEditListView

urlpatterns = [
    url(r'^edit-driver/$',
        DriverEditListView.as_view(),
        name='edit-driver'
    ),

]
