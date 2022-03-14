
from django.shortcuts import redirect, render

from .form import (MensalistaForm, MovMensalsitaForm, MovRotativoForm,
                   PessoaForm, VeiculoForm)
from .models import Mensalista, MovMensalista, MovRotativo, Pessoa, Veiculo


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context=context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()  # Passando o valor do banco para a var form
    # add o valor das var para outra var
    data = {'pessoa': pessoas, 'form': form}
    return render(request, 'core/listas_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():  # Puxando o valor do form com um if
        form.save()  # Salvando o form
    return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculo = Veiculo.objects.all()
    form = VeiculoForm()  # Recebendo o valor do Form na var
    # Adicionando os valores das vatiaveis para outra var
    data = {'veiculos': veiculo, 'form': form}
    # Retornando o url padrap
    return render(request, 'core/listas_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():  # Puxando o valor do form com um if
        form.save()  # Salvando o form
    # Redirecionando para a url padrao ao salvar os dados
    return redirect('core_lista_veiculos')


def list_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(request, 'core/list_movrotativos.html', data)


def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_movrotativos')


def list_mensalista(request):
    mensalist = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalist': mensalist, 'form': form}
    return render(
        request, 'core/list_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_mensalista')


def list_mov_mensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalsitaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'form': form}
    return render(request, 'core/list_movmensalistas.html', data)


def movmensalista_novo(request):
    form = MovMensalsitaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_mov_mensalista')
