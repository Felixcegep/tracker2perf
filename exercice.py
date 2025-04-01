    # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
class Exercice:
    mouvement = {
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

    def __init__(self, nomexercice:str, rpe:int, set : int ,  rep : int,   poid: int,cardio:bool=False,  temps: int = None):
        if nomexercice in Exercice.mouvement:

            self.nomexercice = nomexercice
        else:
            print("exercice invalide veuillez l'ajouter a liste d'exercices")
        self.rpe = rpe
        self.rep = rep
        self.set = set
        self.poid = poid
        self.temps = temps
        self.cardio = cardio


    @classmethod
    def ajouter_mouvement(cls,nom:str, description:str):
        Exercice.mouvement[nom] = description




    def __str__(self):
        if self.temps == None:
            return f"{self.nomexercice} rpe {self.rpe} set {self.set} rep {self.rep} poid {self.poid}"
        else:
            return f"{self.nomexercice} rpe {self.rpe} set {self.set}  rep {self.rep} poid {self.poid} temps {self.temps}"

