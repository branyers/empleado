from rest_framework import serializers
from applications.departamento.models import Departamento


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'name', 'short_name', 'annulate',)
