
from django.urls import path
from . import views



app_name = 'products'  # App name should match the namespace

urlpatterns = [
    path('',views.homepage , name= 'homepage'),
     path('<int:product_id>/', views.product_detail, name='product_detail'),
     
]

