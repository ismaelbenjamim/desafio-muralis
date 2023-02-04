from rest_framework import serializers

from desafio_muralis.funcionario_fabrica.models import FuncionarioFabrica


class FuncionarioFabricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioFabrica
        fields = '__all__'
