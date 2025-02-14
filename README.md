# Projeto Carros - Django

# Sobre o projeto

Projeto para apredizado utilizando Django.

É uma aplicação Web, que apresenta uma listagem de carros, e possibilita visualizar detalhes de cada veículo por parte do usuário, e o administrador poderá cadastrar, editar e excluir carros, o projeto contém proteção de rotas, assim sendo possível acessar rotas de registro de usuários, de login e de logout.

Este projeto aplica integrações com upload de imagens, Classed-Based-Views do Django, Django Signals, realização de testes unitários e textos gerados a partir da integração da API do Google Gemini.


# Tecnologias Utilizadas

* Python
* Django
* HTML
* Gemini AI

## Bibliotecas Utilizadas

Estão listadas no arquivo requirements.txt

# Como executar o projeto
Pré-requisitos: Python 3.11+

```python
# Realizar o clone desse repositório e acessar a pasta onde foi gerado:
git clone https://github.com/Samaelpicoli/Carros-Django.git

# Criar o ambiente virtual:
python -m venv venv | python3 -m venv venv

# Ativar o ambiente virtual:

# Linux:
source venv/bin/activate

# Windows:
.\venv\Scripts\activate

#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt

# executar o código contrib/env_gen.py para geração do arquivo .env:
python contrib/env_gen.py

# Gerar uma chave API no site Google AI for Developers para uso do Gemini e inserir
# no arquivo .env em API_KEY_GEMINI com o token.

# Realizar as migrações
python manage.py migrate

# Criar um superusuário para realizar login
python manage.py createsuperuser

# Executar os testes:
python manage.py test ou coverage run manage.py test

# Visualizar a cobertura de testes:
coverage html

# Executar o sistema:
python manage.py runserver
```

# Autor
Samael Muniz Picoli

