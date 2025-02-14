from django.urls import path

from accounts import views

"""
URLs da aplicação 'accounts'.

Este módulo mapeia as URLs da aplicação de contas
para as respectivas views. As rotas incluem:
- Registro de usuário
- Login de usuário
- Logout de usuário
"""

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
