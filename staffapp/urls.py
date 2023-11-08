from django.urls import path
from . import views


urlpatterns = [
    path('all_staff/', views.all_staff_view, name='all_staff'),
    path('create_staff/', views.create_staff_view, name='create_staff')
]
