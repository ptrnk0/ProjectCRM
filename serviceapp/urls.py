from django.urls import path
from serviceapp import views

urlpatterns = [
    path('service/delete_resource', views.resourceDelete, name='delete_resource'),
    path('service/delete_service', views.serviceDelete, name='delete_service'),
    path('service/<subDir>', views.service_form_view, name='service'),
]