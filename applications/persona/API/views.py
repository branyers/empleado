from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from applications.persona.models import Persona
from .Serializer import PersonaSerializer
from .permissions import IsAdminOrReadOnlyPermission


class PersonaModelViewSet(ModelViewSet):
    """Using a ModelViewSet we can create a CRUD API complete, if we want to performance the ModelViewSet we can do
    it """

    permission_classes = [IsAdminOrReadOnlyPermission]
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


"""Class PersonaViewSet"""
# class PersonaApiView(ViewSet):
"""Using a ViewSet to handle the API"""
# """List all persona """
#
# def list(self, request):
#     personas = Persona.objects.all()
#     serializer = PersonaSerializer(personas, many=True)
#     return Response(status=status.HTTP_200_OK, data=serializer.data)
#
# """"Get specific a persona by id"""
#
# def retrieve(self, request, pk: int):
#     persona = Persona.objects.get(pk=pk)
#     serializer = PersonaSerializer(persona)
#     return Response(status=status.HTTP_200_OK, data=serializer.data)
#
# """"Create a new persona"""
#
# def create(self, request):
#     serializer = PersonaSerializer(data=request.POST)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
#     return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


"""Way to get all personas using APIView WITH Serializer"""
"""Using a APIView"""
# def get(self, request):
#     persona = PersonaSerializer(Persona.objects.all(), many=True)
#     return Response(status=status.HTTP_200_OK, data=persona.data)
#
# def post(self, request):
#     persona = PersonaSerializer(data=request.data)
#     if persona.is_valid():
#         persona.save()
#         return Response(status=status.HTTP_201_CREATED, data=persona.data)
#     return Response(status=status.HTTP_400_BAD_REQUEST, data=persona.errors)
