from django.test import TestCase

from brands.models import Brand
from cars.forms import CarModelForm


class TestFormsCar(TestCase):
    """Testes para validação do formulário de carros (CarModelForm)"""

    def setUp(self):
        """Configuração inicial para criação de uma marca de carro."""
        self.brand = Brand.objects.create(name='Toyota')

    def test_car_form_retorna_valido(self):
        """
        Testa se o formulário é válido quando todos os campos
        obrigatórios são preenchidos corretamente.
        """
        form = CarModelForm(
            data={
                'model': 'Corolla',
                'brand': self.brand,
                'factory_year': 2011,
                'model_year': 2012,
                'plate': 'EZA9D19',
                'value': 52500.00,
            }
        )
        self.assertTrue(form.is_valid())

    def test_car_form_retorna_invalido(self):
        """
        Testa se o formulário retorna inválido quando o
        campo 'model' não é preenchido.
        """
        form = CarModelForm(
            data={
                'brand': self.brand,
                'factory_year': 2011,
                'model_year': 2012,
                'value': 52500.00,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('model', form.errors)

    def test_car_form_ano_fabricacao_e_modelo_menor_que_1950_retorna_invalido(  # noqa: E501
        self,
    ):
        """
        Testa se o formulário retorna inválido para carros
        fabricados antes de 1950.
        """
        form = CarModelForm(
            data={
                'model': 'Toyota AA',
                'brand': self.brand,
                'factory_year': 1936,
                'model_year': 1936,
                'plate': 'aaa1234',
                'value': 2500,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('factory_year', form.errors)
        self.assertIn('model_year', form.errors)

    def test_car_form_ano_fabricacao_e_modelo_maior_que_ano_atual_retorna_invalido(  # noqa: E501
        self,
    ):
        """
        Testa se o formulário retorna inválido para carros
        fabricados no futuro.
        """
        form = CarModelForm(
            data={
                'model': 'Toyota SUPRA',
                'brand': self.brand,
                'factory_year': 2030,
                'model_year': 2030,
                'plate': 'aaa1234',
                'value': 1000000,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('factory_year', form.errors)
        self.assertIn('model_year', form.errors)

    def test_car_form_valor_menor_que_1000_reais_retorna_invalido(self):
        """
        Testa se o formulário retorna inválido quando o valor
        do carro é menor que R$ 1.000,00.
        """
        form = CarModelForm(
            data={
                'model': 'Bandeirante',
                'brand': self.brand,
                'factory_year': 1971,
                'model_year': 1971,
                'plate': 'aaa1234',
                'value': 500,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('value', form.errors)
