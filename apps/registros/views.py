from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .forms import RegistroForm
from .models import Registro


class RegistrosList(ListView):
    model = Registro

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Registro.objects.filter(funcionario__empresa=empresa_logada)


class RegistroCreate(CreateView):
    model = Registro
    form_class = RegistroForm

    def get_form_kwargs(self):
        kwargs = super(RegistroCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegistroEdit(UpdateView):
    model = Registro
    form_class = RegistroForm

    def get_form_kwargs(self):
        kwargs = super(RegistroEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegistroDelete(DeleteView):
    model = Registro
    success_url = reverse_lazy('list_registros')
