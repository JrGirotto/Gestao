from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Registro(models.Model):
    motivo = models.CharField(max_length=100, help_text='Motivo da Hora Extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('update_registro', args=[self.id])

    def __str__(self):
        return self.motivo
