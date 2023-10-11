from django.db import models
from django.core import validators
from django.contrib.auth.models import User

class Carro(models.Model):
  modelo = models.CharField(max_length=255, blank=False, null=False)
  ano = models.IntegerField(blank=False, null=False)
  placa = models.CharField(max_length=255, blank=False, null=False)
  marca = models.CharField(max_length=255, blank=False, null=False)
  cor = models.CharField(max_length=255, blank=False, null=False)
  proprietario = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
  preco = models.DecimalField(max_digits=12,
    decimal_places=2, blank=False, null=False,
    validators=[validators.MinValueValidator(0.0)]
  )

  def __str__(self):
    return f"proprietario: {self.proprietario}, modelo: {self.modelo}, preco: {self.preco}"

  class Meta:
    db_table = 'carros'
    managed = True
    verbose_name = 'Carro'
    verbose_name_plural = 'Carros'