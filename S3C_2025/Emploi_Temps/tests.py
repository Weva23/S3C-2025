# tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Affectation, Enseignant, Matiere, Groupe, ChargeHebdo

class ChargeHebdoTests(APITestCase):
    def setUp(self):
        self.matiere = Matiere.objects.create(nom='Mathématiques', code='MATH101', credits=3, semestre=1)
        self.groupe = Groupe.objects.create(nom='Groupe A', semestre=1, filiere=None)

    def test_create_charge_hebdo(self):
        data = {
            'matiere': self.matiere.id,
            'groupe': self.groupe.id,
            'cm': 4,
            'td': 2,
            'tp': 1,
            'disponibilites_enseignant': {"lundi": "10:00-12:00", "mercredi": "14:00-16:00"}
        }
        response = self.client.post('/api/charge-hebdo/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['cm'], 4)

    def test_update_charge_hebdo(self):
        charge = ChargeHebdo.objects.create(matiere=self.matiere, groupe=self.groupe, cm=4, td=2, tp=1)
        data = {
            'matiere': self.matiere.id,
            'groupe': self.groupe.id,
            'cm': 5,
            'td': 2,
            'tp': 1,
            'disponibilites_enseignant': {"lundi": "10:00-12:00", "vendredi": "14:00-16:00"}
        }
        response = self.client.put(f'/api/charge-hebdo/{charge.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cm'], 5)

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
