from django import forms
from .models import *


class CoreForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('phone_number',  'phone_code', 'name')