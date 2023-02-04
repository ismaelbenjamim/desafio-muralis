from django.db import models
from django.utils import timezone


class Funcionario(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField("Nome", max_length=150)
    rg = models.CharField("RG", max_length=150)
    cpf = models.CharField("CPF", max_length=150)
    data_admissao = models.DateField("Data de admissão", auto_now=True, editable=True)
    data_hora_alteracao_do_registro = models.DateTimeField("Data e hora da alteração do registro", auto_now=True,
                                                           editable=True)
    cep = models.CharField("CEP", max_length=50)

    def __str__(self):
        return str(f'{self.nome} ({self.cpf})')
