from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('<slug:slug>/', views.product_info, name='product_info'),
]