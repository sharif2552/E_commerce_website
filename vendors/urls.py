from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('<int:vendor_id>/', views.vendor_profile, name='vendor_profile'),
    path('vendor_dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('<int:vendor_id>/products/create/', views.vendor_product_create, name='vendor_product_create'),

]
