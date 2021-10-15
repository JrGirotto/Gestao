from django.urls import path
from .views import RegistrosList, RegistroCreate, RegistroEdit, RegistroDelete


urlpatterns = [
    path('', RegistrosList.as_view(), name='list_registros'),
    path('criar/', RegistroCreate.as_view(), name='create_registro'),
    path('editar/<int:pk>/', RegistroEdit.as_view(), name='update_registro'),
    path('apagar/<int:pk>/', RegistroDelete.as_view(), name='delete_registro'),
]