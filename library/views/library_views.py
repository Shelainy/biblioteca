from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from library.models import *
from library.models import Cliente
from library.models import Livro


# def index(request):
#    return render(
#        request,
#        'library/index.html',
#    )


def index(request):
    return redirect('library:livro')


def livro(request):
    # .filter(disponivel=True): antes do order_by para exibir apenas os livros disponiveis
    livros = Livro.objects.all().order_by('nome')

    paginator = Paginator(livros, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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

    print(livros)

    paginator = Paginator(livros, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': "Livros - ",
    }

    return render(
        request,
        'library/livros.html',
        context
    )


def cliente(request):
    clientes = Cliente.objects.all().order_by('nome_completo')

    paginator = Paginator(clientes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': "Clientes - ",
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
            Q(nome_completo__icontains=search_value) |
            Q(cpf__icontains=search_value) |
            Q(email__icontains=search_value)
    ) \
        .order_by('nome_completo')

    paginator = Paginator(clientes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': "Clientes - ",
    }

    return render(
        request,
        'library/clientes.html',
        context
    )


def cliente_info(request, cliente_id):
    single_cliente = get_object_or_404(Cliente, pk=cliente_id)
    # single_cliente = get_object_or_404(Cliente.objects.filter(pk=cliente_id))

    print(single_cliente)
    context = {
        'cliente': single_cliente,
        'site_title': single_cliente.nome_completo
    }

    return render(
        request,
        'library/cliente_info.html',
        context
    )


def aluguel(request):
    # .filter(disponivel=True): antes do order_by para exibir apenas os livros disponiveis
    alugueis = Cliente_Livro.objects.all().order_by('id_livro')

    paginator = Paginator(alugueis, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': "Alugueis - "
    }

    return render(
        request,
        'library/alugueis.html',
        context
    )


def aluguel_search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('library:aluguel')

    alugueis = Cliente_Livro.objects.all() \
        .filter(
            Q(id_livro__icontains=search_value) |
            Q(id_cliente__icontains=search_value)
    ) \
        .order_by('id_livro')

    paginator = Paginator(alugueis, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': "Alugueis - ",
    }

    return render(
        request,
        'library/alugueis.html',
        context
    )
