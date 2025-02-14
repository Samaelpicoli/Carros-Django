from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuração da aplicação 'accounts'.

    Esta classe é responsável por configurar os
    parâmetros da aplicação de contas no Django.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
