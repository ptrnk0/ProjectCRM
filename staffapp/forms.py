from django import forms
from .models import Staff


class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
