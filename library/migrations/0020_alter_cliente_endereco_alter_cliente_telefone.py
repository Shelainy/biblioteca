# Generated by Django 4.2.5 on 2023-10-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_rename_nome_cliente_nome_completo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15, verbose_name='Telefone para contato'),
        ),
    ]
