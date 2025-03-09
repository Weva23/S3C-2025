from rest_framework import generics
from .models import Enseignant
from .serializers import EnseignantSerializer

class EnseignantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class EnseignantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Matiere
from .serializers import MatiereSerializer

from rest_framework import viewsets
from .models import Matiere
from .serializers import MatiereSerializer

class MatiereViewSet(viewsets.ModelViewSet):  # Doit être ModelViewSet pour autoriser POST
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer


    def create(self, request, *args, **kwargs):
        """Créer une nouvelle matière"""
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """Lister toutes les matières"""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Récupérer une matière spécifique"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Mettre à jour une matière"""
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Supprimer une matière"""
        return super().destroy(request, *args, **kwargs)
