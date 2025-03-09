from rest_framework import generics
from .serializers import EnseignantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Affectation, Enseignant, Matiere, Groupe, ChargeHebdo
from .serializers import AffectationSerializer
from rest_framework import status
from rest_framework import viewsets
from .serializers import ChargeHebdoSerializer, GroupeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class ChargeHebdoViewSet(viewsets.ModelViewSet):
    queryset = ChargeHebdo.objects.all()
    serializer_class = ChargeHebdoSerializer

    def create(self, request, *args, **kwargs):
        matiere_id = request.data.get('matiere')
        groupe_id = request.data.get('groupe')

        try:
            matiere = Matiere.objects.get(id=matiere_id)
        except Matiere.DoesNotExist:
            return Response({"detail": "Matière non trouvée"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            groupe = Groupe.objects.get(id=groupe_id)
        except Groupe.DoesNotExist:
            return Response({"detail": "Groupe non trouvé"}, status=status.HTTP_400_BAD_REQUEST)

        charge_hebdo = ChargeHebdo.objects.filter(matiere=matiere, groupe=groupe).first()

        if charge_hebdo:
            charge_hebdo.cm = request.data.get('cm', charge_hebdo.cm)
            charge_hebdo.td = request.data.get('td', charge_hebdo.td)
            charge_hebdo.tp = request.data.get('tp', charge_hebdo.tp)
            charge_hebdo.disponibilites_enseignant = request.data.get('disponibilites_enseignant', charge_hebdo.disponibilites_enseignant)
            charge_hebdo.save()
            return Response(ChargeHebdoSerializer(charge_hebdo).data, status=status.HTTP_200_OK)
        else:
            charge_hebdo = ChargeHebdo.objects.create(
                matiere=matiere,
                groupe=groupe,
                cm=request.data.get('cm', 0),
                td=request.data.get('td', 0),
                tp=request.data.get('tp', 0),
                disponibilites_enseignant=request.data.get('disponibilites_enseignant', {})
            )
            return Response(ChargeHebdoSerializer(charge_hebdo).data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


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



