from django.urls import path
from rest_framework import routers

from . import viewsets
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.DefaultRouter()
router.register('carros-model-viewsets', viewsets.CarroModelViewSet, basename='CarroModelViewSet')

urlpatterns = [
    #?rotas de autentificação do rest_framework utilizando JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
