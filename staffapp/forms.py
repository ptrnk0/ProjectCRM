from django import forms
from .models import Staff, Schedule


class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class CreateScheduleStaffForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(format="%H:%M")
        }
