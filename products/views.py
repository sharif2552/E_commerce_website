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

from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import render
from .models import Category, Product

from django.shortcuts import render
from .models import Product, Category

def filter_products(request):
    category_id = request.GET.get('category')
    search_input = request.GET.get('search')

    categories = Category.objects.annotate(product_count=models.Count('product'))

    selected_category = None
    products = Product.objects.all()

    if category_id:
        selected_category = int(category_id)
        products = products.filter(category_id=selected_category)

    if search_input:
        products = products.filter(name__icontains=search_input)

    return render(request, 'filter_products.html', {'products': products, 'categories': categories, 'selected_category': selected_category})


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category

from django.shortcuts import render
from .models import Category  # Import your Category model here

def category_menu(request):
    categories = Category.objects.all()  # Retrieve all categories
    return render(request, 'category_menu.html', {'categories': categories})




