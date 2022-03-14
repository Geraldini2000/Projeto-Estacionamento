from django.forms import ModelForm

from .models import Pessoa, Veiculo


# Form puxando o banco de dados Pessoa
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa  # Puxando o nome do modelo do banco
        fields = '__all__'  # Selecionando todos os campos do modelo Pessoa

# Form puxando o banco de dados Pessoa


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo  # Puxando o nome do modelo do banco
        fields = '__all__'  # Selecionando todos os campos do modelo Veiculo
