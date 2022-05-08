# Createfrom django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Fornecedores, Cliente, Produto, Servicos
from .forms import FornecedoresForm, ProdutoForm, ClienteForm, ServicoForm



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

            return redirect('/')
    else:        
        form = FornecedoresForm()
        return render(request, 'cadfornecedores.html', {'form': form})

# lista de fornecedores
@login_required 
def meusfornecedores(request):
    fornlist = Fornecedores.objects.all().filter()
    paginator = Paginator(fornlist, 3)
    page = request.GET.get('page')
    listafornecedores = paginator.get_page(page)

    return render(request, 'fornecedorescadastrados.html', {'listafornecedores' : listafornecedores})
# cadastro produto
@login_required 
def produtocad(request):
    if request.method == 'POST':
            form = ProdutoForm(request.POST)
            if form.is_valid():
             produto = form.save(commit=False)
             produto.user = request.user
             produto.save()

            return redirect('/')
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

            return redirect('/')
    else:        
        form = ClienteForm()
        return render(request, 'cadcliente.html', {'form': form})

# cadastro serviço
@login_required 
def servicocad(request):
    if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
             servicos = form.save(commit=False)
             servicos.user = request.user
             servicos.save()

            return redirect('/')
    else:        
        form = ServicoForm()
        return render(request, 'cadservico.html', {'form': form})