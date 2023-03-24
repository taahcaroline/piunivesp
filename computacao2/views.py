# Createfrom django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



from .models import Cadastrovagas
from .forms import CadastrovagasForm
from django.db.models import Q



from django.shortcuts import render, get_object_or_404



def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')




# cadastro vagas
@login_required 
def vagascad(request):
    if request.method == 'POST':
            form = CadastrovagasForm(request.POST)
            if form.is_valid():
             servicos = form.save(commit=False)
             servicos.user = request.user
             servicos.save()

            return redirect('demandas')
    else:        
        form = CadastrovagasForm()
        return render(request, 'cadservico.html', {'form': form})


#lista de vagas

def vagas(request):
    vagas = Cadastrovagas.objects.all()
   
    context = {
        'vagas': vagas
    }

    return render(request, 'servicoscadastrados.html',  context)

def vagasview(request, id):
    cadastrovagas = get_object_or_404(Cadastrovagas, pk=id)
    return render(request, 'demandas.html', {'cadastrovagas': cadastrovagas} )


# @login_required 
# #editar demandas
# @login_required 
# def editvagas(request, id):
#     vagas = get_object_or_404(Cadastrovagas, pk=id)
#     form = CadastrovagasForm(instance=vagas)
    
#     if(request.method == 'POST'):
#         form = CadastrovagasForm(request.POST, instance=vagas)
#         if (form.is_valid()):
#             vagas.save()
#             return redirect('demandas')
#         else:
#             return render(request, 'editarservico.html', {'form': form, 'vagas': vagas})
#     else: 
#         return render(request, 'editarservico.html', {'form': form, 'vagas': vagas})

            
# # deletar demandas
# @login_required 
# def vagasdelete(request, cadastrovagas_pk):
#     vagas = Cadastrovagas.objects.get(pk=cadastrovagas_pk)
#     vagas.delete()

#     return redirect('demandas')





# #lista de produtos
# @login_required 
# def listaprodutos(request):
#     produtos = Nomeproduto.objects.all()
#     # paginator = Paginator(serv, 3)
#     # page = request.GET.get('page')
#     # listademanda = paginator.get_page(page)
#     context = {
#         'produtos': produtos
#     }

#     return render(request, 'produtoscadastrados.html',  context)



# busca
def busca(request):
    query = request.GET.get('q')
    results = Cadastrovagas.objects.filter(cargo__icontains=query)
    return render(request, 'resultado.html', {'results': results})
   