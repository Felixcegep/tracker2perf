from seance import Seance
from exercice import Exercice
import datetime

class Journee:
    def __init__(self, date):
        self.seances_ajourdhui = []
        self.date = date
        self.date_creation = datetime.date.today()

    def ajouter_seance(self, seance: Seance):
        self.seances_ajourdhui.append(seance)
    def afficher_exercice(self):
        for exercices in ajourdhui.seances_ajourdhui:
            for exercice in exercices.exercice_seaces:
                print(exercice.nomexercice)



if __name__ == '__main__':
    Exercice1 = Exercice("bench", 5, 5, 50)
    Exercice2 = Exercice("dips", 5, 5, 50)
    seance1 = Seance("push")
    seance1.ajouterExercice(Exercice1)
    seance1.ajouterExercice(Exercice2)

    ajourdhui = Journee("aujourdhui")
    ajourdhui.ajouter_seance(seance1)
    ajourdhui.afficher_exercice()


