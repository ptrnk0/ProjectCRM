from django.urls import path, re_path
from clientapp import views
from django.contrib.auth.decorators import login_required, permission_required 


urlpatterns = [
    
    path('client/delete_client/', login_required(views.clientDelete), name='delete'),
    path('client/<subClient>/', login_required(views.client_form_view), name='client'),
]