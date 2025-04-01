from seance import Seance
from exercice import Exercice
from journee import Journee
from genre import Genre
from datetime import datetime
import enum

class Utilisateur:
    nombre_utilisateur = 0
    def __init__(self, nom : str,taille: int, age: int, poid:float,genre:str):
        self.nom = nom
        self.taille = taille
        self.age = age
        self.poid = poid
        self.journee = []
        if genre in [g.value for g in Genre]:
            self.genre = genre
        else:
            raise ValueError("genre invalide") 
        self.personal_record = {
            }

        Utilisateur.nombre_utilisateur += 1

    def ajouter_journee(self, journee:Journee):
        self.journee.append(journee)





    @classmethod
    def afficher_total_utilisateur(cls):
        print(cls.nombre_utilisateur)

    def __str__(self):
        return f"Nom : {self.nom}\ntaille : {self.taille}\nage:  {self.age} \npoid: {self.poid} lbs"

if __name__ == '__main__':
    joueur1 = Utilisateur("test", 150,19 ,60,"homme")
    # création de d'exercice
    x = datetime(2020, 5, 17)
    Exercice1 = Exercice("bench", 5, 5, 5, 50, )
    # création de séance
    seance1 = Seance("push")
    seance1.ajouterExercice(Exercice1)
    #
    ajourdhui = Journee("yooo", x)
    ajourdhui.ajouter_seance(seance1)
    ajourdhui.afficher_exercice()