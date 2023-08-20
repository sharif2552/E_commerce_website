from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render
from .models import Category, Product

@login_required(login_url='myuser:login')
def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})


@login_required(login_url='myuser:login')
def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})
