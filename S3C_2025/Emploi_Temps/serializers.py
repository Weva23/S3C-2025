from rest_framework import serializers


from .models import *




class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'


class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'


class AffectationSerializer(serializers.ModelSerializer):
    enseignant = EnseignantSerializer()
    matiere = MatiereSerializer()
    groupe = GroupeSerializer()

    class Meta:
        model = Affectation
        fields = '__all__'


class DisponibiliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilite
        fields = '__all__'