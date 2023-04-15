
from django.db import models
from django.contrib.auth import get_user_model



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



