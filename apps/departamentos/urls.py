from django.urls import path
from .views import DepartamentoCreate, DepartamentoEdit, DepartamentoList, DepartamentoDelete

urlpatterns = [
    path('list', DepartamentoList.as_view(), name='list_departamentos'),
    path('criar', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name='update_departamento'),
    path('apagar/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
]
