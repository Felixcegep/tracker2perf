from Exercice import Exercice

#TODO  finir verification exercicecardio disponible depuis le fichier Mouvementdisponible
class ExerciceCardio(Exercice):
    def __init__(self, nom_exercice:str,duree:int,distance:float,intensite : int):
        super().__init__(nom_exercice)
        self.duree = duree
        self.intensite = intensite
        self.distance = distance

    @property
    def intensite(self):
        return self._intensite

    @intensite.setter
    def intensite(self, intensite):
        if 0 < intensite <= 10:
            self._intensite = intensite
        else:
            raise ValueError("intensite doit etre entre 1 et 10")

    @property
    def distance(self):
        return self._distance
    @distance.setter
    def distance(self, distance):
        if distance <= 0:
            raise ValueError("la distance doit etre positive")
        else:
            self._distance = distance

    @property
    def duree(self):
        return self._duree
    @duree.setter
    def duree(self, duree):
        if duree <= 0:
            raise ValueError("la duree doit etre positive")
        else:
            self._duree = duree

    def __str__(self):
        return f'nom :{self.nomexercice} duree : {self._duree} intensite : {self.intensite} distances : {self.distance}'

