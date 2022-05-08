
from django.db import models
from django.contrib.auth import get_user_model

# Formulário de cadastro de fornecedor
class Fornecedores(models.Model):
    forn = models.CharField('Fornecedor', max_length=500)

    def __str__(self):
        return self.forn

# Formulário de cadastro de produto

class Produto(models.Model):
    title = models.CharField('Produto', max_length=50)
    data = models.DateField('Data de aquisição')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    numero = models.CharField('Número da Nota Fiscal',  max_length=10)
    quantidade = models.CharField('Quantidade',  max_length=10)
    marca = models.CharField('Marca do produto', max_length=10)
    garantia = models.CharField(max_length=10)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title

# Formulário de cadastro de clientes

class Cliente(models.Model):
   nome = models.CharField('Nome', max_length=100)
   endereco = models.CharField('Logradouro', max_length=100)
   numero = models.CharField('Número', max_length=6)
   bairro = models.CharField('Bairro', max_length=100)
   cidade = models.CharField('Cidade', max_length=30)

   def __str__(self):
        return self.nome


# Formulário de cadastro de serviços
class Servicos(models.Model):
   cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
   servico = models.CharField('Serviço a ser executado', max_length=100)
   data = models.DateTimeField()
 
