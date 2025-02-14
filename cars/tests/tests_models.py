from django.test import TestCase

from brands.models import Brand
from cars.models import Car


class TestModelCar(TestCase):
    """Realiza os testes no modelo Car e seus métodos."""

    def setUp(self):
        """
        Configuração inicial dos testes, cria uma marca e um carro
        para realizaçaõ dos testes.
        """
        self.brand = Brand.objects.create(name='Toyota')
        self.car = Car.objects.create(
            model='Corolla',
            brand=self.brand,
            factory_year=2011,
            model_year=2012,
            plate='EZA9D19',
            value=52500.00,
        )

    def test_str_de_carro_deve_retornar_seu_modelo(self):
        """
        Testa se a string retornada pelo modelo
        CarInventory é no formato esperado.
        """
        esperado = 'Corolla'
        resultado = str(self.car)
        self.assertEqual(esperado, resultado)
