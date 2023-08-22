from django.shortcuts import render
from myuser.models import Vendor
from products.models import Product

def vendor_profile(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    return render(request, 'vendors/vendor_profile.html', {'vendor': vendor})

def vendor_dashboard(request):
    vendor_id = request.user.id
    if vendor_id:
        print(" this")
        print(vendor_id)
        print(" this ")
    else:
        print(" no vendor")
    vendor = Vendor.objects.get(user_id=vendor_id)
    products = Product.objects.filter(vendor=vendor)
    return render(request, 'vendor_dashboard.html', {'vendor': vendor, 'products': products})

def vendor_product_create(request, vendor_id):
    # Logic to create a new product for the vendor
    pass
