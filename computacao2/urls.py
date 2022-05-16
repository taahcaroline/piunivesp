from django.urls import path
from computacao2 import views


urlpatterns = [
    path('', views.home, name='meuapp-home'),
    path('sobre/', views.sobre, name='sobre'),
    path('nomeproduto/', views.produtotitle, name='nomeproduto'),
    path('produtocad/', views.produtocad, name='produtocad'),
    path('fornecedorcad/', views.fornecedorcad, name='fornecedorcad'),
    path('clientecad/', views.clientecad, name='clientecad'),
    path('servicocad/', views.servicocad, name='servicocad'),
    path('meusfornecedores/', views.meusfornecedores, name='meusfornecedores'),
]