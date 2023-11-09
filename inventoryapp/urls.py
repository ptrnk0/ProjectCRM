from django.urls import path
from inventoryapp import views
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [
    path('inventory/delete_order', login_required(views.orderDelete, login_url='http://127.0.0.1:8000/admin'), name='delete_order'),
    path('inventory/delete_commodity', login_required(views.commodityDelete, login_url='http://127.0.0.1:8000/admin'), name='delete_commodity'),
    path('inventory/<subDir>', login_required(views.inventory_form_view, login_url='http://127.0.0.1:8000/admin'), name='inventory'),
]