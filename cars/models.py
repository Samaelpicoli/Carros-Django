from django.db import models

from brands.models import Brand


class Car(models.Model):
    """
    Modelo que representa um carro no sistema.

    Atributos:
    - id (AutoField): Identificador único do carro.
    - model (CharField): Nome ou modelo do carro.
    - brand (ForeignKey de Brand): Marca do carro (relacionamento com Brand).
    - factory_year (IntegerField): Ano de fabricação do carro (opcional).
    - model_year (IntegerField): Ano do modelo do carro (opcional).
    - plate (CharField): Placa do carro (opcional).
    - value (FloatField): Valor do carro (opcional).
    - photo (ImageField): Imagem do carro (opcional).
    - bio (TextField): Descrição adicional do carro (opcional).
    """

    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand'
    )
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        """
        Representação de Carro no modelo Car.

        Returns:
            str: Representação em string do modelo Car.
        """
        return f'{self.model}'
