from django import forms
from django.core.exceptions import ValidationError
# from localflavor.br.forms import BRCPFField
# from pycpfcnpj import cpfcnpj
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

        # cpf = BRCPFField()

        fields = (
            'nome_completo', 'cpf', 'nascimento', 'telefone', 'email', 'endereco',
        )

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if (len(cpf) != 11):
            raise ValidationError('CPF inválido', code='invalid')
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if (len(telefone) != 11):
            raise ValidationError('Telefone inválido', code='invalid')
        return telefone


class RentForm(forms.ModelForm):
    class Meta:
        model = models.Cliente_Livro
        fields = (
            'id_cliente',
        )
