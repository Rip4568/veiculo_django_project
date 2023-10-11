from Carro_app.models import Carro, Modelo, Marca, Imagem, Album
from django.contrib.auth.models import User
from rest_framework import serializers

class CarroModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Carro
    fields = '__all__'
    
class UserModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
  
class ModeloModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Modelo
    fields = '__all__'
    
class MarcaModelSerializer(serializers.ModelSerializer):
 class Meta:
   model = Marca
   fields = '__all__'
   
class ImagemModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Imagem
    fields = '__all__'


class AlbumModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = '__all__'









