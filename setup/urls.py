from django.contrib import admin 
from django.urls import path, include

# Imports essenciais para o gerenciamento de arquivos de mídia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota do painel administrativo 
    path('admin/', admin.site.urls),
    
    # Diz ao Django para olhar as rotas de dentro do aplicativo 'cardapio'
    path('', include('cardapio.urls')),
]

# Adiciona a rota de arquivos de mídia quando estamos em modo debug 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)