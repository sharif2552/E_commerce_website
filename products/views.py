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


