from django.contrib import admin
from .models import Orders_Adhoc, OrderItems, CustomerItems

admin.site.register(Orders_Adhoc)
admin.site.register(OrderItems)
admin.site.register(CustomerItems)