
from django.db import models
from django.contrib.auth import get_user_model

# # Formulário de cadastro de fornecedor
# class Fornecedores(models.Model):
#     forn = models.CharField('Fornecedor', max_length=500)

#     def __str__(self):
#         return self.forn

# Formulário de cadastro de vagas


MODELO_CHOICES = (
    ('Home Office', 'Home Office'),
    ('Hibrido', 'Híbrido'),
    ('Presencial', 'Presencial'),
)


ESCOLARIDADE_CHOICES = (
    ('Ensino Fundamental Incompleto', 'Ensino Fundamental Incompleto'),
    ('Ensino Fundamental Completo', 'Ensino Fundamental Completo'),
    ('Ensino Médio Completo', 'Ensino Médio Completo'),
    ('Ensino Superior Incompleto', 'Ensino Superior Incompleto'),
    ('Ensino Superior completo', 'Ensino Superior completo'),
)
class Cadastrovagas(models.Model):
    cargo = models.CharField('Cargo', max_length=200)
    empresa = models.CharField('Empresa', max_length=200)
    descricao = models.TextField('Descrição', max_length=500)
    vagas = models.CharField('Quantidade de vagas',  max_length=10)
    escolaridade = models.CharField('Escolaridade',  choices=ESCOLARIDADE_CHOICES, default='Ensino Médio Completo', max_length=30)
    salario = models.DecimalField('Salário', max_digits=10, decimal_places=2, default=0.00)
    modelo = models.CharField('Modelo de trabalho', choices=MODELO_CHOICES, default='Presencial', max_length=11)
    localizacao = models.CharField('Localização', max_length=30)
    horassemanais = models.CharField('Horas semanais', max_length=6)
    


    def __str__(self):
        return self.cargo

""" # Formulário de cadastro de nota fiscal

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
        return self.titulo """