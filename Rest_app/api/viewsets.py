from rest_framework import viewsets

from .serializers import UserSerializer, CarroSerializer

from django.contrib.auth.models import User

from Carro_app.models import Carro

class CarroModelViewSet(viewsets.ModelViewSet):
  queryset = Carro.objects.all()
  serializer_class = CarroSerializer