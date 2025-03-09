from rest_framework import generics
from .serializers import EnseignantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Affectation, Enseignant, Matiere, Groupe
from .serializers import AffectationSerializer



    
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Groupe
from .serializers import GroupeSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Affectation, Enseignant, Matiere, Groupe
from .serializers import AffectationSerializer




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






class AffecterEnseignantView(APIView):

    def post(self, request):
        enseignant_id = request.data.get('enseignant_id')
        matiere_id = request.data.get('matiere_id')
        groupe_id = request.data.get('groupe_id')
        type_enseignement = request.data.get('type')

        # Vérifier que les objets existent
        try:
            enseignant = Enseignant.objects.get(id=enseignant_id)
            matiere = Matiere.objects.get(id=matiere_id)
            groupe = Groupe.objects.get(id=groupe_id)
        except (Enseignant.DoesNotExist, Matiere.DoesNotExist, Groupe.DoesNotExist):
            return Response({"error": "Enseignant, Matière, ou Groupe non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        # Créer l'affectation
        affectation = Affectation.objects.create(
            enseignant=enseignant,
            matiere=matiere,
            groupe=groupe,
            type=type_enseignement
        )

        serializer = AffectationSerializer(affectation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListeAffectationsView(APIView):

    def get(self, request):
        affectations = Affectation.objects.all()
        serializer = AffectationSerializer(affectations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



