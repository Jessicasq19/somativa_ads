# Generated by Django 4.2.4 on 2023-10-11 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Somativa_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itensmanut',
            old_name='qtde',
            new_name='qtde_usada',
        ),
        migrations.RenameField(
            model_name='produtos',
            old_name='qtde',
            new_name='qtde_estoque',
        ),
    ]
