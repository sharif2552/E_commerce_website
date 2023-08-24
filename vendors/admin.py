from django.contrib import admin
from .models import  VendorProduct




@admin.register(VendorProduct)
class VendorProductAdmin(admin.ModelAdmin):
    list_display =  ('name', 'stock_quantity', 'description' , 'price')