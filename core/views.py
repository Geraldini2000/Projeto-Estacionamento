
from django.shortcuts import render

from .models import Mensalista, MovMensalista, MovRotativo, Pessoa, Veiculo


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context=context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/listas_pessoas.html', {'pessoa': pessoas})


def lista_veiculos(request):
    veiculo = Veiculo.objects.all()
    return render(request, 'core/listas_veiculos.html', {'veiculos': veiculo})


def list_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    return render(request, 'core/list_movrotativos.html', {'mov_rot': mov_rot})


def list_mensalista(request):
    mensalist = Mensalista.objects.all()
    return render(
        request, 'core/list_mensalistas.html', {'mensalist': mensalist})


def list_mov_mensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    return render(request, 'core/list_movmensalistas.html',
                  {'mov_mensalistas': mov_mensalistas})
