from django.urls import path
from coracao.views import CoracaoCreateView
from coracao.views import CoracaoListaView
from coracao.views import CoracaoEditView
urlpatterns = [
    path("form",CoracaoCreateView.as_view(),name="coracao_create"),
    path("lista", CoracaoListaView.as_view(), name='lista_pacientes'),
    path('editar/<int:id>/', CoracaoEditView.as_view(), name='editar_paciente'),
]
