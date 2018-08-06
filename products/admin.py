from django.contrib import admin
from .models import Products
# Register your models here.
class ProductsModel(admin.ModelAdmin):
    model = Products
admin.site.register(Products,ProductsModel)
