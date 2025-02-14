from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from brands.models import Brand
from cars.models import Car


class TestUpdateCarView(TestCase):
    """Testa a view de atualização de um carro."""

    def setUp(self):
        """Configura os dados iniciais para os testes."""
        self.brand = Brand.objects.create(name='Toyota')
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.client.login(username='testuser', password='12345')
        self.car = Car.objects.create(
            model='Corolla',
            brand=self.brand,
            factory_year=2020,
            model_year=2021,
            plate='AAA1234',
            value=50000,
        )

    def test_update_view_a_ser_acessada_retorna_status_code_200(self):
        """
        Verifica se a página de atualização do carro pode ser
        acessada e retorna status HTTP 200.
        """
        esperado_status_code = HTTPStatus.OK
        response = self.client.get(reverse('car_update', args=[self.car.id]))
        self.assertEqual(response.status_code, esperado_status_code)

    def test_update_view_template_utilizado_retorna_car_update_html(self):
        """
        Verifica se a view de atualização do carro utiliza o template correto.
        """
        esperado_nome_template = 'car_update.html'

        response = self.client.get(reverse('car_update', args=[self.car.id]))
        self.assertTemplateUsed(response, esperado_nome_template)

    def test_update_view_atualiza_carro_valido(self):
        """
        Testa se a atualização de um carro válido ocorre corretamente
        e redireciona para a página de detalhes.
        """
        response = self.client.post(
            reverse('car_update', args=[self.car.id]),
            data={
                'model': 'Corolla XRS',
                'brand': self.brand.id,
                'factory_year': 2020,
                'model_year': 2021,
                'plate': 'BBB5678',
                'value': 60000,
            },
        )
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, 'Corolla XRS')
        self.assertEqual(self.car.plate, 'BBB5678')
        self.assertEqual(self.car.value, 60000)
        self.assertRedirects(
            response, reverse('car_detail', args=[self.car.id])
        )

    def test_update_view_sem_login_retorna_redirecionameto_a_url_login(self):
        """
        Verifica se usuários não autenticados são redirecionados
        para a página de login ao tentar acessar a view.
        """
        esperado_status_code = HTTPStatus.FOUND
        self.client.logout()
        response = self.client.post(reverse('car_update', args=[self.car.id]))
        self.assertEqual(response.status_code, esperado_status_code)
        self.assertTrue(response.url.startswith('/login/'))

    def test_update_car_view_carro_inexistente_retorna_not_found(self):
        """
        Verifica se a tentativa de atualizar um carro
        inexistente retorna um status HTTP 404 (Not Found).
        """
        esperado_status_code = HTTPStatus.NOT_FOUND
        response = self.client.post(reverse('car_update', args=[9999]))
        self.assertEqual(response.status_code, esperado_status_code)
