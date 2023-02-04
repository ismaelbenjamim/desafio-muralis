from django.db import migrations


class Migration(migrations.Migration):

    def load_initial_data(apps, schema_editor):
        data = [
            {
                "id": 1,
                "nome": "João Henrique da Silva"
            },
            {
                "id": 2,
                "nome": "Mateus Silva dos Santos"
            },
            {
                "id": 3,
                "nome": "Tiago Bello de Oliveira"
            },
            {
                "id": 4,
                "nome": "Barbara Vaz Santos"
            },
            {
                "id": 5,
                "nome": "Mariana Borba Ferreira"
            },
            {
                "id": 6,
                "nome": "Felipe Leandro Barreto"
            },
            {
                "id": 7,
                "nome": "Dante Santana da Silva"
            },
            {
                "id": 8,
                "nome": "Liliane Wanderley de Souza"
            },
            {
                "id": 9,
                "nome": "Murilo Calebe Pereira"
            },
            {
                "id": 10,
                "nome": "Fátima Bianca Moura"
            }
        ]
        funcionario_model = apps.get_model('funcionario_fabrica', 'FuncionarioFabrica')
        for obj in data:
            funcionario_model.objects.create(**obj)

    dependencies = [
        ('funcionario_fabrica', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
