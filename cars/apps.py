from django.apps import AppConfig


class CarsConfig(AppConfig):
    """
    Configuração do aplicativo Django 'cars'.

    default_auto_field: Define o tipo padrão de campo automático para IDs.
    name: Nome do aplicativo Django.
    ready: Importa os sinais (signals) quando o aplicativo estiver pronto.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self):
        """Importa os signals do aplicativo quando ele estiver pronto."""
        import cars.signals  # noqa
