# Generated by Django 4.2.5 on 2023-10-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_delete_telefone_cliente_telefone_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone_1',
            field=models.CharField(max_length=15),
        ),
    ]
