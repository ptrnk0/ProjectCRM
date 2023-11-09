from django.urls import path, re_path
from django.urls import re_path as url
from clientapp import views
from django.contrib.auth.decorators import login_required, permission_required 


urlpatterns = [
    
    path('client/delete_client', login_required(views.clientDelete, login_url='http://127.0.0.1:8000/admin'), name='delete'),
    path('client/<subClient>', login_required(views.client_form_view, login_url='http://127.0.0.1:8000/admin'), name='client'),
]