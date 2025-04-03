from Exercice import Exercice
# Todo: changer les methode d'instance pour avor le format
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire
class ExerciceMusculation(Exercice):
    def __init__(self, nomexercice :str,rpe:int,set:int,rep:int,poid:int):
        super().__init__(nomexercice)
        self.nomexercice = nomexercice
        self.rpe = rpe
        self.set = set
        self.rep = rep
        self.poid = poid
    @property
    def rpe(self):
        return self._rpe
    @rpe.setter
    def rpe(self,rpe):
        if 0 < rpe <=10:
            self._rpe = rpe
        else:
            raise ValueError("rpe doit etre dans la range de 1 a 10")


    def __str__(self):
        return f"nom : {self.nomexercice}, rpe : {self.rpe}, set : {self.set}, rep : {self.rep}, poid : {self.poid} kg"

