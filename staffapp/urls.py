from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    path('all_staff/', login_required(views.all_staff_view, login_url='http://127.0.0.1:8000/admin'), name='all_staff'),
    path('create_staff/', login_required(views.create_staff_view, login_url='http://127.0.0.1:8000/admin'), name='create_staff'),
    path('create_schedule/', login_required(views.create_schedule_staff, login_url='http://127.0.0.1:8000/admin'), name='create_schedule'),
]
