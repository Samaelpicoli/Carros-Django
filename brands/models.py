from django.db import models


class Brand(models.Model):
    """
    Modelo que representa uma marca.
    Este modelo armazena informações sobre marcas, incluindo um
    identificador único e o nome da marca. Ele é utilizado para
    gerenciar e organizar as marcas no sistema.

    id: AutoField - Identificador único da marca, gerado automaticamente.
    name: CharField - Nome da marca, com no máximo 200 caracteres
    e deve ser único no banco de dados.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        """
        Este método é utilizado para exibir o nome da marca
        quando o objeto é impresso ou exibido em uma interface.

        Returns:
            str: Representação em string da marca.
        """
        return f'{self.name}'
