from rest_framework import generics
from .models import Enseignant
from .serializers import EnseignantSerializer
    
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Groupe
from .serializers import GroupeSerializer

class EnseignantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class EnseignantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
    

class GroupeViewSet(viewsets.ModelViewSet):
    """
    API pour gérer les groupes : CRUD et filtres.
    """
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    permission_classes = [IsAuthenticated]  # Accès restreint aux utilisateurs connectés

    # Ajout de filtres pour rechercher les groupes
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'filiere__nom', 'semestre']

