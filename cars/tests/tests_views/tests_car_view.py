from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from brands.models import Brand
from cars.models import Car


class TestCarView(TestCase):
    """Testes para a View de Listagem de Carros."""

    def setUp(self):
        """
        Configura o ambiente de teste com a criação de 2 marcas de carro.
        """
        self.ford = Brand.objects.create(name='Ford')
        self.chevrolet = Brand.objects.create(name='Chevrolet')

    def test_car_view_retorna_status_code_200(self):
        """
        Testa se a visualização da lista de carros retorna
        um código de status 200 (OK).
        """
        esperado = HTTPStatus.OK
        response = self.client.get(reverse('car_list'))
        resultado = response.status_code
        self.assertEqual(esperado, resultado)

    def test_car_view_template_utilizado_retorna_cars_html(self):
        """
        Testa se a visualização da lista de carros utiliza o
        template correto ('cars.html').
        """
        esperado = 'cars.html'
        response = self.client.get(reverse('car_list'))
        self.assertTemplateUsed(response, esperado)

    def test_car_view_retorna_nenhum_carro_encontrado(self):
        """
        Testa se, quando não há carros no banco de dados,
        a mensagem 'Nenhum carro encontrado.' é exibida.
        """
        esperado = 'Nenhum carro encontrado.'
        response = self.client.get(reverse('car_list'))
        self.assertContains(response, esperado)

    def test_car_view_retorna_context_com_filtro_no_search(self):
        """
        Testa se o filtro de busca funciona corretamente.
        Quando o filtro de busca é aplicado, apenas os carros
        que correspondem ao termo de pesquisa devem ser retornados.
        """
        Car.objects.create(
            brand=self.ford,
            model='Mustang',
            factory_year=2020,
            model_year=2020,
            plate='AAA3333',
            value=30000,
        )
        Car.objects.create(
            brand=self.chevrolet,
            model='Camaro',
            factory_year=2021,
            model_year=2020,
            plate='AAA4444',
            value=40000,
        )
        response = self.client.get(reverse('car_list'), {'search': 'Mustang'})
        self.assertContains(response, 'Mustang')
        self.assertNotContains(response, 'Camaro')

    def test_car_view_retorna_context_e_quantidade_de_itens(self):
        """
        Testa se o contexto da view contém a lista de carros
        e verifica a quantidade de carros retornados.
        """
        Car.objects.create(
            brand=self.ford,
            model='Mustang',
            factory_year=2020,
            model_year=2020,
            plate='AAA3333',
            value=30000,
        )
        response = self.client.get(reverse('car_list'))
        chave_esperada_no_context = 'cars'
        self.assertIn(chave_esperada_no_context, response.context)

        esperado_quantidade_itens = 1

        self.assertEqual(
            len(response.context['cars']), esperado_quantidade_itens
        )

    def tearDown(self):
        """Limpa os dados criados no banco de dados após cada teste."""
        Car.objects.all().delete()
        Brand.objects.all().delete()
