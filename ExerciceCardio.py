from Exercice import Exercice

# Todo: changer les methode d'instance pour avor le format
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire
class ExerciceCardio(Exercice):
    # verifier mouvements disponible cardio 
    def __init__(self, nom_exercice:str,duree:int,intensite:str,distance:float):
        super().__init__(nom_exercice)
        self.duree = duree
        self.intensite = intensite
        self.distance = distance

    def __str__(self):
        return f'nom :{self.nomexercice} duree : {self.duree} intensite : {self.intensite} distances : {self.distance}'

test = ExerciceCardio("squat",9,"dure",9)
print(test)