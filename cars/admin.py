from django.contrib import admin

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    """
    Configuração do painel de administração para o modelo Car.

    list_display: Define os campos exibidos na listagem de carros no admin.
    search_fields: Permite busca pelos campos especificados.
    """

    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


admin.site.register(Car, CarAdmin)
