# Generated by Django 4.2.5 on 2023-10-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]