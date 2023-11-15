from django.urls import path
from .views import clients, ClientList, Client

urlpatterns = [
    # path('clients/', clients, name='ClientListAPI'),
    path('clients', ClientList.as_view()),
    path('clients/<int:pk>', Client.as_view()),
]