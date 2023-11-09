from django.shortcuts import render
from .models import Staff
from .forms import CreateStaffForm, CreateScheduleStaffForm


def all_staff_view(request):
    st = Staff.objects.all()
    return render(request, 'staffapp/all_staff.html', {'staff': st})


def create_staff_view(request):
    form = CreateStaffForm()
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'staffapp/create_staff.html', context)


def create_schedule_staff(request):
    form = CreateScheduleStaffForm()
    if request.method == 'POST':
        form = CreateScheduleStaffForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'staffapp/create_schedule_staff.html', context)
