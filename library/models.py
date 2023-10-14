from django.db import models
from django.utils import timezone

#Book
# id (primary key - automático)
# name (string), genero (string), escritor (string), editora (string), data_pub (date), description (text)
#picture (imagem), disponivel (boolean)

#disponivel: False se o livro for alugado, True quando o livro é devolvido
#criar um trigger para mudar o valor quando o livro for alugado/devolvido
#livro não pode ser alugado se o valor = False

#Cliente
# id (primary key - automático)
# nome (string), sobrenome (string), cpf (string, unique key), nascimento (date), email (email), 
# rua (string), numero (string), complemento (string), bairro (string), cep (string)

# Telefone
# id (primary key - automático)
# id_cliente (foreing key), telefone (string)

#Cliente-livro
# id (primary key - automático)
# id_livro (foreign key), id_cliente (foreign_key), data_alugel (date), data_dev (date), multa (real)

#data_dev: Preenchido de acordo com o valor data_aluguel
#multa: calculado automaticamente de acordo com a diferença entre o dia atual e data_dev (default = 0)
# (Talvez criar um botão "Ver multa" para chamar uma função que faz o cálculo)

class Book(models.Model):
    nome = models.CharField(max_length=254)
    genero = models.CharField(max_length=50)
    escritor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    edicao = models.CharField(max_length=25)
    data_pub = models.DateField()
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/')
    disponivel = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nome} - {self.escritor}'
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, unique=True)
    nascimento = models.DateField()
    email = models.EmailField(max_length=254, blank=True)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.nome} '