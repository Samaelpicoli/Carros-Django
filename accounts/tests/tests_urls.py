from django.test import TestCase
from django.urls import resolve, reverse

from accounts import views


class TestUrlsCar(TestCase):
    def test_url_login_possui_a_url_correta(self):
        """
        Verifica se a URL de login é a correta.
        """
        esperado = '/login/'
        resultado = reverse('login')
        self.assertEqual(esperado, resultado)

    def test_url_login_retorna_a_view_login(self):
        """
        Verifica se a URL de login resolve para a view correta.
        """
        esperado = views.login_view
        resultado = resolve(reverse('login'))
        self.assertIs(esperado, resultado.func)

    def test_url_register_possui_a_url_correta(self):
        """Verifica se a URL de registro é a correta."""
        esperado = '/register/'
        resultado = reverse('register')
        self.assertEqual(esperado, resultado)

    def test_url_register_retorna_a_view_register(self):
        """Verifica se a URL de registro resolve para a view correta."""
        esperado = views.register_view
        resultado = resolve(reverse('register'))
        self.assertIs(esperado, resultado.func)

    def test_url_logout_possui_a_url_correta(self):
        """Verifica se a URL de logout é a correta."""
        esperado = '/logout/'
        resultado = reverse('logout')
        self.assertEqual(esperado, resultado)

    def test_url_logout_retorna_a_view_logout(self):
        """Verifica se a URL de logout resolve para a view correta."""
        esperado = views.logout_view
        resultado = resolve(reverse('logout'))
        self.assertIs(esperado, resultado.func)
