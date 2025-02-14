from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from cars.forms import CarModelForm
from cars.models import Car


class CarsListView(ListView):
    """
    Exibe a lista de carros disponíveis.

    - Usa a template 'cars.html'.
    - Define 'cars' como o nome do contexto para acesso na template.
    - Ordena os carros por modelo.
    - Permite busca filtrando modelos que começam com a
    string informada no parâmetro 'search'.
    """

    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        """
        Retorna a queryset dos carros ordenada por modelo,
        aplicando filtro de busca se o parâmetro 'search' for informado.
        """
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__istartswith=search)
        return cars


class CreateCarView(LoginRequiredMixin, CreateView):
    """
    Permite a criação de um novo carro.

    - Apenas usuários autenticados podem acessar.
    - Usa a template 'new_car.html'.
    - Utiliza o formulário CarModelForm.
    - Redireciona para a lista de carros após o cadastro.
    """

    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class DetailCarView(DetailView):
    """
    Exibe os detalhes de um carro específico.

    - Usa a template 'car_detail.html'.
    """

    model = Car
    template_name = 'car_detail.html'


class UpdateCarView(LoginRequiredMixin, UpdateView):
    """
    Permite a edição de um carro existente.

    - Apenas usuários autenticados podem acessar.
    - Usa a template 'car_update.html'.
    - Utiliza o formulário CarModelForm.
    - Após a edição, redireciona para a página de detalhes do carro.
    """

    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        """Redireciona para a página de detalhes do carro atualizado."""
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class DeleteCarView(LoginRequiredMixin, DeleteView):
    """
    Permite a exclusão de um carro.

    - Apenas usuários autenticados podem acessar.
    - Usa a template 'car_delete.html'.
    - Após a exclusão, redireciona para a lista de carros.
    """

    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    def get_queryset(self):
        """
        Retorna a queryset de todos os carros disponíveis para exclusão.
        """
        return Car.objects.all()
