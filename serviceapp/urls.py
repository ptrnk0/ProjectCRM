from django.urls import path
from serviceapp import views
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [
    path('service/delete_resource', login_required(views.resourceDelete, login_url='http://127.0.0.1:8000/admin'), name='delete_resource'),
    path('service/delete_service', login_required(views.serviceDelete, login_url='http://127.0.0.1:8000/admin'), name='delete_service'),
    path('service/<subDir>', login_required(views.service_form_view, login_url='http://127.0.0.1:8000/admin'), name='service'),
]