from django.db import models


class FuncionarioFabrica(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField("Nome", max_length=150)
    rg = models.CharField("RG", max_length=150, null=True, blank=True)
    cpf = models.CharField("CPF", max_length=150, null=True, blank=True)
    data_admissao = models.DateField("Data de admissão", auto_now=True, editable=True, null=True, blank=True)
    data_hora_alteracao_do_registro = models.DateTimeField("Data e hora da alteração do registro", auto_now=True,
                                                           editable=True, null=True, blank=True)
    cep = models.CharField("CEP", max_length=50, null=True, blank=True)
    endereco = models.CharField("Endereço", max_length=250, null=True, blank=True)
    bairro = models.CharField("Bairro", max_length=250, null=True, blank=True)
    cidade = models.CharField("Cidade", max_length=250, null=True, blank=True)

    def __str__(self):
        return str(f'{self.nome} ({self.id})')
