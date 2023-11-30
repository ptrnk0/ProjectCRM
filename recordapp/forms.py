from django import forms
from django.core.exceptions import ValidationError

from recordapp.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', "class": "form-control"}),
            'id_client': forms.Select(attrs={"class": "form-select"}),
            'id_staff': forms.Select(attrs={"class": "form-select"}),
            'id_service': forms.Select(attrs={"class": "form-select"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'duration': forms.NumberInput(attrs={"class": "form-control"})
        }

    def clean(self):
        super().clean()
        dates_from_bd = self.instance.objects.filter(date=self.data.get('date'))
        if dates_from_bd:
            for obj in dates_from_bd:
                if obj['time'] < self.data.get('time') < obj['time'] + obj['duration']:
                    raise ValidationError
