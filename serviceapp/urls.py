from django.urls import path
from serviceapp import views
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [
    path('service/delete_resource', login_required(views.resourceDelete), name='delete_resource'),
    path('service/delete_service', login_required(views.serviceDelete), name='delete_service'),
    path('service/<subDir>', login_required(views.service_form_view), name='service'),
]