from django.urls import path, include
<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from .views import (
    # Enseignants
    EnseignantListCreateAPIView,
    EnseignantRetrieveUpdateDestroyAPIView,

    # Groupes
    GroupeViewSet,

    # Affectations
    AffecterEnseignantView,
    ListeAffectationsView,

    # Disponibilités
    DisponibiliteViewSet,
    UpdateDisponibiliteView,
    CopyPreviousWeekView,
    ReconduireDisponibilitesView
)

# ----- Router pour les ViewSets -----
router = DefaultRouter()
router.register(r'groupes', GroupeViewSet)
router.register(r'disponibilites', DisponibiliteViewSet)

# ----- URL patterns -----
urlpatterns = [
    # URLs pour les enseignants
    path('enseignants/', EnseignantListCreateAPIView.as_view(), name='enseignant-list-create'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyAPIView.as_view(), name='enseignant-detail'),

    # URLs pour les affectations
    path('affectations/', ListeAffectationsView.as_view(), name='liste-affectations'),
    path('affectations/affecter/', AffecterEnseignantView.as_view(), name='affecter-enseignant'),

    # URLs pour les disponibilités
    path('', include(router.urls)),  # CRUD pour Groupes et Disponibilités via ViewSets
    path('disponibilites/<int:pk>/update/', UpdateDisponibiliteView.as_view(), name='update-disponibilite'),
    path('disponibilites/copy-previous-week/', CopyPreviousWeekView.as_view(), name='copy-previous-week'),
    path('disponibilites/reconduire/', ReconduireDisponibilitesView.as_view(), name='reconduire-disponibilites'),
]
=======
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
>>>>>>> f9998d1d562e137f9fee37bace2a2a2672ceedb9
