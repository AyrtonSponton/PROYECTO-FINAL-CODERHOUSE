# Generated by Django 4.0.4 on 2022-06-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppArquitectos', '0003_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='imagen',
        ),
        migrations.AddField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
