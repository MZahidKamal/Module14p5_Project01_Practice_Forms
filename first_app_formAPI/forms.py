from django import forms
from django.forms.widgets import NumberInput


class SampleForm01(forms.Form):
    name = forms.CharField(max_length=50, label='Full Name')


class SampleForm02(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, max_length=2000, label='Write your comment')


class SampleForm03(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))


class SampleForm04(forms.Form):
    email = forms.EmailField()


class SampleForm05(forms.Form):
    agree = forms.BooleanField()


class SampleForm06(forms.Form):
    date = forms.DateField()


class SampleForm07(forms.Form):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))


YEAR_CHOICES = ['1980', '1981', '1982']
class SampleForm08(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))


class SampleForm09(forms.Form):
    value = forms.DecimalField()


class SampleForm10(forms.Form):
    email = forms.EmailField(required=False)


class SampleForm11(forms.Form):
    message = forms.CharField(min_length=10, max_length=20)

class SampleForm12(forms.Form):
    email = forms.EmailField(label='Enter a valid email address')
