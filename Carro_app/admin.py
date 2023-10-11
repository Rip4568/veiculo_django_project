from django.contrib import admin
from .models import Carro, Modelo, Marca, Imagem, Album

admin.site.register(Carro)
admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Imagem)
admin.site.register(Album)