from exercicesvalide import Exercicesvalide
    # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
class Exercice:
    def __init__(self, nomexercice:str, rpe:int, set : int ,  rep : int,   poid: int,  temps: int = None):
        if nomexercice in [e.value for e in Exercicesvalide]:
            self.nomexercice = nomexercice
        else:
            raise ValueError("exercice invalide")
        self.nomexercice = nomexercice
        self.rpe = rpe
        self.rep = rep
        self.set = set
        self.poid = poid
        self.temps = temps





    def __str__(self):
        if self.temps == None:
            return f"{self.nomexercice} rep {self.rep} poid {self.poid}"
        else:
            return f"{self.nomexercice} rep {self.rep} poid {self.poid} temps {self.temps}"

