from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.departamento.models import Departamento


class DepartamentoApiView(APIView):

    def get(self, request):
        departamento = [Departamento.name for Departamento in Departamento.objects.all()]
        return Response(status=status.HTTP_200_OK, data=departamento)

    def post(self, request):
        Departamento.objects.create(
            name=request.data['name'],
            short_name=request.data['short_name'],
            annulate=request.data['annulate'],)
        return self.get(request)


