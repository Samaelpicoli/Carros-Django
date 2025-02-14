from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from brands.models import Brand
from cars.models import Car


class TestDeleteCarView(TestCase):
    """Testes para a View de Exclusão de Carros."""

    def setUp(self):
        """
        Configura o ambiente de teste com um usuário, uma marca
        de carro (Toyota), e um carro (Corolla). Além disso,
        realiza o login do usuário para testes de exclusão.
        """
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
        """
        Testa se a página de exclusão de um carro retorna o código de
        status 200 (OK) quando acessada por GET.
        """
        esperado_status_code = HTTPStatus.OK
        response = self.client.get(reverse('car_delete', args=[self.car.id]))
        self.assertEqual(response.status_code, esperado_status_code)

    def test_delete_view_template_utilizado_retorna_car_delete_html(self):
        """
        Testa se a página de exclusão utiliza o template
        correto ('car_delete.html').
        """
        esperado_nome_template = 'car_delete.html'
        response = self.client.get(reverse('car_delete', args=[self.car.id]))
        self.assertTemplateUsed(response, esperado_nome_template)

    def test_delete_view_deleta_carro_retorna_zero_objects_e_direciona(self):
        """
        Testa se o carro é deletado corretamente após o envio do POST para
        a view de exclusão. Verifica também se o número de carros no
        banco de dados é 0 após a exclusão e se ocorre um redirecionamento
        para a página de lista de carros.
        """
        esperado_quantidade_carros = 0
        response = self.client.post(reverse('car_delete', args=[self.car.id]))
        self.assertEqual(Car.objects.count(), esperado_quantidade_carros)
        self.assertRedirects(response, reverse('car_list'))

    def test_delete_view_sem_login_retorna_redirecionameto_a_url_login(self):
        """
        Testa se um usuário não autenticado é redirecionado para a página de
        login quando tenta acessar a view de exclusão de carro.
        """
        esperado_status_code = HTTPStatus.FOUND
        self.client.logout()
        response = self.client.post(reverse('car_delete', args=[self.car.id]))
        self.assertEqual(response.status_code, esperado_status_code)
        self.assertTrue(response.url.startswith('/login/'))

    def test_delete_car_view_carro_inexistente_retorna_not_found(self):
        """
        Testa se a tentativa de exclusão de um carro que não existe
        retorna o código de status 404 (Not Found).
        """
        esperado_status_code = HTTPStatus.NOT_FOUND
        response = self.client.post(reverse('car_delete', args=[9999]))
        self.assertEqual(response.status_code, esperado_status_code)
