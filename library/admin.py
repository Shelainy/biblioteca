from django.contrib import admin
from library import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    #quais colunas da tabela vão ser exibidas na adm do django
    list_display = 'id', 'nome', 'genero', 'escritor', 'edicao', 'editora', 'data_pub', 'disponivel',
    #qual coluna irá ser usada para a ordenação padrão (-id é id em ordem descrescente)
    ordering = '-id',
    #adiciona filtros e define quais colunas serão usadas na filtragem
    list_filter = 'editora', 'escritor', 'genero',
    #adicionar campo de search e definir quais colunas vão poder ser usados na pesquisa
    search_fields = 'nome','editora', 'escritor', 'genero',
    #adiciona paginação e define o máximo de itens por página
    list_max_show_all = 10
    #define quais colunas podem ser editados sem ter que abrir ele (adiciona input no item)
    #list_editable = 'editora', 'escritor',
    #define quais colunas receberão links para abrir a página de edição do item
    list_display_links = 'id', 'nome',

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    #quais colunas da tabela vão ser exibidas na adm do django
    list_display = 'id', 'nome', 'sobrenome', 'cpf', 'nascimento', 'email', 'cep',
    #qual coluna irá ser usada para a ordenação padrão (-id é id em ordem descrescente)
    ordering = '-id',
    #adicionar campo de search e definir quais colunas vão poder ser usados na pesquisa
    search_fields = 'nome', 'sobrenome', 'cpf', 'email',
    #adiciona paginação e define o máximo de itens por página
    list_max_show_all = 10
    #define quais colunas receberão links para abrir a página de edição do item
    list_display_links = 'id', 'nome', 'sobrenome',