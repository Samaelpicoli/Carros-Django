from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestLoginAndLogoutViews(TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste criando um usuário de teste.
        Um usuário com o nome de usuário 'testuser' e senha
        'testpassword123' é criado para ser utilizado nos testes
        de login e logout.
        """
        User.objects.create_user(
            username='testuser', password='testpassword123'
        )

    def test_login_view_retorna_status_code_200(self):
        """
        Verifica se a view de login retorna o status code 200
        ao acessar a página.
        Este teste verifica se a requisição GET para a URL de login
        é bem-sucedida e retorna o código de status HTTP 200,
        indicando que a página foi carregada corretamente.
        """
        esperado = HTTPStatus.OK
        response = self.client.get(reverse('login'))
        resultado = response.status_code
        self.assertEqual(esperado, resultado)

    def test_login_view_template_utilizado_retorna_login_html(self):
        """
        Confirma que a view de login utiliza o template 'login.html'.
        Este teste garante que a resposta da view de login
        renderiza o template correto, que deve ser 'login.html'.
        """
        esperado = 'login.html'
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, esperado)

    def test_login_view_valid(self):
        """
        Verifica se um login válido redireciona para a lista de carros.
        Este teste simula um login bem-sucedido usando as credenciais
        do usuário de teste. Espera-se que a resposta tenha o código
        de status HTTP 302 (FOUND) e que o usuário seja redirecionado
        para a página da lista de carros. Também verifica se o
        usuário existe no banco de dados.
        """
        esperado = HTTPStatus.FOUND
        response = self.client.post(
            reverse('login'),
            data={
                'username': 'testuser',
                'password': 'testpassword123',
            },
        )
        self.assertEqual(response.status_code, esperado)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertRedirects(response, reverse('car_list'))

    def test_login_view_invalid(self):
        """
        Verifica se um login inválido retorna o status code 200
        e exibe erros de validação.
        Este teste simula uma tentativa de login com uma senha incorreta.
        Espera-se que a resposta tenha o código de status HTTP 200,
        indicando que a página foi carregada novamente, e que o
        formulário de login contenha erros de validação.
        """
        esperado = HTTPStatus.OK
        response = self.client.post(
            reverse('login'),
            data={
                'username': 'testuser',
                'password': 'wrongpassword',
            },
        )
        self.assertEqual(response.status_code, esperado)
        self.assertIn('login_form', response.context)
        self.assertFalse(response.context['login_form'].is_valid())

    def test_logout_view(self):
        """
        Verifica se o logout do usuário redireciona corretamente
        para a lista de carros.
        Este teste simula o logout do usuário de teste. Espera-se que
        a resposta tenha o código de status HTTP 302 e que o usuário
        seja redirecionado para a página da lista de carros após o logout.
        """
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('car_list'))


class TestRegisterView(TestCase):
    def test_register_view_retorna_status_code_200(self):
        """
        Verifica se a view de registro retorna o status code 200
        ao acessar a página.
        Este teste verifica se a requisição GET para a URL de registro
        é bem-sucedida e retorna o código de status HTTP 200,
        indicando que a página foi carregada corretamente.
        """
        esperado = HTTPStatus.OK
        response = self.client.get(reverse('register'))
        resultado = response.status_code
        self.assertEqual(esperado, resultado)

    def test_register_view_template_utilizado_retorna_register_html(self):
        """
        Confirma que a view de registro utiliza o template 'register.html'.
        Este teste garante que a resposta da view de registro
        renderiza o template correto, que deve ser 'register.html'.
        """
        esperado = 'register.html'
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, esperado)

    def test_register_view_valid(self):
        """
        Verifica se um registro válido cria um novo usuário
        e redireciona para a página de login.
        Este teste simula um registro bem-sucedido com um novo usuário.
        Espera-se que a resposta tenha o código de status HTTP 302 (FOUND),
        indicando um redirecionamento para a página de login, e que o
        usuário seja criado no banco de dados.
        """
        esperado = HTTPStatus.FOUND
        response = self.client.post(
            reverse('register'),
            data={
                'username': 'testuser',
                'password1': 'testpassword123',
                'password2': 'testpassword123',
            },
        )
        self.assertEqual(response.status_code, esperado)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertRedirects(response, reverse('login'))

    def test_register_view_invalid(self):
        """
        Verifica se um registro inválido retorna o status code 200
        e exibe erros de validação.
        Este teste simula uma tentativa de registro com senhas que não
        coincidem. Espera-se que a resposta tenha o código de status HTTP
        200, indicando que a página foi carregada novamente, e que o
        formulário de registro contenha erros de validação.
        """
        response = self.client.post(
            reverse('register'),
            data={
                'username': 'testuser',
                'password1': 'testpassword123',
                'password2': 'differentpassword',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_form', response.context)
        self.assertFalse(response.context['user_form'].is_valid())
