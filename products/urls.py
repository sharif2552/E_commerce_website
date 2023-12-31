
from django.urls import path
from . import views



app_name = 'products'  # App name should match the namespace

urlpatterns = [
    path('',views.homepage , name= 'homepage'),
     path('<int:product_id>/', views.product_detail, name='product_detail'),
     path('add_product/', views.add_product, name='add_product'),
     path('filter/', views.filter_products, name='filter_products'),
     path('categories/', views.category_menu, name='category_menu'),
     path('cart/', views.cart_view, name='cart_view'),
     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
     path('checkout/', views.checkout_view, name='checkout'),
     

]

