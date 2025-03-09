from rest_framework import generics, viewsets, filters, status
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Matiere, Enseignant, Groupe, Affectation
from .serializers import MatiereSerializer, EnseignantSerializer, GroupeSerializer, AffectationSerializer
from rest_framework.permissions import AllowAny
permission_classes = [AllowAny]

# ✅ ViewSet pour Matiere (Correct pour DefaultRouter)
class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer
    permission_classes = [AllowAny]  # ✅ Permet l'accès à tout le monde


# ✅ APIViews pour Enseignants
class EnseignantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class EnseignantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

# ✅ APIView pour Affecter un Enseignant
class AffecterEnseignantView(APIView):
    def post(self, request):
        enseignant_id = request.data.get('enseignant_id')
        matiere_id = request.data.get('matiere_id')
        groupe_id = request.data.get('groupe_id')
        type_enseignement = request.data.get('type')

        try:
            enseignant = Enseignant.objects.get(id=enseignant_id)
            matiere = Matiere.objects.get(id=matiere_id)
            groupe = Groupe.objects.get(id=groupe_id)
        except (Enseignant.DoesNotExist, Matiere.DoesNotExist, Groupe.DoesNotExist):
            return Response({"error": "Enseignant, Matière, ou Groupe non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        affectation = Affectation.objects.create(
            enseignant=enseignant,
            matiere=matiere,
            groupe=groupe,
            type=type_enseignement
        )

        serializer = AffectationSerializer(affectation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# ✅ ViewSet pour Groupe (Correct pour DefaultRouter)
class GroupeViewSet(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    # permission_classes = [IsAuthenticated]  
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'filiere__nom', 'semestre']

# ✅ APIView pour Liste des Affectations
class ListeAffectationsView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        affectations = Affectation.objects.all()
        serializer = AffectationSerializer(affectations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
