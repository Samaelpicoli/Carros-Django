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
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__istartswith=search)
        return cars


class CreateCarView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class DetailCarView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class UpdateCarView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class DeleteCarView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

    def get_queryset(self):
        return Car.objects.all()
