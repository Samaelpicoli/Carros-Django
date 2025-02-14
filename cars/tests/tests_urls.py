from django.test import TestCase
from django.urls import resolve, reverse

from cars import views


class TestUrlsCar(TestCase):
    def test_url_car_list_possui_a_url_correta(self):
        esperado = '/cars/'
        resultado = reverse('car_list')
        self.assertEqual(esperado, resultado)

    def test_url_car_list_retorna_a_view_car_list(self):
        esperado = views.CarsListView
        resultado = resolve(reverse('car_list'))
        self.assertIs(esperado, resultado.func.view_class)

    def test_url_new_car_possui_a_url_correta(self):
        esperado = '/cars/new-car/'
        resultado = reverse('new_car')
        self.assertEqual(esperado, resultado)

    def test_url_new_car_list_retorna_a_view_create_car(self):
        esperado = views.CreateCarView
        resultado = resolve(reverse('new_car'))
        self.assertIs(esperado, resultado.func.view_class)
