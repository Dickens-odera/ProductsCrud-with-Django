from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    path('list/', views.ListCustomers, name='list_customers'),
    path('add/', views.AddCustomer, name='add_customer'),
    path('update/<int:id>', views.UpdateCustomer, name='update')
    #path('register/', views.register, name='register'),
]
