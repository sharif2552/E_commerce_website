from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from myuser.models import Vendor
from .models import Product
from django.db import models


@login_required(login_url='myuser:login')
def homepage(request):
    products = Product.objects.all()
    category_id = request.POST.get('categorySelect')
    print(category_id)
    search_input = request.POST.get('search_input')
    # Retrieve all categories and annotate each with product count
    categories = Category.objects.annotate(product_count=models.Count('product'))
    print(categories)
    selected_category = None  # Initialize as None

    products = Product.objects.all()

    if category_id:
        selected_category = int(category_id)  # Convert to int if not None
        products = products.filter(category_id=selected_category)
    return render(request, 'homepage.html', {'products': products, 'categories': categories, 'selected_category': selected_category})

@login_required(login_url='myuser:login')
def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required(login_url='myuser:login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            
            # Fetch the Vendor instance based on the logged-in user
            vendor_instance = Vendor.objects.get(user=request.user)
            product.vendor = vendor_instance  # Assign the Vendor instance
            
            product.save()  # Save the form with the vendor information
            return redirect('products:add_product')
    else:
        form = ProductForm()  # Create a new form instance
        
        # Exclude the 'vendor' field from the form

    return render(request, 'add_product.html', {'form': form})


from django.shortcuts import render
from .models import Product

from django.shortcuts import render
from .models import Category, Product



def filter_products(request):
    category_id = request.GET.get('category')
    search_input = request.GET.get('search')

    categories = Category.objects.annotate(product_count=models.Count('product'))

    selected_category = None
    products = Product.objects.all()

    if category_id is not None and category_id != "0":
        selected_category = int(category_id)
        products = products.filter(category_id=selected_category)

    if search_input:
        products = products.filter(name__icontains=search_input)
    
    # If no category is selected, do not apply category filtering
    
    return render(request, 'filter_products.html', {'products': products, 'categories': categories, 'selected_category': selected_category})


from django.shortcuts import render

from .models import Category

from django.shortcuts import render
from .models import Category  # Import your Category model here

def category_menu(request):
    categories = Category.objects.all()  # Retrieve all categories
    return render(request, 'category_menu.html', {'categories': categories})




from django.shortcuts import render, redirect
from .models import Product, CartItem

# views.py
from django.shortcuts import get_object_or_404
from orders.models import Order, OrderItem


from django.shortcuts import get_object_or_404, redirect

def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        user = request.user
        Total = 0
        # Retrieve the user's active (incomplete) order or create a new one
        order, created = Order.objects.get_or_create(user=user)
        
        # Create an OrderItem for the product and add it to the order
        order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'quantity': 1})
        
        if not item_created:
            order_item.quantity += 1
            order_item.save()

        return redirect('products:filter_products')  # Redirect to the product detail page or any other appropriate page




from django.shortcuts import render
from .models import CartItem, Product

def cart_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order = Order.objects.filter(user=customer).first()  # Assuming a user has only one active order
        
        cart_items = []  # Initialize an empty list for cart items
        total_price = 0  # Initialize total price
        
        if order:
            cart_items = OrderItem.objects.filter(order=order)
            for cart_item in cart_items:
                product_price = cart_item.product.price
                print(f"Product Price: {product_price}")
            total_price = sum(item.product.price * item.quantity for item in cart_items)
        
        context = {
            
            'cart_items': cart_items,
            'total_price': total_price
        }
        return render(request, 'cart.html', context)

# checkout/views.py
from django.shortcuts import render, redirect
from .models import Address
from products.models import Product  # Import the Product model
from django.contrib import messages

def checkout_view(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user)
    cart_items = OrderItem.objects.filter(order=order)


    for cart_item in cart_items:
                product_price = cart_item.product.price
                print(f"Product Price: {product_price}")
    total_price = sum(item.product.price * item.quantity for item in cart_items)  #total price
    order.Total = total_price
    order.save()       
    if request.method == 'POST':
        # Retrieve address fields from the form
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        zip_code = request.POST['zip-code']
        telephone = request.POST['tel']

        # Create an Address instance and save it to the database
        new_address = Address.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
            country=country,
            zip_code=zip_code,
            telephone=telephone,
        )
        new_address.save()


            # Associate the newly created address with the order
        order.address = new_address
        order.Total = total_price
        order.save()

        messages.success(request, 'Address saved and order placed successfully.')
        return redirect('payments:home')  # Redirect back to the checkout page

            


    cart_items = OrderItem.objects.filter(order=order)

    context = {
            
            'cart_items': cart_items,
            'total_price': total_price
        }
    return render(request, 'checkout.html', context)


# from sslcommerz_python.payment import SSLCSession
# from decimal import Decimal
# import socket
# def payment(request):
