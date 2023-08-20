from django.urls import path

from . import views  # Import your views module

app_name = 'myuser' # App name should match the namespace

urlpatterns = [
    # Other URL patterns...
    path('login/', views.login_view, name='login'), 
    path('signup/', views.signup_view, name='signup') # Define your login view URL pattern
    # Other URL patterns...
]
