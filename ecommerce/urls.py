
from django.contrib import admin
from django.urls import path, include
from products import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('vendors/', include('vendors.urls')),
    path('myuser/', include('myuser.urls')),
    

]
