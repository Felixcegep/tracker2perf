from Exercice import Exercice
# Todo: changer les methode d'instance pour avor le format
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire
class ExerciceMusculation(Exercice):
    def __init__(self, nomexercice :str,rpe:int,set:int,rep:int,poid_kg:int):
        super().__init__(nomexercice)
        self.nomexercice = nomexercice
        self.rpe = rpe
        self.set = set
        self.rep = rep
        self.poid_kg = poid_kg
    @property
    def rpe(self):
        return self._rpe
    @rpe.setter
    def rpe(self,rpe):
        if 0 < rpe <=10:
            self._rpe = rpe
        else:
            raise ValueError("rpe doit etre dans la range de 1 a 10")
    @property
    def set(self):
        return self._set
    @set.setter
    def set(self,set):
        if 0 < set <=10:
            self._set = set
        else:
            raise ValueError("set doit etre entre la range de 1 a 10")
    @property
    def rep(self):
        return self._rep
    @rep.setter
    def rep(self,rep):
        if 0 < rep <=25:
            self._rep = rep
        else:
            raise ValueError("rep doit etre entre la range de 1 a 25")
    @property
    def poid_kg(self):
        return self._poid_kg
    @poid_kg.setter
    def poid_kg(self,poid_kg):
        if 0 < poid_kg <=500:
            self._poid_kg = poid_kg
        else:
            raise ValueError("le poid doit etre entre la range de 1 a 500 kg")

    def __str__(self):
        return f"nom : {self.nomexercice}, rpe : {self.rpe}, set : {self.set}, rep : {self.rep}, poid : {self.poid} kg"