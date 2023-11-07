from django.urls import path
from clientapp import views

urlpatterns = [
    
    path('client/delete_client', views.clientDelete, name='delete'),
    path('client/<subClient>', views.client_form_view, name='client'),
]