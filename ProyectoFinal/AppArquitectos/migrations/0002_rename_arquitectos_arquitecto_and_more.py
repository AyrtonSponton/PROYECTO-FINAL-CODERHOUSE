# Generated by Django 4.0.4 on 2022-05-25 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppArquitectos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='arquitectos',
            new_name='Arquitecto',
        ),
        migrations.RenameModel(
            old_name='edificios',
            new_name='Edificio',
        ),
    ]