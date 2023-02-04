from rest_framework import serializers

from desafio_muralis.funcionario.models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
