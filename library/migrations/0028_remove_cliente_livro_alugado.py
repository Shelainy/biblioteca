# Generated by Django 4.2.5 on 2023-10-28 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0027_cliente_livro_alugado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente_livro',
            name='alugado',
        ),
    ]
