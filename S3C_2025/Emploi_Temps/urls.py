from django.urls import path, include
from .views import EnseignantListCreateAPIView, EnseignantRetrieveUpdateDestroyAPIView, AffecterEnseignantView, ListeAffectationsView, ChargeHebdoViewSet
from rest_framework.routers import DefaultRouter

# Créer un routeur pour les vues basées sur les ViewSets
router = DefaultRouter()
router.register(r'charge-hebdo', ChargeHebdoViewSet)

# URLs spécifiques à vos vues
urlpatterns = [
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),
    path('affecter/', AffecterEnseignantView.as_view(), name='affecter_enseignant'),
    path('affectations/', ListeAffectationsView.as_view(), name='liste_affectations'),
]

# Inclure les routes générées par le routeur pour l'API de charge-hebdo
urlpatterns += router.urls
