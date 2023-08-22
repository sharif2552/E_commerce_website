from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from myuser.models import Vendor
from .models import Product

@login_required(login_url='myuser:login')
def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})

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
