from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('increase_quantity/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove_item/<int:product_id>/', views.remove_item, name='remove_item'),
    # ... Other cart URLs ...
]
