from django import forms
from clientapp import models

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'


# class ClientForm(forms.Form):
#     first_name = forms.CharField(max_length=200, required=False)
#     last_name = forms.CharField(max_length=200)
#     phone = forms.CharField(max_length=200)