from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EnseignantListCreateAPIView, EnseignantRetrieveUpdateDestroyAPIView,
    AffecterEnseignantView, ListeAffectationsView,
    MatiereViewSet, GroupeViewSet
)

# ✅ Utilisation correcte du router avec des ViewSets
router = DefaultRouter()
router.register(r'matieres', MatiereViewSet, basename='matiere')  # ✅ Corrigé
router.register(r'groupes', GroupeViewSet, basename='groupe')  # ✅ Ajout de GroupeViewSet

urlpatterns = [
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),
    path('affecter/', AffecterEnseignantView.as_view(), name='affecter_enseignant'),
    path('affectations/', ListeAffectationsView.as_view(), name='liste_affectations'),
    path('', include(router.urls)),  # ✅ Le router s'occupe des routes des ViewSets
]
