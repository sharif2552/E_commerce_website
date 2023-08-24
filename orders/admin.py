from django.contrib import admin
from .models import Order , OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('vendor','id', 'order', 'product', 'quantity')  # Display relevant fields for order items
