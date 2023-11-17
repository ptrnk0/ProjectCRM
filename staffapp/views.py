from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from rest_framework import generics
from .models import Staff, Schedule
from .forms import CreateStaffForm, CreateScheduleStaffForm
from .serializers import StaffSerializer


class ListStaffView(ListView):
    model = Staff
    template_name = 'staffapp/staff_list.html'
    success_url = 'all_staff/'
    paginate_by = 10


class CreateStaffView(CreateView):
    model = Staff
    form_class = CreateStaffForm
    success_url = '/create_staff/'
    template_name = 'staffapp/staff_create.html'


class DetailStaffView(DetailView):
    model = Staff
    template_name = 'staffapp/staff_detail.html'


class CreateScheduleStaffView(CreateView):
    model = Schedule
    form_class = CreateScheduleStaffForm
    success_url = '/create_schedule/'
    template_name = 'staffapp/schedule_staff_create.html'


class DeleteStaffView(DeleteView):
    model = Staff
    success_url = '/all_staff/'
    template_name = 'staffapp/staff_delete_confirm.html'


class UpdateStaffView(UpdateView):
    fields = '__all__'
    model = Staff
    template_name = 'staffapp/staff_update_form.html'
    success_url = '/all_staff/'


def detail_schedule_staff(request, id_staff):
    schedule = Schedule.objects.filter(id_staff=id_staff)
    staff = Staff.objects.get(id=id_staff)
    return render(request, 'staffapp/detail_schedule_staff.html',
                  {'data_schedule': schedule, 'data_staff': staff})


class StaffAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
