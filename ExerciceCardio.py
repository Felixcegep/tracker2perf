from exercice import Exercice


class ExerciceCardio(Exercice):
    def __init__(self, nomexercice:str,duree:int,intensite:str,distance:int):
        super().__init__(nomexercice)
        self.duree = duree
        self.intensite = intensite
        self.distance = distance

    def __str__(self):
        return f'nom :{self.nomexercice} duree : {self.duree} intensite : {self.intensite} distances : {self.distance}'