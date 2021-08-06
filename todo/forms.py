from django import forms
from .models import Tarea

class FormTarea(forms.ModelForm):
    class Meta:
        model=Tarea
        fields=['tarea']