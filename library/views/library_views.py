from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from library.models import Livro
from library.models import Cliente

def index(request):
    return render(
        request,
        'library/index.html',
    )

def livro(request):
    livros = Livro.objects.all().order_by('nome') #.filter(disponivel=True): antes do order_by para exibir apenas os livros disponiveis 
    context= {
        'livros':livros,
        'site_title': "Livros - "
    }


    return render(
        request,
        'library/livros.html',
        context
    )

def livro_search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('library:livro')

    livros = Livro.objects.all() \
        .filter(
            Q(nome__icontains=search_value) |
            Q(genero__icontains=search_value) |
            Q(escritor__icontains=search_value) |
            Q(editora__icontains=search_value)
        ) \
        .order_by('nome')
    
    context= {
        'livros':livros,
        'site_title': "Livros - "
    }


    return render(
        request,
        'library/livros.html',
        context
    )

def cliente(request):
    clientes = Cliente.objects.all().order_by('nome')
    context= {
        'clientes':clientes,
        'site_title': "Clientes - "
    }


    return render(
        request,
        'library/clientes.html',
        context
    )

def cliente_search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('library:cliente')
    
    
    clientes = Cliente.objects.all() \
        .filter(
            Q(nome__icontains=search_value) |
            Q(sobrenome__icontains=search_value) |
            Q(cpf__icontains=search_value) |
            Q(email__icontains=search_value)
        ) \
        .order_by('nome')
    context= {
        'clientes':clientes,
        'site_title': "Clientes - "
    }


    return render(
        request,
        'library/clientes.html',
        context
    )

def cliente_info(request, cliente_id):
    single_cliente = get_object_or_404(Cliente, pk=cliente_id)
    #single_cliente = get_object_or_404(Cliente.objects.filter(pk=cliente_id))

    print(single_cliente)
    context= {
        'cliente':single_cliente,
        'site_title': single_cliente.nome + " " + single_cliente.sobrenome + " - "
    }


    return render(
        request,
        'library/cliente_info.html',
        context
    )