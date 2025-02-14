"""
Gerador de SECRET_KEY para o Django.
Assim como outras informações como o server run do Django
e configurações do banco de dados.
Além de infos sensíveis utilizadas pelo projeto.
"""

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = (
    """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost
API_KEY_GEMINI=CHAVE_DE_API_DO_GEMINI_AQUI
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
""".strip()
    % get_random_string(50, chars)
)

# Escreve o arquivo de configuração em '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
