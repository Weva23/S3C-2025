from rest_framework import generics
from .models import Enseignant
from .serializers import EnseignantSerializer

class EnseignantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class EnseignantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer
