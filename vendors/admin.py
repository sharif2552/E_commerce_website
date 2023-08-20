from django.contrib import admin
from .models import Vendor, Order, OrderItem , VendorProduct


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('vendor','id', 'order', 'product', 'quantity')  # Display relevant fields for order items


@admin.register(VendorProduct)
class VendorProductAdmin(admin.ModelAdmin):
    list_display =  ('name', 'stock_quantity', 'description' , 'price')