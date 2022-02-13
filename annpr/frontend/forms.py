from django import forms
from .models import NumberPlate

class ModelForm(forms.ModelForm):
    class Meta:
        model= NumberPlate
        fields =['img','videofile']