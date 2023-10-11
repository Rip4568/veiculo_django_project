from rest_framework import viewsets, serializers, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import (
    CarroModelSerializer,
    ImagemModelSerializer,
    AlbumModelSerializer,
    MarcaModelSerializer,
    ModeloModelSerializer,
    UserModelSerializer,
)
from django.contrib.auth.models import User
from Carro_app.models import Carro
from rest_framework.pagination import PageNumberPagination

class CarroModelViewSet(viewsets.ModelViewSet):
  pagination_class = PageNumberPagination
  queryset = Carro.objects.all().order_by('-preco')
  serializer_class = CarroModelSerializer
  def get_paginated_response(self, data):
        # Obtenha a resposta paginada padrão
        response = super().get_paginated_response(data)
        
        # Obtenha o número total de páginas
        total_pages = self.paginator.page.paginator.num_pages
        
        # Adicione o número total de páginas à resposta
        response.data['total_pages'] = total_pages
        
        #coloque as imagens e os albuns para seriliazar
        for carro in response.data['results']:
            carro["imagens"] = ImagemModelSerializer(Carro.objects.get(id=carro["id"]).albuns.first().imagens.all(), many=True).data

        return response
  
class CarroImagensViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroModelSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]  # Ajuste conforme suas necessidades

    def create(self, request, *args, **kwargs):
        imagens_data = request.data.pop('imagens', [])  # Extrai os dados das imagens
        carro_serializer = self.get_serializer(data=request.data)

        if carro_serializer.is_valid():
            carro = carro_serializer.save()

            for imagem_data in imagens_data:
                imagem_data['carro'] = carro.id  # Associa a imagem ao carro
                imagem_serializer = ImagemModelSerializer(data=imagem_data)

                if imagem_serializer.is_valid():
                    imagem_serializer.save()
                else:
                    carro.delete()
                    return Response(imagem_serializer.errors, status=400)

            return Response(carro_serializer.data, status=201)

        return Response(carro_serializer.errors, status=400)