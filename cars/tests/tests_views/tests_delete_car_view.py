from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from brands.models import Brand
from cars.models import Car


class TestDeleteCarView(TestCase):
    def setUp(self):
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

    def test_delete_view_a_ser_acessada_retorna_status_code_200(self):
        esperado_status_code = HTTPStatus.OK

        response = self.client.get(reverse('car_delete', args=[self.car.id]))

        self.assertEqual(response.status_code, esperado_status_code)

    def test_delete_view_template_utilizado_retorna_car_delete_html(self):
        esperado_nome_template = 'car_delete.html'

        response = self.client.get(reverse('car_delete', args=[self.car.id]))

        self.assertTemplateUsed(response, esperado_nome_template)

    def test_delete_view_deleta_carro_retorna_zero_objects_e_direciona(self):
        esperado_quantidade_carros = 0

        response = self.client.post(reverse('car_delete', args=[self.car.id]))

        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)
        self.assertRedirects(response, reverse('car_list'))

    def test_delete_view_sem_login_retorna_redirecionameto_a_url_login(self):
        esperado_status_code = HTTPStatus.FOUND

        self.client.logout()
        response = self.client.post(reverse('car_delete', args=[self.car.id]))

        self.assertEqual(response.status_code, esperado_status_code)
        self.assertTrue(response.url.startswith('/login/'))

    def test_delete_car_view_carro_inexistente_retorna_not_found(self):
        esperado_status_code = HTTPStatus.NOT_FOUND

        response = self.client.post(reverse('car_delete', args=[9999]))

        self.assertEqual(response.status_code, esperado_status_code)
