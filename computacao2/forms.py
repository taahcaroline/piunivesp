from django import forms
from .models import Fornecedores, Nomeproduto, Produto, Cliente, Servicos, Gestao


class FornecedoresForm(forms.ModelForm):
    class Meta:
     model = Fornecedores
     fields = '__all__'

class NomeprodutoForm(forms.ModelForm):
    class Meta:
     model = Nomeproduto
     fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
     model = Produto
     fields = 'item', 'data', 'fornecedor', 'numero', 'quantidade', 'marca', 'garantia', 'valornota'

class ClienteForm(forms.ModelForm):
    class Meta:
     model = Cliente
     fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta:
     model = Servicos
     fields = '__all__'

class GestaoForm(forms.ModelForm):
    class Meta:
     model = Gestao
     fields = '__all__'
