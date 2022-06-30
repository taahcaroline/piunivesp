
from django.db import models
from django.contrib.auth import get_user_model

# Formulário de cadastro de fornecedor
class Fornecedores(models.Model):
    forn = models.CharField('Fornecedor', max_length=500)

    def __str__(self):
        return self.forn

# Formulário de cadastro de produto
class Nomeproduto(models.Model):
    numero = models.CharField('Número da Nota Fiscal',  max_length=10)
    nameproduto = models.CharField('Produto', max_length=200)
    quantidade = models.CharField('Quantidade',  max_length=10)
    marca = models.CharField('Marca do produto', max_length=10)
    garantia = models.CharField('Garantia', max_length=10)


    def __str__(self):
        return self.nameproduto

# Formulário de cadastro de nota fiscal

class Produto(models.Model):
    data = models.DateField('Data de aquisição')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    numero = models.CharField('Número da Nota Fiscal',  max_length=10)
    valornota = models.DecimalField('Valor total da nota', max_digits=10, decimal_places=2, default=0.00)
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
ESTADO_CHOICES = (
    ('Não realizado', 'Não realizado'),
    ('Concluído', 'Concluído')
)
class Servicos(models.Model):
   cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
   servico = models.TextField('Serviço a ser executado', max_length=300)
   valor = models.DecimalField('Valor total do orçamento', max_digits=10, decimal_places=2, default=0.00)
   data = models.DateTimeField()
   estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='Não realizado')
 
   def __str__(self):
        return self.servico

# Formulário de tomada de decisão
class Gestao(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    politicas = models.TextField('Atualização', max_length=300)

    def __str__(self):
        return self.titulo