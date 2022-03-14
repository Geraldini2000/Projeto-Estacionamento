
from django.urls import path

from .views import (home, list_mensalista, list_mov_mensalista,
                    list_movrotativos, lista_pessoas, lista_veiculos)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoa/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', list_movrotativos, name='core_list_movrotativos'),
    path('mensalistas/', list_mensalista, name='core_list_mensalista'),
    path('mov_mensal/', list_mov_mensalista, name='core_list_mov_mensalista'),
]
