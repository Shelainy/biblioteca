# Generated by Django 4.2.5 on 2023-10-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_rename_book_livro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_livro',
            name='data_aluguel',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='edicao',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
