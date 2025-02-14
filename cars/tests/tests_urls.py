from django.test import TestCase
from django.urls import resolve, reverse

from cars import views


class TestUrlsCar(TestCase):
    def test_url_car_list_possui_a_url_correta(self):
        """
        Testa se a URL para a página de listagem de carros está correta.
        """
        esperado = '/cars/'
        resultado = reverse('car_list')
        self.assertEqual(esperado, resultado)

    def test_url_car_list_retorna_a_view_car_list(self):
        """
        Testa se a URL de Listagem de carros retorna
        a view correta (CarsListView).
        """
        esperado = views.CarsListView
        resultado = resolve(reverse('car_list'))
        self.assertIs(esperado, resultado.func.view_class)

    def test_url_new_car_possui_a_url_correta(self):
        """
        Testa se a URL para a página de cadastro de carro está correta.
        """
        esperado = '/cars/new-car/'
        resultado = reverse('new_car')
        self.assertEqual(esperado, resultado)

    def test_url_new_car_list_retorna_a_view_create_car(self):
        """
        Testa se a URL de cadastro de carro retorna
        a view correta (CreateCarView).
        """
        esperado = views.CreateCarView
        resultado = resolve(reverse('new_car'))
        self.assertIs(esperado, resultado.func.view_class)

    def test_url_car_detail_possui_a_url_correta(self):
        """
        Testa se a URL para a página de detalhes do carro está correta.
        """
        esperado = '/cars/detail/1/'
        resultado = reverse('car_detail', kwargs={'pk': 1})
        self.assertEqual(esperado, resultado)

    def test_url_car_detail_retorna_a_view_detail_car(self):
        """
        Testa se a URL de detalhes retorna a view correta (DetailCarView).
        """
        esperado = views.DetailCarView
        resultado = resolve(reverse('car_detail', kwargs={'pk': 1}))
        self.assertIs(esperado, resultado.func.view_class)

    def test_url_car_update_possui_a_url_correta(self):
        """
        Testa se a URL para a página de atualização do carro está correta.
        """
        esperado = '/cars/update/1/'
        resultado = reverse('car_update', kwargs={'pk': 1})
        self.assertEqual(esperado, resultado)

    def test_url_car_update_retorna_a_view_update_car(self):
        """
        Testa se a URL de atualização do carro retorna
        a view correta (UpdateCarView).
        """
        esperado = views.UpdateCarView
        resultado = resolve(reverse('car_update', kwargs={'pk': 1}))
        self.assertIs(esperado, resultado.func.view_class)

    def test_url_car_delete_possui_a_url_correta(self):
        """Testa se a URL para a página de exclusão do carro está correta."""
        esperado = '/cars/delete/1/'
        resultado = reverse('car_delete', kwargs={'pk': 1})
        self.assertEqual(esperado, resultado)

    def test_url_car_delete_retorna_a_view_delete_car(self):
        """
        Testa se a URL de exclusão do carro retorna a view
        correta (DeleteCarView).
        """
        esperado = views.DeleteCarView
        resultado = resolve(reverse('car_delete', kwargs={'pk': 1}))
        self.assertIs(esperado, resultado.func.view_class)
