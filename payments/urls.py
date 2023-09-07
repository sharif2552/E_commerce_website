# payments/urls.py

from django.urls import path

from . import views
app_name = 'payments'
urlpatterns = [
    path('home', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook), # new
]