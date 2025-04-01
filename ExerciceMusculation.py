from Exercice import Exercice
# Todo: changer les methode d'instance pour avor le format

class ExerciceMusculation(Exercice):
    def __init__(self, nomexercice :str,rpe:int,set:int,rep:int,poid:int):
        super().__init__(nomexercice)
        self.nomexercice = nomexercice
        self.rpe = rpe
        self.set = set
        self.rep = rep
        self.poid = poid

    def __str__(self):
        return f"nom : {self.nomexercice} rpe : {self.rpe} set : {self.set} rep : {self.rep} poid : {self.poid}"