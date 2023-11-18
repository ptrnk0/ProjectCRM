from django import forms
from serviceapp import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'id_resource': forms.Select(attrs={"class": "form-select"}),
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control"}),
        }