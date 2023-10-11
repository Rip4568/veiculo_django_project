from django.db import models
from django.core import validators
from django.contrib.auth.models import User



class Imagem(models.Model):
  imagem = models.ImageField(upload_to="media/", 
    height_field=None, width_field=None, 
     max_length=None, blank=True, null=True)
  #album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="imagens", blank=True, null=True)

  def __str__(self):
    return f"{self.imagem}"

  class Meta:
    db_table = 'imagens'
    managed = True
    verbose_name = 'Imagem'
    verbose_name_plural = 'Imagens'

class Album(models.Model):
  carro = models.ForeignKey("Carro", on_delete=models.CASCADE, related_name="albuns", blank=True, null=True)
  imagens = models.ManyToManyField(Imagem, related_name="albuns", blank=True, null=True)

  def __str__(self):
    return f"imagens: {self.imagens.count()}, carro: {self.carro.modelo}"

  class Meta:
    db_table = 'albuns'
    managed = True
    verbose_name = 'Album'
    verbose_name_plural = 'Albums'
  

class Carro(models.Model):
    modelo = models.ForeignKey("Modelo", on_delete=models.CASCADE)
    cor = models.CharField(max_length=255, choices=[
    ('Azul', 'Azul'),
    ('Branco', 'Branco'),
    ('Preto', 'Preto'),
    ('Vermelho', 'Vermelho'),
    ])
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
    
class Marca(models.Model):
  nome = models.CharField(max_length=255, blank=False, null=False)
  def __str__(self):
    return self.nome

  class Meta:
    db_table = 'marcas'
    managed = True
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'
    
class Modelo(models.Model):
  nome = models.CharField(max_length=255, blank=False, null=False)
  marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=False, null=False)
  ano = models.IntegerField(blank=False, null=False)

  def __str__(self):
    return self.nome

  class Meta:
    db_table = 'modelos'
    managed = True
    verbose_name = 'Modelo'
    verbose_name_plural = 'Modelos'