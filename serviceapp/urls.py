from django.urls import path
from serviceapp import views
from django.contrib.auth.decorators import login_required
from serviceapp.views import ListResourceView, DetailResourceView, DeleteResourceView, CreateResourceView, \
    ListServiceView, DetailServiceView, CreateServiceView, DeleteServiceView, AddResourceForService, \
    list_resource_for_service

urlpatterns = [
    # path('service/delete_resource/', login_required(views.resourceDelete), name='delete_resource'),
    # path('service/delete_service/', login_required(views.serviceDelete), name='delete_service'),
    # path('service/<subDir>/', login_required(views.service_form_view), name='service'),
    path('service/list_resource/', login_required(ListResourceView.as_view()), name='list_resource'),
    path('service/create_resource/', login_required(CreateResourceView.as_view()), name='create_resource'),
    path('service/detail_resource/<int:pk>', login_required(DetailResourceView.as_view()), name='detail_resource'),
    path('service/delete_resource/<int:pk>', login_required(DeleteResourceView.as_view()), name='delete_resource'),
    path('service/list_service/', login_required(ListServiceView.as_view()), name='list_service'),
    path('service/create_service/', login_required(CreateServiceView.as_view()), name='create_service'),
    path('service/detail_service/<int:pk>', login_required(DetailServiceView.as_view()), name='detail_service'),
    path('service/delete_service/<int:pk>', login_required(DeleteServiceView.as_view()), name='delete_service'),
    path('service/add_resource_for_service', login_required(AddResourceForService.as_view()), name='add_resource_for_service'),
    path('service/resource_list_for_service/<id_service>', login_required(list_resource_for_service), name='resource_list_for_service')
]