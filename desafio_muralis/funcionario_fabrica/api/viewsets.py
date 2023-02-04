from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from desafio_muralis.funcionario_fabrica.api.serializers import FuncionarioFabricaSerializer
from desafio_muralis.funcionario_fabrica.models import FuncionarioFabrica


class FuncionarioFabricaAPI(viewsets.ModelViewSet):
    queryset = FuncionarioFabrica.objects.all()
    serializer_class = FuncionarioFabricaSerializer
    http_method_names = ['post', 'get', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    docs = {
        "post": {
            "operation_summary": "Adicionar funcionário da fábrica",
            "operation_description": "Adicionar um novo funcionário da fábrica"
        },
        "get": {
            "operation_summary": "Listar funcionários da fábrica",
            "operation_description": "Listagem de funcionários da fábrica"
        },
        "patch": {
            "operation_summary": "Alterar parcialmente funcionário da fábrica",
            "operation_description": "Alterar parcialmente um funcionário da fábrica"
        },
        "put": {
            "operation_summary": "Alterar funcionário da fábrica",
            "operation_description": "Alterar funcionário da fábrica"
        },
        "delete": {
            "operation_summary": "Deletar funcionário da fábrica",
            "operation_description": "Deletar funcionário da fábrica"
        },
    }

    @swagger_auto_schema(**docs["post"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(**docs["get"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(**docs["put"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(**docs["patch"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**docs["delete"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

