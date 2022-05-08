from django import forms
from .models import Fornecedores, Produto, Cliente, Servicos


class FornecedoresForm(forms.ModelForm):
    class Meta:
     model = Fornecedores
     fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
     model = Produto
     fields = 'title', 'data', 'fornecedor', 'numero', 'quantidade', 'marca', 'garantia'

class ClienteForm(forms.ModelForm):
    class Meta:
     model = Cliente
     fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta:
     model = Servicos
     fields = '__all__'
