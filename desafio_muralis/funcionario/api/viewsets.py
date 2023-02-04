from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from desafio_muralis.funcionario.api.serializers import FuncionarioSerializer
from desafio_muralis.funcionario.models import Funcionario


class FuncionarioAPI(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    http_method_names = ['post', 'get', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    docs = {
        "post": {
            "operation_summary": "Adicionar funcionário",
            "operation_description": "Adicionar um novo funcionário"
        },
        "get": {
            "operation_summary": "Listar funcionários",
            "operation_description": "Listagem de funcionários"
        },
        "patch": {
            "operation_summary": "Alterar parcialmente funcionário",
            "operation_description": "Alterar parcialmente um funcionário"
        },
        "put": {
            "operation_summary": "Alterar funcionário",
            "operation_description": "Alterar funcionário"
        },
        "delete": {
            "operation_summary": "Deletar funcionário",
            "operation_description": "Deletar funcionário"
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
