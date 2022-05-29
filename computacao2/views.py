# Createfrom django.shortcuts import render

# Create your views here.
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from .models import Fornecedores, Cliente, Nomeproduto, Produto, Servicos
from .forms import FornecedoresForm, ProdutoForm, ClienteForm, ServicoForm, NomeprodutoForm



def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')

# cadastro fornecedor
 
@login_required 
def fornecedorcad(request):
    if request.method == 'POST':
            form = FornecedoresForm(request.POST)
            if form.is_valid():
             fornecedores = form.save(commit=False)
             fornecedores.user = request.user
             fornecedores.save()

            return redirect('fornecedorescadastrados.html')
    else:        
        form = FornecedoresForm()
        return render(request, 'cadfornecedores.html', {'form': form})

# cadastro nome do produto
 
@login_required 
def produtotitle(request):
    if request.method == 'POST':
            form = NomeprodutoForm(request.POST)
            if form.is_valid():
             nomeproduto = form.save(commit=False)
             nomeproduto.user = request.user
             nomeproduto.save()

            return redirect('meusprodutos')
    else:        
        form = NomeprodutoForm()
        return render(request, 'cadnomedoproduto.html', {'form': form})

# lista de fornecedores
@login_required 
def meusfornecedores(request):
    fornlist = Fornecedores.objects.all().filter()
    paginator = Paginator(fornlist, 3)
    page = request.GET.get('page')
    listafornecedores = paginator.get_page(page)

    return render(request, 'fornecedorescadastrados.html', {'listafornecedores' : listafornecedores})
# cadastro nota fiscal
@login_required 
def produtocad(request):
    if request.method == 'POST':
            form = ProdutoForm(request.POST)
            if form.is_valid():
             produto = form.save(commit=False)
             produto.user = request.user
             produto.save()

            return redirect('notasfiscais')
    else:        
        form = ProdutoForm()
        return render(request, 'cadproduto.html', {'form': form})

# cadastro cliente
@login_required 
def clientecad(request):
    if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
             cliente = form.save(commit=False)
             cliente.user = request.user
             cliente.save()

            return redirect('clientes')
    else:        
        form = ClienteForm()
        return render(request, 'cadcliente.html', {'form': form})

# cadastro serviço
@login_required 
def servicocad(request):
    if request.method == 'POST':
            form = ServicoForm(request.POST)
            if form.is_valid():
             servicos = form.save(commit=False)
             servicos.user = request.user
             servicos.save()

            return redirect('demandas')
    else:        
        form = ServicoForm()
        return render(request, 'cadservico.html', {'form': form})


#lista de demanda
@login_required 
def demandas(request):
    serv = Servicos.objects.all()
    # paginator = Paginator(serv, 3)
    # page = request.GET.get('page')
    # listademanda = paginator.get_page(page)
    context = {
        'serv': serv
    }

    return render(request, 'servicoscadastrados.html',  context)

def demandasview(request, id):
    servicos = get_object_or_404(Servicos, pk=id)
    return render(request, 'demandas.html', {'servicos': servicos} )


@login_required 
#editar demandas
@login_required 
def editdemandas(request, id):
    servico = get_object_or_404(Servicos, pk=id)
    form = ServicoForm(instance=servico)
    
    if(request.method == 'POST'):
        form = ServicoForm(request.POST, instance=servico)
        if (form.is_valid()):
            servico.save()
            return redirect('demandas')
        else:
            return render(request, 'editarservico.html', {'form': form, 'servico': servico})
    else: 
        return render(request, 'editarservico.html', {'form': form, 'servico': servico})

            
# deletar demandas
@login_required 
def demandasdelete(request, servicos_pk):
    serv = Servicos.objects.get(pk=servicos_pk)
    serv.delete()

    return redirect('demandas')

#lista de clientes
@login_required 
def listaclientes(request):
    clientes = Cliente.objects.all()
    # paginator = Paginator(serv, 3)
    # page = request.GET.get('page')
    # listademanda = paginator.get_page(page)
    context = {
        'clientes': clientes
    }

    return render(request, 'clientescadastrados.html',  context)

# @login_required 
# #editar clientes
# def editclientes(request, cliente_pk):
#     cliente = Cliente.objects.get(pk=cliente_pk)
#     form = ClienteForm(request.POST or None, instance=cliente)
#     if request.POST:
#             if form.is_valid():
#                form.save()
#                return redirect('clientescadastrados')
#     context ={
#         'form': form,
#         'cliente': cliente
#     }
#     return render(request, 'editarcliente.html',  context)
            
# deletar clientes
@login_required 
def deleteclientes(request, pk):
    if request.method == 'POST':
        try:       
             cliente = Cliente.objects.get(id=pk)
             cliente.delete()
        except ObjectDoesNotExist:
            print(f"Record is not found with the id: {pk}")
    return redirect('clientes')



#lista de produtos
@login_required 
def listaprodutos(request):
    produtos = Nomeproduto.objects.all()
    # paginator = Paginator(serv, 3)
    # page = request.GET.get('page')
    # listademanda = paginator.get_page(page)
    context = {
        'produtos': produtos
    }

    return render(request, 'produtoscadastrados.html',  context)

#notas cadastradas
@login_required 
def notascadastradas(request):
    notas = Produto.objects.all()
    # paginator = Paginator(serv, 3)
    # page = request.GET.get('page')
    # listademanda = paginator.get_page(page)
    context = {
        'notas': notas
    }

    return render(request, 'notascadastradas.html',  context)