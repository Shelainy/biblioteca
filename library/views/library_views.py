from django.shortcuts import render
from library.models import Livro
from library.models import Cliente

def index(request):
    livros = Livro.objects.all().order_by('nome') #.filter(disponivel=True): antes do order_by para exibir apenas os livros disponiveis 
    context= {
        'livros':livros
    }


    return render(
        request,
        'library/index.html',
        context
    )

def cliente(request):
    clientes = Cliente.objects.all().order_by('nome')
    context= {
        'clientes':clientes
    }


    return render(
        request,
        'library/clientes.html',
        context
    )

def cliente_info(request, cliente_id):
    single_cliente = Cliente.objects.get(pk=cliente_id)
    print(single_cliente)
    context= {
        'cliente':single_cliente
    }


    return render(
        request,
        'library/cliente_info.html',
        context
    )