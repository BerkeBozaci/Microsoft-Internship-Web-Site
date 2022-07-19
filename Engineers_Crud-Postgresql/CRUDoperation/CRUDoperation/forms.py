from django import forms 
from CRUDoperation.models import engineers

class Engforms(forms.ModelForm):
    class Meta:
        model = engineers
        fields="__all__"