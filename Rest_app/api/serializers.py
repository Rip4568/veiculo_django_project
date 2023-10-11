from Carro_app.models import Carro
from django.contrib.auth.models import User
from rest_framework import serializers

class CarroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Carro
    fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user