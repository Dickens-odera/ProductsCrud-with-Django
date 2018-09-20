from django.contrib import admin
from .models import Customers

# Register your models here.

class CustomerTRegistration(admin.ModelAdmin):
    model = Customers
admin.site.register(Customers,CustomerTRegistration)