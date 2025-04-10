import sys
import os
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QScrollArea, \
    QWidget, QVBoxLayout  # Corrected the import
from PySide6.QtCore import Qt, Signal
from demo_interface1.creationcompte import creationcompte
from demo_interface1.dashboard_ui import Dashboard
from demo_interface1.journee_ui import Journee_ui
from Journeemodif_ui import Journeemodif
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


class ClickableLabel(QLabel):
    """
    A QLabel subclass that emits a 'labelClicked' signal
    with its text when clicked.
    """
    # --- Define the signal using PySide6.QtCore.Signal ---
    print("pour les bouton dans les choix de classe scrollable")

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        # couleurs pour differencier
        self.setStyleSheet("padding: 8px; border: 1px solid gray; border-radius: 5px; background-color: #e0e0e0;")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCursor(Qt.CursorShape.PointingHandCursor) # Indicate it's clickable

    def mousePressEvent(self, event):
        print(f"Label clicked: {self.text()}")
        print(f"'{self.text()}' label clicked. Emitting signal...")
        self.Journeemodif = Journeemodif_window(self.text())
        self.Journeemodif.show()
        self.close()

class Journeemodif_window(QMainWindow):
    def __init__(self, label_text=None):
        super().__init__()
        self.ui = Journeemodif()
        self.ui.setupUi(self)
        if label_text != None:
            self.ui.info.setText(label_text)


class dashboard_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.journee = ["yes","non"]
        self.ui = Dashboard()  # Instantiate the UI class from second_ui.py
        self.ui.setupUi(self)  # Setup the UI
        self.ui.aller.clicked.connect(self.allerdashboard)

        with open("creationcompte.pkl", "rb") as f:
            self.creationcompte = pickle.load(f)
        print(self.creationcompte.journee)
        self.ui.nom.setText(self.creationcompte.nom)

        # passer a travers la liste journee
        # recharge et le plus recent ajouter en haut avec reversed liste
        for jour in reversed(self.creationcompte.journee):
            label = ClickableLabel(str(jour))  # Tu peux personnaliser ici
            label.setStyleSheet("padding: 10px; border: 1px solid #aaa; border-radius: 5px;")
            # selection le widget et le layout. puis cree un widget(label)
            self.ui.listejourney.widget().layout().addWidget(label)


    def allerdashboard(self):
        self.Journee = Journee()
        self.Journee.show()
        self.close()

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
        self.close()
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
            return

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
    # chatgpt explication message erreur
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
