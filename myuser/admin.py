from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser ,Vendor , Customer

admin.site.register(CustomUser, UserAdmin)
#admin.site.register(Customer, UserAdmin)
admin.site.register(Customer)
admin.site.register(Vendor)