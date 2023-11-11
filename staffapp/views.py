from django.shortcuts import render
from .models import Staff
from .forms import CreateStaffForm, CreateScheduleStaffForm


def all_staff_view(request):
    if request.method == 'POST':
        Staff.objects.filter(id=request.POST.get('id')).delete()
        st = Staff.objects.all()
        return render(request, 'staffapp/all_staff.html', {'staff': st})
    st = Staff.objects.all()
    return render(request, 'staffapp/all_staff.html', {'staff': st})


def create_staff_view(request):
    form = CreateStaffForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'staffapp/create_staff.html', context)


def create_schedule_staff(request):
    form = CreateScheduleStaffForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateScheduleStaffForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'staffapp/create_schedule_staff.html', context)
