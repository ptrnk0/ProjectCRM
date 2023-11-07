from django import forms
from serviceapp import models

class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = '__all__'


class ResourceForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = '__all__'