from django.contrib import admin
from django.urls import path
from clientapp import views

urlpatterns = [
    path('client/<subClient>', views.client_form_view, name='new_client_form'),
]