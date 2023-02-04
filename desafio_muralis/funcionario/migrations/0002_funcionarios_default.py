from django.db import migrations


class Migration(migrations.Migration):

    def load_initial_data(apps, schema_editor):
        data = [
            {
                "id": 1,
                "nome": "João Henrique da Silva",
                "rg": "46.383.212-7",
                "cpf": "612.196.640-81",
                "cep": "56909-661"
            },
            {
                "id": 2,
                "nome": "Mateus Silva dos Santos",
                "rg": "27.703.751-7",
                "cpf": "979.809.560-01",
                "cep": "65610-970"
            },
            {
                "id": 3,
                "nome": "Tiago Bello de Oliveira",
                "rg": "27.172.818-8",
                "cpf": "959.877.140-79",
                "cep": "79930-970"
            },
            {
                "id": 4,
                "nome": "Barbara Vaz Santos",
                "rg": "21.115.369-2",
                "cpf": "808.796.800-08",
                "cep": "79785-971"
            },
            {
                "id": 5,
                "nome": "Mariana Borba Ferreira",
                "rg": "48.500.525-6",
                "cpf": "903.784.510-06",
                "cep": "49700-974"
            },
            {
                "id": 6,
                "nome": "Felipe Leandro Barreto",
                "rg": "52.210.598-2",
                "cpf": "103.254.320-07",
                "cep": "42570-324"
            },
            {
                "id": 7,
                "nome": "Dante Santana da Silva",
                "rg": "18.590.158-4",
                "cpf": "204.614.381-32",
                "cep": "52610-604"
            },
            {
                "id": 8,
                "nome": "Liliane Wanderley de Souza",
                "rg": "78.120.624-1",
                "cpf": "102.234.511-22",
                "cep": "61870-124"
            },
            {
                "id": 9,
                "nome": "Murilo Calebe Pereira",
                "rg": "48.995.412-1",
                "cpf": "244.312.534-32",
                "cep": "68810-970"
            },
            {
                "id": 10,
                "nome": "Fátima Bianca Moura",
                "rg": "49.871.511-5",
                "cpf": "213.514.704-42",
                "cep": "68810-970"
            }
        ]
        funcionario_model = apps.get_model('funcionario', 'Funcionario')
        for obj in data:
            funcionario_model.objects.create(**obj)

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
