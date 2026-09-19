from django.contrib import admin 
from django.urls import path
from cardapio import views

# Imports essenciais para o gerenciamento de arquivos de mídia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # essa é a rota do painel administrativo 
    path('admin/', admin.site.urls),
    
    # 2. criamos a rota da pag inicial do restaurante 
    path('', views.vitrine_digital, name='vitrine'),
]

# Adiciona a rota de arquivos de mídia quando estamos em modo debug 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)