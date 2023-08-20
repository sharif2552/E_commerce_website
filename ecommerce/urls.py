
from django.contrib import admin
from django.urls import path, include
from products import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('vendors/', include('vendors.urls')),
    path('myuser/', include('myuser.urls')),
    

]



# Include this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)