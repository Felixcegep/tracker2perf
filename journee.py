from seance import Seance
from exercice import Exercice
from datetime import datetime

class Journee:
    def __init__(self,nom, date : datetime):
        self.nom = nom
        self.seances_ajourdhui = []
        if datetime.now() > date:
            self.date = date
        else:
            raise ValueError("date ne peux pas etre dans le futur")
        self.date_creation = datetime.today()

    def ajouter_seance(self, seance: Seance):
        self.seances_ajourdhui.append(seance)

    def afficher_exercice(self):
        for exercices in self.seances_ajourdhui:
            for exercice in exercices.exercice_seaces:
                print(exercice.nomexercice)
   # TODO: ajouter une vérification de date dans le format datetime



