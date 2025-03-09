<<<<<<< HEAD

from datetime import timedelta
from rest_framework import generics, viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Affectation, Enseignant, Matiere, Groupe, Disponibilite, Calendrier
from .serializers import (
    EnseignantSerializer,
    AffectationSerializer,
    GroupeSerializer,
    DisponibiliteSerializer
)
=======
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
>>>>>>> f9998d1d562e137f9fee37bace2a2a2672ceedb9


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



class DisponibiliteViewSet(viewsets.ModelViewSet):
    queryset = Disponibilite.objects.all()
    serializer_class = DisponibiliteSerializer


# ----- Vue pour mettre à jour la disponibilité -----
class UpdateDisponibiliteView(APIView):

    def post(self, request, pk):
        try:
            disponibilite = Disponibilite.objects.get(pk=pk)
        except Disponibilite.DoesNotExist:
            return Response({"error": "Disponibilité non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        disponibilite.disponible = request.data.get('disponible', disponibilite.disponible)
        disponibilite.save()
        return Response({'status': 'Disponibilité mise à jour'})


# ----- Vue pour copier les disponibilités de la semaine précédente -----
class CopyPreviousWeekView(APIView):

    def post(self, request):
        enseignant_id = request.data.get('enseignant_id')
        current_week = request.data.get('current_week')

        if not enseignant_id or not current_week:
            return Response({"error": "Enseignant ID et semaine actuelle requis"}, status=status.HTTP_400_BAD_REQUEST)

        previous_week = current_week - timedelta(weeks=1)

        previous_disponibilites = Disponibilite.objects.filter(enseignant_id=enseignant_id, calendrier__date=previous_week)

        new_disponibilites = [
            Disponibilite(
                enseignant=dispo.enseignant,
                calendrier=Calendrier.objects.create(jour=dispo.calendrier.jour + timedelta(days=7)),
                disponible=dispo.disponible
            )
            for dispo in previous_disponibilites
        ]

        Disponibilite.objects.bulk_create(new_disponibilites)

        return Response({'status': 'Disponibilités copiées depuis la semaine précédente'})


# ----- Vue pour reconduire les disponibilités à la semaine suivante -----
class ReconduireDisponibilitesView(APIView):

    def post(self, request):
        enseignant_id = request.data.get('enseignant_id')

        if not enseignant_id:
            return Response({"error": "Enseignant ID requis"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            enseignant = Enseignant.objects.get(id=enseignant_id)
        except Enseignant.DoesNotExist:
            return Response({"error": "Enseignant non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        # Récupérer les dernières disponibilités
        latest_disponibilites = Disponibilite.objects.filter(
            enseignant=enseignant
        ).order_by('-calendrier__date')[:7]

        new_disponibilites = [
            Disponibilite(
                enseignant=enseignant,
                calendrier=Calendrier.objects.create(jour=dispo.calendrier.jour + timedelta(days=7)),
                disponible=dispo.disponible
            )
            for dispo in latest_disponibilites
        ]

        Disponibilite.objects.bulk_create(new_disponibilites)
        return Response({"status": "Disponibilités reconduites avec succès"})