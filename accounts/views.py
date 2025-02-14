from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def register_view(request):
    """
    Exibe e processa o formulário de registro de usuário.

    Quando o método da requisição é POST, a função tenta salvar um novo
    usuário com os dados fornecidos. Se a criação do usuário for
    bem-sucedida, o usuário é redirecionado para a página de login.

    Se o método não for POST ou se o formulário não for válido,
    a função renderiza o template de registro, exibindo o formulário
    atual para que o usuário possa corrigir quaisquer erros.
    """
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    """
    Exibe e processa o formulário de login de usuário.

    Quando o método da requisição é POST, a função tenta autenticar
    o usuário com as credenciais fornecidas. Se a autenticação for
    bem-sucedida, o usuário é redirecionado para a lista de carros.

    Se a autenticação falhar ou se o método não for POST,
    a função renderiza o template de login, exibindo o formulário
    de autenticação para que o usuário possa tentar novamente.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('car_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    """
    Realiza o logout do usuário e redireciona para a lista de carros.

    Esta função encerra a sessão do usuário autenticado e, em seguida,
    redireciona para a lista de carros, permitindo que o usuário
    inicie uma nova sessão ou explore outras partes da aplicação.
    """
    logout(request)
    return redirect('car_list')
