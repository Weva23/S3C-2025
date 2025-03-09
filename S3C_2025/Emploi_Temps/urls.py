from django.urls import path
from .views import EnseignantListCreateAPIView, EnseignantRetrieveUpdateDestroyAPIView, AffecterEnseignantView, ListeAffectationsView

urlpatterns = [
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),
    path('affecter/', AffecterEnseignantView.as_view(), name='affecter_enseignant'),
    path('affectations/', ListeAffectationsView.as_view(), name='liste_affectations'),
]



router = DefaultRouter()
router.register(r'groupes', GroupeViewSet)  # Génération des routes CRUD

urlpatterns = [
    path('', include(router.urls)),  # Routes API automatiques
]



