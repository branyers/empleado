from rest_framework import serializers
from  applications.persona.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'FirstName', 'LastName', 'Jobs', 'full_name', 'departament', 'avatar', 'habilidades', 'resume',)
        # fields = ['FirstName , LastName, Jobs, departament, habilidades']

