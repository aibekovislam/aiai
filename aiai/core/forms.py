from django import forms
from .models import *


class CoreForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('phoneNumber',  'phoneCode', 'name', 'cityAddress')