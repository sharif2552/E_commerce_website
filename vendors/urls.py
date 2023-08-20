from django.urls import path
from . import views

urlpatterns = [
    path('<int:vendor_id>/', views.vendor_profile, name='vendor_profile'),
    path('<int:vendor_id>/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('<int:vendor_id>/products/create/', views.vendor_product_create, name='vendor_product_create'),
]
