from django import forms
from .models import Persona


class EmpleadosForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = (
            'FirstName',
            'LastName',
            'Jobs',
            'departament',
            'avatar',
            'habilidades',
        )

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }