from seance import Seance
from exercice import Exercice
from journee import Journee
from genre import Genre
import datetime
import enum

class Utilisateur:
    nombre_utilisateur = 0
    def __init__(self, nom : str,taille: int, age: int, poid:float,genre:str):
        self.nom = nom
        self.taille = taille
        self.age = age
        self.poid = poid
        if genre in [g.value for g in Genre]:
            self.genre = genre
        else:
            raise ValueError("genre invalide") 
        self.personal_record = {
            }

        Utilisateur.nombre_utilisateur += 1




    @classmethod
    def afficher_total_utilisateur(cls):
        print(cls.nombre_utilisateur)

    def __str__(self):
        return f"Nom : {self.nom}\ntaille : {self.taille}\nage:  {self.age} \npoid: {self.poid} lbs"

if __name__ == '__main__':
    test = Utilisateur("test", 150,19 ,60,"homme")