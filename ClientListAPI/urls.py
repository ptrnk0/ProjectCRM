from django.urls import path
from .views import clients, client, ClientList, Client, ClientListView, SingleClientView

urlpatterns = [
    path('clients/', clients, name='ClientListAPI'),
    # path('clients', ClientListView.as_view()),
    # path('clients/<int:pk>', SingleClientView.as_view()),
    path('clients/<int:pk>', client),
]