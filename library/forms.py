from django import forms
from django.core.exceptions import ValidationError
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Livro
        fields = (
            'nome', 'genero', 'escritor', 'editora', 'data_pub'
        )


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = (
            'nome_completo', 'cpf', 'nascimento', 'telefone', 'email', 'endereco',
        )


class RentForm(forms.ModelForm):
    class Meta:
        model = models.Cliente_Livro
        fields = (
            'id_cliente',
        )
