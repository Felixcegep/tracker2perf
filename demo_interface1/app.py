import sys
import os
import pickle
from PySide6.QtWidgets import ( QApplication, QMainWindow, QMessageBox, QLabel,
                                QScrollArea, QWidget, QVBoxLayout, QLineEdit # Added QLineEdit
                              )
from PySide6.QtCore import Qt, Signal
from demo_interface1.creationcompte import creationcompte
# Make sure these imports point to the correct UI definitions if they are separate files
# Assuming dashboard_ui.py contains the definition for the Dashboard UI class
from demo_interface1.dashboard_ui import Dashboard
from demo_interface1.journee_ui import Journee_ui
from Journeemodif_ui import Journeemodif

# --- Keep your existing classes: exercice, journeetest, utilisateur, ClickableLabel ---
class exercice:
    def __init__(self,exercice):
        self.exercice = exercice

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
    labelClicked = Signal(str)

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("padding: 8px; border: 1px solid gray; border-radius: 5px; background-color: #e0e0e0;")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        print(f"Label clicked: {self.text()}")
        print(f"'{self.text()}' label clicked. Emitting signal...")
        self.labelClicked.emit(self.text())

# --- Keep Journeemodif_window ---
class Journeemodif_window(QMainWindow):
    def __init__(self, label_text=None):
        super().__init__()
        self.ui = Journeemodif()
        self.ui.setupUi(self)
        # Load data safely
        try:
            with open("creationcompte.pkl", "rb") as f:
                self.creationcompte = pickle.load(f)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "creationcompte.pkl not found!")
            self.close()
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
            self.close()
            return

        if label_text is not None:
            self.ui.info.setText(label_text) # Assuming 'info' is a QLabel or similar in Journeemodif UI
            # Ensure 'supprimer' button exists in Journeemodif UI
            if hasattr(self.ui, 'supprimer'):
                 self.ui.supprimer.clicked.connect(lambda: self.go_todashboard(label_text))
            else:
                print("Warning: 'supprimer' button not found in Journeemodif UI.")

    def go_todashboard(self,label_text):
        print("Current list:", [j.nom for j in self.creationcompte.journee])
        print("Element to remove:", label_text)

        found = False
        for journee in self.creationcompte.journee:
            if journee.nom == label_text:
                self.creationcompte.journee.remove(journee)
                found = True
                print(f"'{journee.nom}' found and removed.")
                break # Exit loop once found and removed

        if not found:
             print(f"Warning: '{label_text}' not found in the list.")
             # Optionally show a message to the user
             QMessageBox.warning(self, "Not Found", f"Journey '{label_text}' was not found.")
             # Still proceed to save and reopen dashboard if needed, or handle differently
             # return # Or maybe don't proceed if not found? Depends on desired logic.


        # Save the updated data
        try:
            with open("creationcompte.pkl", "wb") as f:
                pickle.dump(self.creationcompte, f)
            print("Data saved successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")
            # Decide if you still want to open the dashboard
            # return

        # Open the dashboard
        self.dashboard_window = dashboard_window()
        self.dashboard_window.show()
        self.close()


# --- MODIFIED dashboard_window ---
class dashboard_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Dashboard()
        self.ui.setupUi(self)

        # --- Central Widget and Layout Setup ---
        # Create a central widget if your UI file doesn't define one properly
        # or if you want to manage layout programmatically here.
        # If dashboard_ui.setupUi already sets a central widget with a layout,
        # you might need to get that layout instead of creating a new one.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget) # Layout for the central widget

        # --- Add Search Bar ---
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search Journées...")
        self.search_bar.textChanged.connect(self.filter_journees) # Connect signal
        main_layout.addWidget(self.search_bar) # Add search bar to the top

        # --- Add existing UI elements to the layout ---
        # Add the user name label (assuming it's self.ui.nom)
        # You might need to reparent it if setupUi assigned it elsewhere
        if hasattr(self.ui, 'nom'):
             main_layout.addWidget(self.ui.nom)
        else:
            # Add a default label if 'nom' isn't in the UI file
            self.ui.nom = QLabel("User Name Placeholder")
            main_layout.addWidget(self.ui.nom)

        # Add the scroll area (self.ui.listejourney)
        # Ensure listejourney is correctly initialized by setupUi
        if not hasattr(self.ui, 'listejourney') or not isinstance(self.ui.listejourney, QScrollArea):
             print("Warning: self.ui.listejourney is not a QScrollArea. Creating one.")
             self.ui.listejourney = QScrollArea()
             self.ui.listejourney.setWidgetResizable(True)
             scroll_content = QWidget()
             scroll_layout = QVBoxLayout(scroll_content)
             scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop) # Align items to top
             self.ui.listejourney.setWidget(scroll_content)

        # Ensure the scroll area's widget has a layout
        if self.ui.listejourney.widget() is None:
             scroll_content = QWidget()
             scroll_layout = QVBoxLayout(scroll_content)
             scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
             self.ui.listejourney.setWidget(scroll_content)
        elif self.ui.listejourney.widget().layout() is None:
             scroll_layout = QVBoxLayout(self.ui.listejourney.widget())
             scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        main_layout.addWidget(self.ui.listejourney) # Add scroll area below search bar

        # Add the 'Aller' button (self.ui.aller)
        if hasattr(self.ui, 'aller'):
             self.ui.aller.clicked.connect(self.allerjournee)
             main_layout.addWidget(self.ui.aller)
        else:
            print("Warning: 'aller' button not found in Dashboard UI.")
            # Optionally create a default button if needed

        # --- Load Data ---
        try:
            with open("creationcompte.pkl", "rb") as f:
                self.creationcompte = pickle.load(f)
            print("Loaded journées:", [j.nom for j in self.creationcompte.journee])
            self.ui.nom.setText(self.creationcompte.nom)
        except FileNotFoundError:
             QMessageBox.critical(self, "Error", "creationcompte.pkl not found!")
             # Handle error appropriately, maybe disable functionality or close
             self.creationcompte = None # Indicate data couldn't be loaded
        except Exception as e:
             QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
             self.creationcompte = None

        # --- Populate Scroll Area ---
        if self.creationcompte: # Only populate if data loaded successfully
             self.afficher_elements_scrollbar()

    def afficher_elements_scrollbar(self):
        # Get the layout inside the scroll area's widget
        scroll_layout = self.ui.listejourney.widget().layout()

        # --- Clear existing labels before adding new ones (important for refresh) ---
        # This avoids duplicates if this function is called multiple times
        while scroll_layout.count():
            item = scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater() # Delete the widget

        # --- Add labels for each journee ---
        if not self.creationcompte.journee:
             print("No journées to display.")
             # Optionally add a placeholder label
             placeholder = QLabel("No journeys created yet.")
             placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
             scroll_layout.addWidget(placeholder)
             return # Exit if no journeys

        print(f"Displaying {len(self.creationcompte.journee)} journées.")
        for jour in reversed(self.creationcompte.journee): # Show newest first
            label = ClickableLabel(str(jour.nom))
            # Stylesheet moved to ClickableLabel constructor
            # label.setStyleSheet("padding: 10px; border: 1px solid #aaa; border-radius: 5px;")
            scroll_layout.addWidget(label) # Add to the scroll area's layout
            label.labelClicked.connect(self.handle_label_click)

    def filter_journees(self):
        """ Hides/shows labels in the scroll area based on search bar text. """
        search_text = self.search_bar.text().strip().lower() # Get search text, lowercase
        scroll_layout = self.ui.listejourney.widget().layout()

        # Iterate through the widgets in the layout
        for i in range(scroll_layout.count()):
            item = scroll_layout.itemAt(i)
            widget = item.widget()

            # Make sure it's one of our ClickableLabels
            if isinstance(widget, ClickableLabel):
                label_text = widget.text().lower()
                # Hide if search text is not empty and not found in label text
                # Show otherwise (if search is empty or text is found)
                if search_text and search_text not in label_text:
                    widget.hide()
                else:
                    widget.show()
            elif isinstance(widget, QLabel) and widget.text() == "No journeys created yet.":
                # Hide the placeholder if we are searching and there are results
                # (or if the list wasn't empty initially)
                # This logic might need refinement depending on exact behavior desired
                pass # Keep placeholder visible/hidden based on initial list state + filter


    def handle_label_click(self, label_text):
        print(f"Dashboard received click from: {label_text}")
        self.Journeemodif = Journeemodif_window(label_text)
        self.Journeemodif.show()
        self.close()

    def allerjournee(self):
        self.Journee = Journee()
        self.Journee.show()
        self.close()

# --- Keep Journee class ---
class Journee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Journee_ui()
        self.ui.setupUi(self)
        try:
            with open("creationcompte.pkl", "rb") as f:
                self.creationcompte = pickle.load(f)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "creationcompte.pkl not found!")
            self.close() # Or handle differently
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
            self.close() # Or handle differently
            return

        # Ensure pushButton exists
        if hasattr(self.ui, 'pushButton'):
            self.ui.pushButton.clicked.connect(self.bouton_clicker)
        else:
            print("Warning: 'pushButton' not found in Journee UI.")


    def bouton_clicker(self):
        # Ensure 'nom' QLineEdit exists
        if not hasattr(self.ui, 'nom') or not hasattr(self.ui.nom, 'text'):
             QMessageBox.warning(self, "Error", "UI element 'nom' not found.")
             return

        journee_name = self.ui.nom.text().strip()
        if not journee_name:
            QMessageBox.warning(self, "Input Error", "Journey name cannot be empty.")
            return

        # Check for duplicates (optional but good practice)
        if any(j.nom == journee_name for j in self.creationcompte.journee):
             QMessageBox.warning(self, "Duplicate", f"A journey named '{journee_name}' already exists.")
             return

        test = journeetest(journee_name)
        self.creationcompte.ajouter_journee(test)

        try:
            with open("creationcompte.pkl", "wb") as f:
                pickle.dump(self.creationcompte, f)
            print(f"Journey '{journee_name}' added and saved.")
            self.go_todashboard()
        except Exception as e:
             QMessageBox.critical(self, "Error", f"Failed to save data: {e}")


    def go_todashboard(self):
        self.dashboard_window = dashboard_window()
        self.dashboard_window.show()
        self.close()


# --- Keep CreateAccount class ---
class CreateAccount(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = creationcompte()
        self.ui.setupUi(self)
         # Ensure pushButton exists
        if hasattr(self.ui, 'pushButton'):
            self.ui.pushButton.clicked.connect(self.create_account)
        else:
            print("Warning: 'pushButton' not found in CreateAccount UI.")


    def create_account(self):
        # Safer access to UI elements
        nom = self.ui.nom.text().strip() if hasattr(self.ui, 'nom') else ""
        taille = self.ui.taille.text().strip() if hasattr(self.ui, 'taille') else ""
        poid = self.ui.poid.text().strip() if hasattr(self.ui, 'poid') else ""
        age = self.ui.age.text().strip() if hasattr(self.ui, 'age') else ""
        genre = self.ui.genre.text().strip() if hasattr(self.ui, 'genre') else ""


        if not nom:
            self.show_popup_message("Input Error", "The name cannot be empty!")
            return
        # Add more validation if needed (e.g., check if taille, poid, age are numbers)

        try:
            # Création de l'objet utilisateur
            nouvel_utilisateur = utilisateur(nom, taille, poid, age, genre)
            with open('creationcompte.pkl', 'wb') as file:
                pickle.dump(nouvel_utilisateur, file)
            print("Utilisateur sauvegarder:", nouvel_utilisateur.nom)

            self.go_todashboard()

        except ValueError as ve: # Catch specific error from utilisateur setter
             self.show_popup_message("Validation Error", str(ve))
        except Exception as e:
             self.show_popup_message("Error", f"Failed to create account: {e}")


    def go_todashboard(self):
        self.dashboard_window = dashboard_window()
        self.dashboard_window.show()
        self.close()

    def show_popup_message(self, title, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning) # Use Warning or Information, Critical is usually for errors
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

# --- Main execution block ---
if __name__ == "__main__":
    app = QApplication(sys.argv)

    if os.path.exists("creationcompte.pkl"):
        window = dashboard_window()
    else:
        window = CreateAccount()

    window.show()
    sys.exit(app.exec())