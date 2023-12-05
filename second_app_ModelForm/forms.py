from django import forms
from second_app_ModelForm.models import (SampleModel01, SampleModel02, SampleModel03)

class SampleModel01_Forms(forms.ModelForm):
    class Meta:
        model = SampleModel01
        # fields = '__all__'
        fields = ['id', 'name']
        labels = {
            'id': 'Id',
            'name': 'Name',
        }


class SampleModel02_Forms(forms.ModelForm):
    class Meta:
        model = SampleModel02
        fields = '__all__'

class SampleModel03_Forms(forms.ModelForm):
    class Meta:
        model = SampleModel03
        fields = '__all__'
