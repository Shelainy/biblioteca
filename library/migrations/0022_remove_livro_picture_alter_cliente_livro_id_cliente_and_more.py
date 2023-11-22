# Generated by Django 4.2.5 on 2023-10-21 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_remove_cliente_cep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='picture',
        ),
        migrations.AlterField(
            model_name='cliente_livro',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente_livro',
            name='id_livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.livro', verbose_name='Livro'),
        ),
    ]