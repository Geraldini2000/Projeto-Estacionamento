from django.forms import ModelForm

from .models import Mensalista, MovMensalista, MovRotativo, Pessoa, Veiculo


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


class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class MovMensalsitaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
