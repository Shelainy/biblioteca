# Generated by Django 4.2.5 on 2023-10-21 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0023_alter_cliente_livro_data_aluguel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_livro',
            name='data_aluguel',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]