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
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    if cars_value is None:
        cars_value = 0.0
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        text = client.get_car_ai_bio(
            instance.model, instance.brand, instance.factory_year
        )
        instance.bio = text
