# Generated by Django 4.2.5 on 2023-10-14 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_cliente_telefone_1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClienteLivro',
        ),
    ]
