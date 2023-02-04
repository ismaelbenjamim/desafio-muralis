<div align="center">
  <h1>Desafio Muralis</h1>
</div>

<br />

Descrição

- [Introdução](#introducao)
- [Instalação](#instalacao)
- [APIs](#apis)

### Introdução

Esse projeto tem como objetivo realizar um desafio em python e para o desenvolvimento foi utilizado o framework django.

### Instalação

1. Realizar o download do repositório
```shell
git clone https://github.com/ismaelbenjamim/desafio-muralis
```

2. Abrir o diretório do projeto
```shell
cd desafio-muralis/
```

3. Iniciar uma virtualenv
```shell
python -m venv venv
```

4. Executar a virtualenv
```shell
source venv/bin/activate
```

5. Realizar o download das dependências do projeto
```shell
pip install -r requirements.txt 
```

6. Executar as migrações do projeto, gerando os bancos no formato ".sqlite3"
```shell
python manage.py migrate
python manage.py migrate --database=db01 funcionario
python manage.py migrate --database=db02 funcionario_fabrica
```

7. Criar um super usuário para acessar o painel de administrador (http://127.0.0.1:8000/admin) e consumir as APIs com utilização do token
```shell
python manage.py createsuperuser
```

8. Carregar funcionários do BD01 para a tabela funcionarios_fabrica do BD02
```shell
python manage.py update_funcionarios_fabrica
```

9. Executar o projeto
```shell
python manage.py runserver
```

10. Para acessar a documentação das APIs (redoc e swagger):
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/swagger/
```

11. Exemplo de curl para obter o token de autenticação nas APIs
```
curl -X POST "http://127.0.0.1:8000/api/token/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: FnR7VaZfB7cxaESaennWUA8rLThWzXL4y3vcy5dEwX3pcNrN2Bse81T0aai2R9Bf" -d "{  \"username\": \"root\",  \"password\": \"root\"}"
```

### APIs

TOKEN (POST)
```
http://127.0.0.1:8000/api/token/
```

Funcionário (GET, POST, PUT, PATCH, DELETE)
```
http://127.0.0.1:8000/api/funcionario/
```

Funcionário de Fábrica (GET, POST, PUT, PATCH, DELETE)
```
http://127.0.0.1:8000/api/funcionario-fabrica/
```