from rest_framework import serializers
from .models import Enseignant, Affectation, Matiere, Groupe, Filiere, ChargeHebdo, Disponibilite


# Serializer pour ChargeHebdo
class ChargeHebdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeHebdo
        fields = ['matiere', 'groupe', 'cm', 'td', 'tp', 'disponibilites_enseignant']


# Serializer pour Enseignant
class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'


# Serializer pour Groupe
class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'


# Serializer pour Matiere
class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'


# Serializer pour Affectation
class AffectationSerializer(serializers.ModelSerializer):
    enseignant = EnseignantSerializer()
    matiere = MatiereSerializer()
    groupe = GroupeSerializer()

    class Meta:
        model = Affectation
        fields = '__all__'


# Serializer pour Disponibilite
class DisponibiliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilite
        fields = '__all__'
