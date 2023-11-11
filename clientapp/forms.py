from django import forms
from clientapp import models

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.Textarea(attrs={"cols": 30, "rows": 3, "class": "form-control"}),
            'birthday': forms.DateTimeInput(attrs={'type': 'date', "class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'image': forms.FileInput(attrs={"class": "form-control"}),
        }


# class ClientForm(forms.Form):
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     phone = forms.CharField(max_length=200)
#     email = forms.EmailField(required=False)
#     birthday = forms.DateField(widget=forms.DateInput, required=False)
#     comment = forms.CharField(widget=forms.Textarea, required=False)

#     birthday.widget.attrs.update(format="%m/%d/%Y")
#     comment.widget.attrs.update(size="10")