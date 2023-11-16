from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

from library.forms import BookForm, ClienteForm, RentForm
from library.models import Livro, Cliente, Cliente_Livro


def index(request):
    return redirect('library:livro')


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            # não vai salvar diretamente na base de dados
            book = form.save(commit=False)

            book.save()  # salva na base de dados
            return redirect('library:create_book')

        return render(
            request,
            'library/create_book.html',
            context,
        )

    context = {
        'form': BookForm()
    }
    return render(
        request,
        'library/create_book.html',
        context,
    )


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            # não vai salvar diretamente na base de dados
            cliente = form.save(commit=False)

            cliente.save()  # salva na base de dados
            return redirect('library:create_cliente')

        return render(
            request,
            'library/create_cliente.html',
            context,
        )

    context = {
        'form': ClienteForm()
    }
    return render(
        request,
        'library/create_cliente.html',
        context,
    )


def rent_book(request, livro_id):
    if request.method == 'POST':
        form = RentForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            livro = get_object_or_404(Livro, pk=livro_id)
            if (livro.disponivel == True):
                # não vai salvar diretamente na base de dados
                rent = form.save(commit=False)
                # rent.alugado = True
                livro.disponivel = False
                # single_cliente = get_object_or_404(Cliente, pk=cliente_id)
                # print(livro)
                rent.id_livro = livro
                # print(rent)
                livro.save()
                rent.save()  # salva na base de dados
                return redirect('library:livro')

        return render(
            request,
            'library/rent_book.html',
            context,
        )

    context = {
        'form': RentForm()
    }
    return render(
        request,
        'library/rent_book.html',
        context,
    )


def return_book(request, livro_id):
    if request.method == 'POST':
        cliente_livro = get_object_or_404(Cliente_Livro, id_livro=livro_id)
        livro = get_object_or_404(Livro, pk=livro_id)
        cliente_livro.delete()
        livro.disponivel = True
        livro.save()
        return redirect('library:livro')
