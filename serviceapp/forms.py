from django import forms
from serviceapp import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"})
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control"}),
        }


# class AddResourceForServiceForm(forms.ModelForm):
#     class Meta:
#         model = models.Service
#         fields = '__all__'
#
#         widgets = {
#             'name': forms.Select(attrs={"class": "form-control"}),
#             'resources': forms.SelectMultiple(attrs={"class": "form-select"}),
#         }


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, resource):
        return '%s' % resource.name



class AddResourceForServiceForm(forms.Form):
    resource = CustomMMCF(
        queryset=models.Resource.objects.all(),
        widget=forms.Select
    )
