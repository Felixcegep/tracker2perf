from Seance import Seance
from Exercice import Exercice
from Journee import Journee
from Genre import Genre
from datetime import datetime
import pickle
import enum
from ExerciceCardio import ExerciceCardio
from ExerciceMusculation import ExerciceMusculation
# Todo: changer les methode d'instance pour avor le format
# Todo: ajout de jsonpickle pour sauvegarder les progrès de l'utilisateur
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire

class Utilisateur:
    nombre_utilisateur = 0
    def __init__(self, nom : str,taille: int, age: int, poid:float,genre:str):
        self.nom = nom
        self.taille = taille
        self.age = age
        #Todo : tracker le poid de l'utilisateur lorsqu'il change avec la date
        self.poid = poid
        self.historique_journee = []

        self.genre = genre

        self.personal_record = {

                }

        Utilisateur.nombre_utilisateur += 1

    def ajouter_journee(self, journee:Journee):
        self.historique_journee.append(journee)
        #TODO : ajouter pr dans lors de ajouter journee





    @classmethod
    def afficher_total_utilisateur(cls):
        print(cls.nombre_utilisateur)

    def __str__(self):
        return f"Nom : {self.nom}\ntaille : {self.taille}\nage:  {self.age} \npoid: {self.poid} lbs"

if __name__ == '__main__':

    joueur1 = Utilisateur("test", 150,19 ,60,"homme")
    # création de d'exercice
    datedeseance = datetime(2005, 2, 7)
    day1 = Journee("nom", datedeseance)
    day2 = Journee("nom", datedeseance)

# seance

    seance1 = Seance("seance1")
    seance2 = Seance("seance2")
# exercice

    Exercice1 = ExerciceMusculation("test1", 1,1,2,3)
# ajouter seance
    seance1.ajouter_exercice(Exercice1)
# jours
    day1.ajouter_seance(seance1)

# user
    joueur1.ajouter_journee(day1)