# Generated by Django 4.2.6 on 2023-10-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Carro_app', '0003_imagem_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='carro',
        ),
        migrations.AddField(
            model_name='carro',
            name='fotos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Carro_app.album'),
        ),
    ]
