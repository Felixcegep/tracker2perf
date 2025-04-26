import pickle

from PySide6.QtWidgets import QDialog

from UI_folder import Ui_AvailableNourritureDialog


class afficher_tous_aliments(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AvailableNourritureDialog()
        self.ui.setupUi(self)
        self.ui.availableExercisesList.clear()
        self.afficher_aliment()
    def afficher_aliment(self):
        liste_aliments = []
        with open("aliment_disponible.pkl", "rb") as f:
            aliment_disponible = pickle.load(f)
        for aliment in aliment_disponible.keys():
            print(aliment)
            liste_aliments.append(aliment)
        self.ui.availableExercisesList.addItems(liste_aliments)