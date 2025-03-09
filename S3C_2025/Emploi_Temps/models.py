from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    identifiant = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class Filiere(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('enseignant', 'Enseignant'),
        ('etudiant', 'Etudiant'),
    ]

    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    filiere = models.ForeignKey(Filiere, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


from django.db import models




class Matiere(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=100)
    credits = models.IntegerField()
    semestre = models.IntegerField(choices=[(i, f"Semestre {i}") for i in range(1, 7)])
    filiere_choices = [
        ('TC', 'Tronc Commun'),
        ('DWM', 'Développement Web et Mobile'),
        ('DSI', 'Développement de Systèmes Informatiques'),
        ('RSS', 'Réseaux et Sécurité des Systèmes'),
    ]
    filiere = models.CharField(max_length=10, choices=filiere_choices)

    def __str__(self):
        return f"{self.code} - {self.nom}"



class Groupe(models.Model):
    nom = models.CharField(max_length=255)
    semestre = models.IntegerField()
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    parent_groupe = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.nom} (Semestre {self.semestre})"


class Calendrier(models.Model):
    date = models.DateField()
    jour = models.CharField(max_length=10, choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), 
                                                   ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi')])
    plage_horaire = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.jour} - {self.plage_horaire}'


class Disponibilite(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    calendrier = models.ForeignKey(Calendrier, on_delete=models.CASCADE)
    disponible = models.BooleanField()

    def __str__(self):
        return f'{self.enseignant} - {self.calendrier} - {"Disponible" if self.disponible else "Indisponible"}'


class ChargeHebdo(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    cm = models.IntegerField(default=0)
    td = models.IntegerField(default=0)
    tp = models.IntegerField(default=0)
    disponibilites_enseignant = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.matiere} - {self.groupe}"


class Affectation(models.Model):
    TYPE_CHOICES = [
        ('CM', 'CM'),
        ('TD', 'TD'),
        ('TP', 'TP'),
    ]

    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):

        return f'{self.enseignant} - {self.matiere} - {self.groupe} - {self.type}'


class EmploiTemps(models.Model):
    TYPE_CHOICES = [
        ('CM', 'CM'),
        ('TD', 'TD'),
        ('TP', 'TP'),
    ]

    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    calendrier = models.ForeignKey(Calendrier, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    
    # ✅ Ajout du champ pour fixer un créneau
    creneau_fixe = models.BooleanField(default=False)  

    def __str__(self):
        return f'{self.groupe} - {self.matiere} - {self.enseignant} - {self.calendrier} - {self.type}'

class Exception(models.Model):
    calendrier = models.ForeignKey(Calendrier, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=[('Ajouter', 'Ajouter'), ('Supprimer', 'Supprimer')])

    def __str__(self):
        return f'{self.calendrier} - {self.action}'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    lu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.created_at}'
