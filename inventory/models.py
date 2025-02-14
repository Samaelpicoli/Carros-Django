from django.db import models


# Create your models here.
class CarInventory(models.Model):
    """
    Modelo que representa o inventário de carros.
    Este modelo armazena informações sobre a contagem e o valor
    dos carros disponíveis. Ele inclui um campo para a contagem
    de carros, o valor total dos carros e a data de criação do registro.

    cars_count (IntegerField): Número de carros no inventário.
    cars_value (FloatField): Valor total dos carros no inventário.
    created_at (DateTimeField): Data e hora em que o registro foi criado.
    """

    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Define a ordem padrão dos registros como decrescente,
        com base na data de criação.
        """

        ordering = ['-created_at']

    def __str__(self) -> str:
        """
        Este método exibe a contagem e o valor total dos carros
        no formato 'contagem - valor'.

        Returns:
            str: Retorna uma representação em string
            do inventário de carros.
        """
        return f'{self.cars_count} - {self.cars_value}'
