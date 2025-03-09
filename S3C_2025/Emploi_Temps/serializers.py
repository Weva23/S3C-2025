from rest_framework import serializers


from .models import Enseignant
from .models import Groupe

from .models import Enseignant,Affectation, Enseignant, Matiere, Groupe, Filiere




from .models import Enseignant,Affectation, Enseignant, Matiere, Groupe, Filiere




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


