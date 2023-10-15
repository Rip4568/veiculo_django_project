from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #?sessão de administração padrão do django
    path('admin/', admin.site.urls),
    #?rotas para os apps
    path('', include('Rest_app.urls')),
    #?rotas de autentificação do rest_framework
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)