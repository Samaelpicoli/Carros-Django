from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from brands.models import Brand
from cars.models import Car


class TestCarView(TestCase):
    def setUp(self):
        self.ford = Brand.objects.create(name='Ford')
        self.chevrolet = Brand.objects.create(name='Chevrolet')

    def test_car_view_retorna_status_code_200(self):
        esperado = HTTPStatus.OK
        response = self.client.get(reverse('car_list'))
        resultado = response.status_code
        self.assertEqual(esperado, resultado)

    def test_car_view_template_utilizado_retorna_cars_html(self):
        esperado = 'cars.html'
        response = self.client.get(reverse('car_list'))
        self.assertTemplateUsed(response, esperado)

    def test_car_view_retorna_nenhum_carro_encontrado(self):
        esperado = 'Nenhum carro encontrado.'
        response = self.client.get(reverse('car_list'))
        self.assertContains(response, esperado)

    def test_car_view_retorna_context_com_filtro_no_search(self):
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
        Car.objects.all().delete()
        Brand.objects.all().delete()
