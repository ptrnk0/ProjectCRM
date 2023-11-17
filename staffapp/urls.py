from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import ListStaffView, CreateStaffView, CreateScheduleStaffView, DetailStaffView, DeleteStaffView, \
    UpdateStaffView, detail_schedule_staff

urlpatterns = [
    path('all_staff/', login_required(ListStaffView.as_view()), name='all_staff'),
    path('create_staff/', login_required(CreateStaffView.as_view()), name='create_staff'),
    path('create_schedule/', login_required(CreateScheduleStaffView.as_view()), name='create_schedule'),
    path('staf_detail/<int:pk>', login_required(DetailStaffView.as_view()), name='staff_detail'),
    path('delete_staff/<int:pk>', login_required(DeleteStaffView.as_view()), name='delete_staff'),
    path('update_staff/<int:pk>', login_required(UpdateStaffView.as_view()), name='update_staff'),
    path('schedule_staff/<id_staff>', login_required(detail_schedule_staff), name='schedule_staff'),
    path('api/v1/staffs', views.StaffAPIView.as_view())
]
