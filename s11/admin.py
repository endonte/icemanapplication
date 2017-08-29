from django.contrib import admin
from .models import StoreRequest, Store

# Register your models here.
my_models = [StoreRequest, Store]
admin.site.register(my_models)
