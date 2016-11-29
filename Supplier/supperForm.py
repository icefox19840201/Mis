from django import forms
from django.forms import ModelForm
from models import Supplier
class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        exclude={'id',}
