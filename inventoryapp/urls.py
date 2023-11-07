from django.urls import path
from inventoryapp import views

urlpatterns = [
    path('inventory/delete_order', views.orderDelete, name='delete_order'),
    path('inventory/delete_commodity', views.commodityDelete, name='delete_commodity'),
    path('inventory/<subDir>', views.inventory_form_view, name='inventory'),
]