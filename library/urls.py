from django.urls import path
from library import views
app_name = 'library'

urlpatterns = [
    path('clientes/<int:cliente_id>/detail',
         views.cliente_info, name='cliente_info'),
    path('clientes/create/', views.create_cliente, name='create_cliente'),
    path('clientes/csearch/', views.cliente_search, name='csearch'),
    path('clientes/', views.cliente, name='cliente'),

    path('livros/create/', views.create_book, name='create_book'),
    path('livros/', views.livro, name='livro'),
    path('lsearch/', views.livro_search, name='lsearch'),

    # path('rent/create/', views.create_rent, name='create_rent'),



    path('livros/<int:livro_id>/rent',
         views.rent_book, name='rent_book'),

    path('livros/<int:livro_id>/return',
         views.return_book, name='return_book'),  # type: ignore

    path('', views.index, name='index'),


    # path('', views.index, name='index'),

    # livros (CRUD)

]
