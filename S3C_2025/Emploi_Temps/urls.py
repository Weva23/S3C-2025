from django.urls import path, include
from .views import EnseignantListCreateAPIView, EnseignantRetrieveUpdateDestroyAPIView,MatiereViewSet

from rest_framework.routers import DefaultRouter


  # Vérifie que 'matieres' est bien défini ici
router = DefaultRouter()
router.register(r'matieres', MatiereViewSet, basename='matiere')

urlpatterns = [
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),
    
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),
    path('api/', include(router.urls)), 
    # path('api/enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),  # Ajoute d'autres routes si besoin
]


