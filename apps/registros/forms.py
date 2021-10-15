from django.forms import ModelForm
from apps.funcionarios.models import Funcionario
from apps.registros.models import Registro


class RegistroForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa
        )

    class Meta:
        model = Registro
        fields = ['motivo', 'funcionario', 'horas']

