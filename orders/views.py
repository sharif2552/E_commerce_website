from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orders.models import OrderItem
from products.models import Product  # Replace with your actual Product model import

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def increase_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = OrderItem.objects.filter(user = request.user , product=product).first()
    print(request.user)
    print(cart_item)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('products:cart_view')
from django.shortcuts import get_object_or_404, redirect
from .models import Product, OrderItem  # Import your models

def decrease_quantity(request, product_id):
    # Get the Product and CartItem
    product = get_object_or_404(Product, id=product_id)
    cart_item = OrderItem.objects.filter(user = request.user , product=product).first()
    print(request.user)
    print(cart_item)
    if cart_item:
        # Check if the cart_item exists
        if cart_item.quantity > 1:
            # Decrease the quantity by 1
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # Remove the item from the cart if quantity is 1
            cart_item.delete()
    else:
        print("not found")
    return redirect('products:cart_view')

def remove_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = OrderItem.objects.filter(user = request.user , product=product).first()
    
    if cart_item:
        cart_item.delete()
        messages.success(request, f'{product.name} removed from the cart.')
    
    return redirect('products:cart_view')
