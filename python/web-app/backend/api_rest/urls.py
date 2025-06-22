from django.urls import path, include

from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('product/', views.create_product, name='create-product'),
    path('order/', views.create_order, name='create-order'),
    path('orders/', views.list_orders, name='list-orders'),
]
