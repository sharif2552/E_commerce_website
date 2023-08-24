from django.contrib import admin
from .models import Category, Product, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


from django.contrib import admin
from .models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_product_names', 'quantity')

    def get_product_names(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    
    get_product_names.short_description = 'Products'
