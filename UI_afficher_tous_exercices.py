import pickle

from PySide6.QtWidgets import QDialog

from UI_folder import Ui_AvailableExercisesDialog


class afficher_tous_exercice(QDialog):
    #ajouter les erreur possible
    def __init__(self):
        super().__init__()
        self.ui = Ui_AvailableExercisesDialog()
        self.ui.setupUi(self)
        self.ui.availableExercisesList.clear()
        self.afficher_exercice()

    def afficher_exercice(self):
        liste_exercices = []
        with open("mouvement_disponible.pkl", "rb") as f:
            mouvement_disponible = pickle.load(f)

        for exercice in mouvement_disponible.keys():
            print(exercice)
            liste_exercices.append(exercice)
        self.ui.availableExercisesList.addItems(liste_exercices)