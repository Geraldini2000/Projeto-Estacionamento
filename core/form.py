from django.forms import ModelForm

from .models import Pessoa


# Form puxando o banco de dados Pessoa
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa  # Puxabdo o nome do modelo do banco
        fields = '__all__'  # Selecionando todos os campos do modelo Pessoa
