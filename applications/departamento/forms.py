from django import forms

class DepartamentoFormView(forms.Form):
    JOBS_CHOICES = (
        ("0", "COUNTER"),
        ("1", "ADMINISTRATOR"),
        ("2", "Economist"),
        ("3", "Others"),
    )

    Nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    departamento = forms.CharField(max_length=100)
    short_name = forms.CharField(max_length=100)
    cargos = forms.ChoiceField(choices=JOBS_CHOICES)
