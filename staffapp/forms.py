from django import forms
from .models import Staff, Schedule


class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'sex': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'job_title': forms.TextInput(attrs={"class": "form-control"}),
            'access_level': forms.NumberInput(attrs={"class": "form-control"}),
        }


class CreateScheduleStaffForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date', "class": "form-control"}),
            'id_staff': forms.Select(attrs={"class": "form-select"}),
            'start_time': forms.TimeInput(format="%H:%M", attrs={"class": "form-control"}),
            'end_time': forms.TimeInput(format="%H:%M", attrs={"class": "form-control"})
        }
