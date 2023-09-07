from django.urls import path

from . import views  # Import your views module

app_name = 'myuser' # App name should match the namespace

urlpatterns = [
    # Other URL patterns...
    path('login/', views.login_view, name='login'), 
    path('signup/', views.signup_view, name='signup'), # Define your login view URL pattern
    # Other URL patterns...
    path('vendor_signup/', views.vendor_signup_view, name='vendor_signup'), # Define your
    path('vendor_login/', views.vendor_login_view, name='vendor_login'), # Define your login view URL pattern
    path('log_out/', views.logout_view, name='log_out'), # Define your login view URL pattern
    path('my-account/', views.my_account, name='my_account'),
]
