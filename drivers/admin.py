from django.contrib import admin
from .models import Designation, Drivers, Postal_Areas

# Register your models here.
my_models = [Designation, Drivers, Postal_Areas]
admin.site.register(my_models)
