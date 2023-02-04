import requests
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from desafio_muralis.funcionario.models import Funcionario
from desafio_muralis.funcionario_fabrica.models import FuncionarioFabrica


class Command(BaseCommand):
    help = 'Atualizar tabela de funcionario_fabrica da database db02 com as informações de funcionario da database db01'

    def get_funcionario(self, funcionario_id: int):
        try:
            funcionario = Funcionario.objects.using('db01').get(id=funcionario_id)
        except Funcionario.DoesNotExist:
            raise CommandError(f'Funcionario {funcionario_id} não existe')
        return funcionario

    def consultar_cep(self, cep: str):
        request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if request.status_code == 200:
            return None if request.json().get('erro') else request.json()
        else:
            return None

    def handle(self, *args, **options):
        for funcionario_fabrica in FuncionarioFabrica.objects.using('db02').all():
            funcionario = self.get_funcionario(funcionario_fabrica.id)
            funcionario_fabrica.rg = funcionario.rg
            funcionario_fabrica.cpf = funcionario.cpf
            funcionario_fabrica.data_hora_alteracao_do_registro = timezone.now()
            funcionario_fabrica.cep = funcionario.cep
            consulta_cep = self.consultar_cep(funcionario_fabrica.cep)
            if consulta_cep:
                funcionario_fabrica.endereco = f"{consulta_cep['logradouro']}, {consulta_cep['complemento']}"
                funcionario_fabrica.bairro = f"{consulta_cep['bairro']}"
                funcionario_fabrica.cidade = f"{consulta_cep['localidade']}"
            funcionario_fabrica.save()
        self.stdout.write(self.style.SUCCESS("Tabela 'funcionario_fabrica' da database db02 atualizada com sucesso!"))
