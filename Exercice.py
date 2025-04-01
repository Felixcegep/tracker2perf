    # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
class Exercice:

    mouvements  = {
        "bench": "Exercice de musculation ciblant principalement les pectoraux, effectué avec une barre ou des haltères.",
        "squat": "Mouvement polyarticulaire sollicitant les jambes et les fessiers, souvent réalisé avec une barre sur les épaules.",
        "deadlift": "Exercice de force sollicitant le dos, les jambes et les bras, consistant à soulever une barre depuis le sol.",
        "pull-up": "Traction à la barre pour renforcer le dos et les bras en tirant son propre poids vers le haut.",
        "shoulder_press": "Développement des épaules avec une barre ou des haltères en poussant le poids au-dessus de la tête.",
        "bicep_curl": "Mouvement d'isolation pour les biceps, réalisé avec des haltères ou une barre en flexion des coudes.",
        "triceps_dips": "Exercice au poids du corps ciblant les triceps en descendant et remontant sur des barres parallèles.",
        "lunges": "Fentes pour travailler les jambes et les fessiers, réalisées avec ou sans charge supplémentaire.",
        "plank": "Exercice de gainage renforçant les abdominaux et le tronc en maintenant une position statique.",
        "leg_press": "Exercice sur machine pour muscler les jambes en poussant une plateforme avec les pieds."
    }
    def __init__(self, nomexercice:str):
        if nomexercice in Exercice.mouvements:

            self._nomexercice = nomexercice
        else:
            raise ValueError("exercice invalide veuillez l'ajouter a liste d'exercices")

    @property
    def nomexercice(self):
        return self._nomexercice

    @nomexercice.setter
    def nomexercice(self, nomexercice):
        if nomexercice in Exercice.mouvements:
            self._nomexercice = nomexercice
        else:
            raise ValueError("mauvais reessais")



    @classmethod
    def ajouter_mouvement_disponible(cls,nom:str, description:str):
        Exercice.mouvements[nom] = description




    def __str__(self):
        return f"nom de l'exercice : {self.nomexercice} "

