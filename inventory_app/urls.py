from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('register-stock/', views.register_stock, name='register_stock'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),

]