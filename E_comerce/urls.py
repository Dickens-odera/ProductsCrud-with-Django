from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url('products/',include('products.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', include('products.urls'))
]
