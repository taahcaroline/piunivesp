from django.urls import path
from computacao2 import views


urlpatterns = [
    path('', views.home, name='meuapp-home'),
    path('sobre/', views.sobre, name='sobre'),
    path('vagascad/', views.vagascad, name='vagascad'),
    path('demandas/', views.vagas, name='demandas'),
    path('demandas/<int:id>', views.vagasview, name='demandasview'),
    # path('editarvaga/<int:id>/', views.editvagas, name='editarvaga'),
    # path('deletarvaga/<int:cadastrovagas_pk>/', views.vagasdelete, name='deletarvaga'),
    path('busca/', views.busca, name='busca'),
    # path('resultados/', resultados, name='resultados'),

    # path('clientescadastrados/', views.listaclientes, name='clientes'),
    # path('deletarcliente/<int:pk>/', views.deleteclientes, name='deletarcliente'),

    
]
