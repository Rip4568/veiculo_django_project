# Generated by Django 4.2.6 on 2023-10-11 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Carro_app', '0005_alter_carro_fotos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagem',
            options={'managed': True, 'verbose_name': 'Imagem', 'verbose_name_plural': 'Imagens'},
        ),
        migrations.RemoveField(
            model_name='album',
            name='imagens',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='fotos',
        ),
        migrations.AddField(
            model_name='album',
            name='carro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='Carro_app.carro'),
        ),
        migrations.AddField(
            model_name='imagem',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='Carro_app.album'),
        ),
    ]
