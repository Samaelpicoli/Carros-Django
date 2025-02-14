from datetime import datetime

from django import forms

from cars.models import Car


class CarModelForm(forms.ModelForm):
    """
    Formulário para o modelo Car, com validações personalizadas.

    - clean_factory_year: Garante que o ano de fabricação não seja
    maior que o próximo ano nem menor que 1950.
    - clean_model_year: Garante que o ano do modelo não seja maior
    que o próximo ano nem menor que 1950.
    - clean_value: Garante que o valor do carro seja no mínimo R$ 1.000,00.
    """

    class Meta:
        """
        Modelo que será utilizado no fomrmulário e os campos que serão
        disponibilizados para preenchimento, sendo all, todos os campos
        do modelo Car.
        """

        model = Car
        fields = '__all__'

    def clean_factory_year(self):
        """
        Valida o ano de fabricação do carro.
        O ano de fabricação não pode ser maior que o próximo ano.
        O ano de fabricação não pode ser inferior a 1950.
        """
        factory_year = self.cleaned_data.get('factory_year')
        year = int(datetime.now().year) + 1
        if factory_year > year:
            self.add_error(
                'factory_year', 'Não é possível cadastrar carros do futuro.'
            )
        elif factory_year < 1950:
            self.add_error(
                'factory_year',
                'Não é possível cadastrar carros fabricados antes de 1950',
            )
        return factory_year

    def clean_model_year(self):
        """
        Valida o ano do modelo do carro.
        O ano do modelo não pode ser maior que o próximo ano.
        O ano do modelo não pode ser inferior a 1950.
        """
        model_year = self.cleaned_data.get('model_year')
        year = int(datetime.now().year) + 1
        if model_year > year:
            self.add_error(
                'model_year', 'Não é possível cadastrar carros do futuro.'
            )
        elif model_year < 1950:
            self.add_error(
                'model_year',
                'Não é possível cadastrar carros fabricados antes de 1950',
            )
        return model_year

    def clean_value(self):
        """
        Valida o valor do carro.
        O valor do carro deve ser no mínimo R$ 1.000,00.
        """
        value = self.cleaned_data.get('value')
        if value < 1000:
            self.add_error(
                'value', 'Valor mínimo de veículo deve ser de R$ 1.000,00'
            )
        return value
