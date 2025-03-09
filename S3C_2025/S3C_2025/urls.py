from django.contrib import admin
from django.urls import path, include
from django.apps import AppConfig

class EmploiTempsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Emploi_Temps'  # Assure-toi que c'est bien le bon nom
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Emploi_Temps.urls')),
]

