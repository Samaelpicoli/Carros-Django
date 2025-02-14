from datetime import datetime

from django import forms

from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_factory_year(self):
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
        value = self.cleaned_data.get('value')
        if value < 1000:
            self.add_error(
                'value', 'Valor mínimo de veículo deve ser de R$ 1.000,00'
            )
        return value
