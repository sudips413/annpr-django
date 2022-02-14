from django import forms
from .models import MediaFiles, NumberPlate

class ModelForm1(forms.ModelForm):
    class Meta:
        model= NumberPlate
        fields =['number']
class ModelForm2(forms.ModelForm):
    class Meta:
        model= MediaFiles
        fields =['img','videofile']        