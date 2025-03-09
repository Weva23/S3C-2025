from rest_framework import serializers
from .models import Enseignant, Affectation, Matiere, Groupe, Filiere, ChargeHebdo, Disponibilite



# Serializer pour ChargeHebdo
class ChargeHebdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeHebdo
        fields = ['matiere', 'groupe', 'cm', 'td', 'tp', 'disponibilites_enseignant']



from .models import Affectation, Enseignant, Matiere, Groupe, Filiere




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


from rest_framework import serializers
from .models import Matiere


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


# Serializer pour Disponibilite
class DisponibiliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilite
        fields = '__all__'
from rest_framework import serializers
from .models import EmploiTemps

class EmploiTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploiTemps
        fields = "__all__"  # ✅ Inclut maintenant creneau_fixe
