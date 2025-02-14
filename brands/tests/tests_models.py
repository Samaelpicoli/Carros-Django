from django.test import TestCase

from brands.models import Brand


class TestModelBrand(TestCase):
    """
    Teste do modelo Brand.
    Esta classe contém os testes para verificar o comportamento do
    modelo Brand, incluindo a representação em string do objeto.
    """

    def setUp(self):
        """
        Configura o ambiente de teste criando uma instância de Brand.
        Este método é chamado antes da execução de cada teste,
        garantindo que uma marca chamada 'Toyota' esteja disponível
        para os testes.
        """
        self.brand = Brand.objects.create(name='Toyota')

    def test_str_de_brand_deve_retornar_seu_nome(self):
        """
        Verifica se a representação em string de Brand retorna seu nome.
        Este teste assegura que o método __str__ do modelo Brand
        retorna o nome da marca corretamente.
        """
        esperado = 'Toyota'
        resultado = str(self.brand)
        self.assertEqual(esperado, resultado)
