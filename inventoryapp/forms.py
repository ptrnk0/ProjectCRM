from django import forms
from inventoryapp import models

class ComodityForm(forms.ModelForm):
    class Meta:
        model = models.Commodity
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'