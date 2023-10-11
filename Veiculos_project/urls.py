from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #?sessão de administração padrão do django
    path('admin/', admin.site.urls),
    #?rotas para os apps
    path('', include('Rest_app.urls')),
    #?rotas de autentificação do rest_framework
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
