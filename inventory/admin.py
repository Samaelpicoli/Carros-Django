from django.contrib import admin

from inventory.models import CarInventory

"""
Registra o modelo CarInventory na interface de administração do Django.

Esta configuração permite que o modelo CarInventory seja gerenciado
facilmente através do painel de administração, proporcionando uma
interface para criar, editar e deletar instâncias do modelo.
"""

admin.site.register(CarInventory)
