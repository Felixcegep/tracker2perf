from Exercice import Exercice
from ExerciceCardio import ExerciceCardio
from ExerciceMusculation import ExerciceMusculation

#TODO : ajouter la logique de volume de la seance
# Todo: faire des test unitaire
class Seance:
    nbseancetotal = 0
    def __init__(self, nom : str):
        self.nom = nom
        self.exercice_seaces = []
        Seance.nbseancetotal += 1

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, nom):
        if len(nom) > 0:
            self._nom = nom
        else:
            raise ValueError("le nom de la seance ne peut pas etre vide")


    def afficher_exercices(self):
        if len(self.exercice_seaces) == 0:
            return "il n'y a pas d'exercice dans cette seance"
        else:
            compteur = 0
            for exercice in self.exercice_seaces:
                print(compteur, ":", exercice.nomexercice)
                compteur += 1

    def ajouter_exercice(self, exercice:ExerciceMusculation):
        if isinstance(exercice, ExerciceCardio) or isinstance(exercice, ExerciceMusculation):
            self.exercice_seaces.append(exercice)
        else:
            raise ValueError("exercice n'est pas un ExerciceMusculation ou ExerciceCardio")
    def supprimer_exercice(self, nom_exercice:str):
        for exercice in self.exercice_seaces:
            if exercice.nomexercice == nom_exercice:
                self.exercice_seaces.remove(exercice)
                break
    def afficher_total_exercice(self):
        return Seance.nbseancetotal
    
    
    def __str__(self):
        return f'{self.nom} {self.exercice_seaces}'
