from django.db.models import Sum
from django.db.models.signals import (
    post_delete,
    post_save,
    pre_save,
)
from django.dispatch import receiver

from cars.models import Car
from gemini_api import client
from inventory.models import CarInventory


def car_inventory_update():
    """
    Atualiza o inventário de carros com a quantidade total
    de carros e o valor total dos veículos cadastrados.

    - Conta o número total de carros na base de dados.
    - Calcula a soma do valor de todos os carros.
    - Se o valor total for None (nenhum carro cadastrado com valor),
    define como 0.0.
    - Cria um novo registro no modelo CarInventory com os dados atualizados.
    """
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    if cars_value is None:
        cars_value = 0.0
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    """
    Signal executado após salvar um objeto Car.

    - Atualiza o inventário de carros chamando `car_inventory_update`.
    """
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    """
    Signal executado após a exclusão de um objeto Car.

    - Atualiza o inventário de carros chamando `car_inventory_update`.
    """
    car_inventory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Signal executado antes de salvar um objeto Car.

    - Se a biografia (`bio`) do carro estiver vazia, gera automaticamente
    uma descrição com base no modelo, marca e ano de fabricação do carro
    usando um cliente de IA.
    """
    if not instance.bio:
        text = client.get_car_ai_bio(
            instance.model, instance.brand, instance.factory_year
        )
        instance.bio = text
