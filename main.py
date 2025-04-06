from ExerciceMusculation import ExerciceMusculation
from Seance import Seance
from datetime import datetime
from Journee import Journee
from Utilisateur import Utilisateur
from Exercice import Exercice


if __name__ == '__main__':

    joueur1 = Utilisateur("test", 150,19 ,60,"homme")
    # création de d'exercice
    datedeseance = datetime(2005, 2, 7)
    day1 = Journee("nom", datedeseance)
    day2 = Journee("nom", datedeseance)

# seance

    seance1 = Seance("seance1")
# exercice

    Exercice1 = ExerciceMusculation("test", 1,1,2,3)
    Exercice2 = ExerciceMusculation("Presse à cuisses", 1,1,2,3)

# ajouter seance
    seance1.ajouter_exercice(Exercice1)
    seance1.ajouter_exercice(Exercice2)
    
# jours
    day1.ajouter_seance(seance1)
    joueur1.ajouter_journee(day1)

# user
