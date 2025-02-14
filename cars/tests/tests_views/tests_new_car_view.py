from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from brands.models import Brand
from cars.models import Car


class TestNewCarView(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Toyota')
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.client.login(username='testuser', password='12345')

    def test_create_view_a_ser_acessado_retorna_status_code_200(self):
        esperado = HTTPStatus.OK

        response = self.client.get(reverse('new_car'))

        self.assertEqual(response.status_code, esperado)

    def test_create_view_template_utilizado_retorna_new_car_html(self):
        esperado = 'new_car.html'

        response = self.client.get(reverse('new_car'))

        self.assertTemplateUsed(response, esperado)

    def test_create_view_valido_cadastra_carro_e_retorna_qtd_carros_e_redirecionamento(  # noqa: E501
        self,
    ):  # noqa: E501
        esperado_status_code = HTTPStatus.FOUND
        esperado_quantidade_carros = 1
        esperado_redirect = 'car_list'

        response = self.client.post(
            reverse('new_car'),
            data={
                'model': 'Corolla',
                'brand': self.brand.id,
                'factory_year': 2011,
                'model_year': 2012,
                'plate': 'EZA9D19',
                'value': 52500.00,
            },
        )

        self.assertEqual(response.status_code, esperado_status_code)
        self.assertTrue(Car.objects.filter(model='Corolla').exists())
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)
        self.assertRedirects(response, reverse(esperado_redirect))

    def test_create_view_invalido_retorna_invalido_e_zero_carros(self):
        esperado_status_code = HTTPStatus.OK
        esperado_template_utilizado = 'new_car.html'
        esperado_quantidade_carros = 0

        response = self.client.post(
            reverse('new_car'),
            data={
                'brand': self.brand.id,
                'factory_year': 2011,
                'model_year': 2012,
                'value': 52500.00,
            },
        )
        self.assertEqual(response.status_code, esperado_status_code)
        self.assertTemplateUsed(response, esperado_template_utilizado)
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)

    def test_create_view_dados_nulos_retorna_invalido_e_zero_carros(self):
        esperado_status_code = HTTPStatus.OK
        esperado_template_utilizado = 'new_car.html'
        esperado_quantidade_carros = 0

        response = self.client.post(
            reverse('new_car'),
            data={
                'model': '',
                'brand': '',
                'factory_year': 2011,
                'model_year': 2012,
                'value': 52500.00,
            },
        )

        self.assertEqual(response.status_code, esperado_status_code)
        self.assertTemplateUsed(response, esperado_template_utilizado)
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)

    def test_create_view_com_factory_year_antes_de_1950_retorna_invalido_e_msg_de_erro(  # noqa: E501
        self,
    ):  # noqa: E501
        esperado_texto = (
            'Não é possível cadastrar carros fabricados antes de 1950'
        )
        esperado_quantidade_carros = 0

        response = self.client.post(
            reverse('new_car'),
            data={
                'model': 'Old Timer',
                'brand': self.brand.id,
                'factory_year': 1940,
                'model_year': 1940,
                'plate': 'AAA1234',
                'value': 5000,
            },
        )

        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('factory_year', response.context['form'].errors)
        self.assertIn('model_year', response.context['form'].errors)
        self.assertContains(response, esperado_texto)
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)

    def test_create_view_com_factory_year_afrente_de_ano_atual_retorna_invalido_e_msg_de_erro(  # noqa: E501
        self,
    ):
        esperado_status_code = HTTPStatus.OK
        esperado_texto = 'Não é possível cadastrar carros do futuro'
        esperado_quantidade_carros = 0

        response = self.client.post(
            reverse('new_car'),
            data={
                'model': 'Corolla GRX',
                'brand': self.brand.id,
                'factory_year': 2100,
                'model_year': 2100,
                'plate': 'AAA1234',
                'value': 5000,
            },
        )

        self.assertEqual(response.status_code, esperado_status_code)
        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('factory_year', response.context['form'].errors)
        self.assertIn('model_year', response.context['form'].errors)
        self.assertContains(response, esperado_texto)
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)

    def test_create_view_com_valor_menor_que_1000_retorna_invalido_e_msg_de_erro(  # noqa: E501
        self,
    ):  # noqa: E501
        esperado_status_code = HTTPStatus.OK
        esperado_texto = 'Valor mínimo de veículo deve ser de R$ 1.000,00'
        esperado_quantidade_carros = 0

        response = self.client.post(
            reverse('new_car'),
            data={
                'model': 'Corolla',
                'brand': self.brand.id,
                'factory_year': 1980,
                'model_year': 1980,
                'plate': 'AAA1234',
                'value': 600.59,
            },
        )

        self.assertEqual(response.status_code, esperado_status_code)
        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('value', response.context['form'].errors)
        self.assertContains(
            response,
            esperado_texto,
        )
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)

    def test_create_view_sem_login_redireciona_para_url_de_login(self):
        esperado = HTTPStatus.FOUND

        self.client.logout()
        response = self.client.post(
            reverse('new_car'),
            data={
                'model': 'Corolla GRX',
                'brand': self.brand.id,
                'factory_year': 2100,
                'model_year': 2100,
                'plate': 'AAA1234',
                'value': 5000,
            },
        )

        self.assertEqual(response.status_code, esperado)
        self.assertTrue(response.url.startswith('/login/'))
