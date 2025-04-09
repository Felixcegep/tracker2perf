import sys
import os
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from demo_interface1.creationcompte import creationcompte
from demo_interface1.dashboard_ui import Dashboard
from demo_interface1.journee_ui import Journee_ui

class journeetest:
    def __init__(self,nom):
        self.nom = nom

class utilisateur():
    def __init__(self, nom, taille, poid, age, genre):
        self.nom = nom  # This will call the setter
        self.taille = taille
        self.poid = poid
        self.age = age
        self.genre = genre
        self.journee = []
    def ajouter_journee(self,journeetest):
        self.journee.append(journeetest)

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        if nom == "":  # Check if the name is empty
            raise ValueError("Nom cannot be empty")
        else:
            self._nom = nom  # Set the private attribute _nom

class dashboard_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Dashboard()  # Instantiate the UI class from second_ui.py
        self.ui.setupUi(self)  # Setup the UI
        self.ui.aller.clicked.connect(self.allerdashboard)
        with open("creationcompte.pkl", "rb") as f:
            self.creationcompte = pickle.load(f)
        print(self.creationcompte.journee)
        self.ui.nom.setText(self.creationcompte.nom)
    def allerdashboard(self):
        self.Journee = Journee()
        self.Journee.show()

class Journee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Journee_ui()  # Instantiate the UI class from second_ui.py
        self.ui.setupUi(self)  # Setup the UI
        with open("creationcompte.pkl", "rb") as f:
            self.creationcompte = pickle.load(f)
        self.ui.pushButton.clicked.connect(self.bouton_clicker)

    def bouton_clicker(self):

        test = journeetest(self.ui.nom.text())

        self.creationcompte.ajouter_journee(test)
        with open("creationcompte.pkl", "wb") as f:
            pickle.dump(self.creationcompte, f)
        self.go_todashboard()

    def go_todashboard(self):
        self.dashboard_window = dashboard_window()
        self.dashboard_window.show()
class CreateAccount(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = creationcompte()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.create_account)

    def create_account(self):
        nom = self.ui.nom.text()
        taille = self.ui.taille.text()
        poid = self.ui.poid.text()
        age = self.ui.age.text()
        genre = self.ui.genre.text()

        if not nom:  # This checks if 'nom' is empty or None
            self.show_popup_message("This is wrong", "The name cannot be empty!")
            return  # Stop further execution if the name is invalid

        else:

            # Création de l'objet utilisateur
            nouvel_utilisateur = utilisateur(nom, taille, poid, age, genre)
            with open('creationcompte.pkl', 'wb') as file:
                pickle.dump(nouvel_utilisateur, file)
            # Optionnel : afficher ou stocker l'objet
            print("Utilisateur sauvegarder :", nouvel_utilisateur.nom, nouvel_utilisateur.taille, nouvel_utilisateur.poid, nouvel_utilisateur.age, nouvel_utilisateur.genre)
            if os.path.exists("creationcompte.pkl"):
                print("user is created")
                self.go_todashboard()

    def go_todashboard(self):
        self.dashboard_window = dashboard_window()
        self.dashboard_window.show()

    def show_popup_message(self, title, message):
        # Display a popup message box with a title and message
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)  # Set icon to 'critical' for errors
        msg.setWindowTitle(title)  # Set the window title
        msg.setText(message)  # Set the message passed as parameter
        msg.setStandardButtons(QMessageBox.Ok)  # Add 'Ok' button
        msg.exec_()  # Show the message box as a popup

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if os.path.exists("creationcompte.pkl"):
        window = dashboard_window()
    else:
        window = CreateAccount()

    window.show()
    sys.exit(app.exec())
