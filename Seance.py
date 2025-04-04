from Exercice import Exercice
from ExerciceCardio import ExerciceCardio
from ExerciceMusculation import ExerciceMusculation


# Todo: changer les methode d'instance pour avor le format
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire
class Seance:
    nbseancetotal = 0
    def __init__(self, nom : str):
        self.nom = nom
        self.exercice_seaces = []
        Seance.nbseancetotal += 1

    def afficher_exercices(self):
        for exercice in self.exercice_seaces:
            print(exercice.nomexercice)

    def ajouter_exercice(self, exercice:ExerciceMusculation):
        if isinstance(exercice, ExerciceCardio) or isinstance(exercice, ExerciceMusculation):
            self.exercice_seaces.append(exercice)
        else:
            raise ValueError("exercice n'est pas un ExerciceMusculation ou ExerciceCardio")
