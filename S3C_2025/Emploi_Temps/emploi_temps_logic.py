from ortools.sat.python import cp_model

def planifier_cours(groupes, matieres, enseignants, disponibilites, contraintes_fixes={}, maximiser=True):
    model = cp_model.CpModel()
    
    # 🔹 Vérifier et compléter les disponibilités des enseignants
    for e in enseignants:
        if e not in disponibilites:
            print(f"⚠️ Erreur : Disponibilité manquante pour l'enseignant {e}, ajout par défaut")
            disponibilites[e] = [False] * 30  # Par défaut, indisponible

    # 🔹 Variables : x[g, m, e, t] = 1 si le groupe g a la matière m enseignée par e au temps t
    x = {}
    for g in groupes:
        for m in matieres:
            for e in enseignants:
                for t in range(30):  # 30 créneaux (ex: 5 jours * 6 plages horaires)
                    x[g, m['code'], e, t] = model.NewBoolVar(f"x_{g}_{m['code']}_{e}_{t}")
    
    # 🔹 Contrainte : Un groupe ne peut pas avoir deux cours en même temps
    for g in groupes:
        for t in range(30):
            model.Add(sum(x[g, m['code'], e, t] for m in matieres for e in enseignants) <= 1)
    
    # 🔹 Contrainte : Un enseignant ne peut pas donner plusieurs cours en même temps
    for e in enseignants:
        for t in range(30):
            model.Add(sum(x[g, m['code'], e, t] for g in groupes for m in matieres) <= 1)
    
    # 🔹 Contrainte : Respect des disponibilités des enseignants
    for e in enseignants:
        for t in range(30):
            if not disponibilites[e][t]:  # Si indisponible, interdire le créneau
                for g in groupes:
                    for m in matieres:
                        model.Add(x[g, m['code'], e, t] == 0)
    
    # 🔹 Bonus 1 : Fixation manuelle des créneaux
    for (g, m_code, t_fixe) in contraintes_fixes:
        model.Add(sum(x[g, m_code, e, t_fixe] for e in enseignants) == 1)
    
    # 🔹 Bonus 2 : Maximiser le nombre de cours planifiés
    if maximiser:
        model.Maximize(sum(x[g, m['code'], e, t] for g in groupes for m in matieres for e in enseignants for t in range(30)))
    
    # 🔹 Résolution
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    # 🔹 Résultats
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        emploi_du_temps = []
        cours_non_planifies = []
        for g in groupes:
            for m in matieres:
                planified = False
                for e in enseignants:
                    for t in range(30):
                        if solver.Value(x[g, m['code'], e, t]) == 1:
                            emploi_du_temps.append({
                                "groupe": g,
                                "matiere": m['nom'],
                                "enseignant": e,
                                "creneau": t
                            })
                            planified = True
                if not planified:
                    cours_non_planifies.append({"groupe": g, "matiere": m['nom']})  # Ajoute les cours non planifiés
        
        return {
            "emploi_du_temps": emploi_du_temps,
            "cours_non_planifies": cours_non_planifies
        }
    else:
        return {"message": "Aucune solution trouvée. Essayez de modifier les contraintes."}


# 🔹 Exemple d'appel
emplois_du_temps = planifier_cours(
    groupes=['G1', 'G2'], 
    matieres=[
        {"code": "COM101", "nom": "Communication", "credits": 3, "semestre": 1, "filiere": "DWM"},
        {"code": "ALG202", "nom": "Algèbre 2", "credits": 4, "semestre": 2, "filiere": "DWM"},
        {"code": "PIX2", "nom": "Certification PIX2", "credits": 2, "semestre": 2, "filiere": "DWM"},
        {"code": "SYR21", "nom": "SYR21-SYR22", "credits": 3, "semestre": 3, "filiere": "DSI"},
        {"code": "CNM", "nom": "CNM", "credits": 3, "semestre": 3, "filiere": "DSI"},
        {"code": "PY101", "nom": "Programmation Python", "credits": 4, "semestre": 2, "filiere": "DSI"},
        {"code": "WEB101", "nom": "Langages web", "credits": 4, "semestre": 3, "filiere": "DWM"},
        {"code": "LAN101", "nom": "LAN", "credits": 3, "semestre": 3, "filiere": "RSS"},
        {"code": "SGBD101", "nom": "SGBD", "credits": 4, "semestre": 2, "filiere": "DSI"},
    ],
    enseignants=['Habeb', 'Cheikh', 'Med Cheikh', 'Aicha', 'Naji', 'Sidi Med', 'Lam', 'Sass', 'Meya', 'Haithem',
                 'F. Abdou', 'Moussa', 'Souvi', 'Abdarahmane', 'M. Lemine', 'Tourade', 'Hafeth'],
    disponibilites={
        "Habeb": [True]*30, "Cheikh": [True]*30, "Med Cheikh": [True]*30, "Aicha": [True]*30,
        "Naji": [True]*30, "Sidi Med": [True]*30, "Lam": [True]*30, "Sass": [True]*30,
        "Meya": [True]*30, "Haithem": [True]*30, "F. Abdou": [True]*30, "Moussa": [True]*30,
        "Souvi": [True]*30, "Abdarahmane": [True]*30, "M. Lemine": [True]*30, "Tourade": [True]*30,
        "Hafeth": [True]*30
    },
    contraintes_fixes=[("G1", "PY101", 5)],  # Ex: Programmation Python pour G1 fixé en plage 5
    maximiser=True
)

print(emplois_du_temps)
