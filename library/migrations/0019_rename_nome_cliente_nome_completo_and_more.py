# Generated by Django 4.2.5 on 2023-10-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_alter_cliente_livro_data_aluguel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nome',
            new_name='nome_completo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='rua',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='sobrenome',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone_1',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone_2',
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(default='Endereço', max_length=254),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='123456', max_length=15, verbose_name='Telefone para contato'),
        ),
        migrations.AlterField(
            model_name='cliente_livro',
            name='data_aluguel',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_pub',
            field=models.DateField(verbose_name='data de publicação'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='edicao',
            field=models.CharField(blank=True, max_length=25, verbose_name='edição'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.CharField(max_length=50, verbose_name='gênero'),
        ),
    ]
