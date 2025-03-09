from django.urls import path
from .views import EnseignantListCreateAPIView, EnseignantRetrieveUpdateDestroyAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupeViewSet

urlpatterns = [
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),
]


router = DefaultRouter()
router.register(r'groupes', GroupeViewSet)  # Génération des routes CRUD

urlpatterns = [
    path('', include(router.urls)),  # Routes API automatiques
]
