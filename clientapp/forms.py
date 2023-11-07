from django import forms
from clientapp import models

class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'

        widgets = {
            'comment': forms.Textarea(attrs={"cols": 30, "rows": 3}),
            'birthday': forms.NumberInput(attrs={'type': 'date'}),
            
        }

        help_texts = {
            'birthday': ('Enter date in format dd/mm/yy'),
        }

        labels = {
            'phone': ('Phone number'),
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