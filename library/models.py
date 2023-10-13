from django.db import models
from django.utils import timezone

# id (primary key - automático)
# name (string), genero (string), escritor (string)
# editora (string), data_pub (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Book(models.Model):
    nome = models.CharField(max_length=254)
    genero = models.CharField(max_length=50)
    escritor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    data_pub = models.DateField()

    def __str__(self) -> str:
        return f'{self.nome} - {self.escritor}'