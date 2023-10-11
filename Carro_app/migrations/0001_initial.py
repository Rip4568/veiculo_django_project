# Generated by Django 4.2.6 on 2023-10-11 13:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('ano', models.IntegerField()),
                ('placa', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
                'db_table': 'carros',
                'managed': True,
            },
        ),
    ]