import imp
from django import forms 
from CRUDoperation.models import *

class Engforms(forms.ModelForm):
    class Meta:
        model = Engineers
        fields="__all__"

class EngLPForms(forms.ModelForm):
    class Meta:
        model = EngineerLearningPaths
        fields = "__all__"

class EngLPStepForms(forms.ModelForm):
    class Meta:
        model = Learningpathsteps
        fields = "__all__"