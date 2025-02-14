from django.apps import AppConfig


class BrandsConfig(AppConfig):
    """
    Configuração do aplicativo Brands.
    Esta classe contém as configurações do aplicativo 'brands',
    incluindo o campo padrão para a criação de IDs de modelo.
    Ela é utilizada pelo Django para configurar o aplicativo
    durante a inicialização do projeto.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brands'
