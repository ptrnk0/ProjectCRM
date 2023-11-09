from django import forms
from inventoryapp import models

class ComodityForm(forms.ModelForm):
    class Meta:
        model = models.Commodity
        fields = '__all__'


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['discount'].required = False

    class Meta:
        model = models.Order
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }