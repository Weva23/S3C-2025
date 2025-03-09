# tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Affectation, Enseignant, Matiere, Groupe

class AffectationTests(APITestCase):

    def test_affectation_creation(self):
        enseignant = Enseignant.objects.create(nom="Prof A", identifiant="A123")
        matiere = Matiere.objects.create(code="MAT123", nom="Mathématiques", credits=4, semestre=1, filiere_id=1)
        groupe = Groupe.objects.create(nom="Groupe 1", semestre=1, filiere_id=1)

        url = '/api/affecter/'
        data = {
            "enseignant_id": enseignant.id,
            "matiere_id": matiere.id,
            "groupe_id": groupe.id,
            "type": "CM"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_liste_affectations(self):
        url = '/api/affectations/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
