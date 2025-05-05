from .Exercice import Exercice
from .ExerciceCardio import ExerciceCardio
from .ExerciceMusculation import ExerciceMusculation



class Seance:
    nbseancetotal = 0
    def __init__(self, nom: str, temps: float):
        self.nom = nom
        self.temps = temps
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

    def volume_par_seance(self):
        """
        calcule le nombre total du volume de la seance a passant a travers chaque exercice et allant chercher
        la propriété du volume de chaque exercice
        :return:
        """
        total_volume = 0
        for exercice in self.exercice_seaces:
            if isinstance(exercice, ExerciceMusculation):
                total_volume += exercice.volume
        return total_volume

    def afficher_exercices(self):
        """
        print chaque exercice dans la seance avec un compteurs de position
        :return: None
        """
        if len(self.exercice_seaces) == 0:
            return "il n'y a pas d'exercice dans cette seance"
        else:
            compteur = 0
            for exercice in self.exercice_seaces:
                print(compteur, ":", exercice.nomexercice)
                compteur += 1

    def ajouter_exercice(self, exercice: ExerciceMusculation | ExerciceCardio) -> Exercice:
        """
        ajouter des exercice a la propriete liste de la seance
        :param exercice:
        :return: None
        """
        if isinstance(exercice, ExerciceCardio) or isinstance(exercice, ExerciceMusculation):
            self.exercice_seaces.append(exercice)
        else:
            raise ValueError("exercice n'est pas un ExerciceMusculation ou ExerciceCardio")

    def supprimer_exercice(self, nom_exercice: str):
        """
        supprime exercice de la seance
        :param nom_exercice:
        :return: None
        """
        for exercice in self.exercice_seaces:
            if exercice.nomexercice == nom_exercice:
                self.exercice_seaces.remove(exercice)
                break

    def afficher_total_exercice(self):
        """
        retourne le nombre d'exercice dans la seance
        :return: Seance.nbseancetotal
        """
        return Seance.nbseancetotal

    def __str__(self):
        return f'{self.nom} {self.exercice_seaces}'
