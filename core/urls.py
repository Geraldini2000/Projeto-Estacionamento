
from django.urls import path

from .views import (home, list_mensalista, list_mov_mensalista,
                    list_movrotativos, lista_pessoas, lista_veiculos,
                    mensalista_novo, mensalista_update, movmensalista_novo,
                    movmensalista_update, movrotativos_novo,
                    movrotativos_update, pessoa_novo, pessoa_update,
                    veiculo_novo, veiculo_update)

urlpatterns = [
    path('', home, name='core_home'),

    # Pessoa
    path('pessoa/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<int:id>/', pessoa_update,
         name='core_pessoa_update'),

    # Veiculo
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo_update/<int:id>/', veiculo_update,
         name='core_veiculo_update'),

    # Movimento Rotativo
    path('mov-rot/', list_movrotativos, name='core_list_movrotativos'),
    path('rot-rot-novo/', movrotativos_novo, name='core_movrotativos_novo'),
    path('mov-rot-update/<int:id>/', movrotativos_update,
         name='core_movrotativos_update'),

    # Mensalistas
    path('mensalistas/', list_mensalista, name='core_list_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>/', mensalista_update,
         name='core_mensalista_update'),

    # Movimento mensalista
    path('mov_mensal/', list_mov_mensalista, name='core_list_mov_mensalista'),
    path('mov_mensal_novo/', movmensalista_novo,
         name='core_movmensalista_novo'),
    path('mov-mensal-update/<int:id>/', movmensalista_update,
         name='core_movmensalista_update'),
]
