
from django.urls import path

from .views import (home, list_mensalista, list_mov_mensalista,
                    list_movrotativos, lista_pessoas, lista_veiculos,
                    mensalista_novo, movmensalista_novo, movrotativos_novo,
                    pessoa_novo, pessoa_update, veiculo_novo)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoa/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<int:id>/', pessoa_update,
         name='core_update'),


    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo/', veiculo_novo, name='core_veiculo_novo'),

    path('mov-rot/', list_movrotativos, name='core_list_movrotativos'),
    path('rot-rot-novo/', movrotativos_novo, name='core_movrotativos_novo'),

    path('mensalistas/', list_mensalista, name='core_list_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),

    path('mov_mensal/', list_mov_mensalista, name='core_list_mov_mensalista'),
    path('mov_mensal_novo/', movmensalista_novo,
         name='core_movmensalista_novo'),
]
