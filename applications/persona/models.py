from django.db import models
from applications.departamento.models import Departamento
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Habilidades(models.Model):
    Habilidades = models.CharField('Habilidades', max_length=50)

    class Meta:
        verbose_name ='Habilidades'
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return f"{self.Habilidades}"


class Persona(models.Model):

    JOBS_CHOICES = (
        ("0", "COUNTER"),
        ("1", "ADMINISTRATOR"),
        ("2", "Economist"),
        ("3", "Others"),
    )

    FirstName = models.CharField("Name", max_length=50)
    LastName = models.CharField("Last Name", max_length=50)
    Jobs = models.CharField("Jobs", choices=JOBS_CHOICES, max_length=1)
    departament = models.ForeignKey(Departamento, related_name='Departamento', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='Empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    resume = RichTextField(null=False)

    class Meta:
        verbose_name='Persona'
        verbose_name_plural = 'Persona'
        ordering = ('-FirstName',)
        unique_together = ('FirstName', 'LastName')

    def __str__(self):
        return f"{self.FirstName} {self.LastName} {self.departament}"




