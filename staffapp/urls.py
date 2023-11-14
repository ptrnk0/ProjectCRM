from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import StaffList

urlpatterns = [
    path('all_staff/', login_required(StaffList.as_view()), name='all_staff'),
    path('create_staff/', login_required(views.create_staff_view), name='create_staff'),
    path('create_schedule/', login_required(views.create_schedule_staff), name='create_schedule'),
    path('api/v1/staffs', views.StaffAPIView.as_view())
]
