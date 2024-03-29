from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('about/', views.about_info, name='about_info'),
    path('<slug:slug>', views.product_info, name='product_info'),
    path('store/<slug:category_slug>/', views.categories_list, name='categories_list'),
    path('get-quantities/', views.get_quantities, name='get_quantities'),
]