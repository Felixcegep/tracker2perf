import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pickle

from UI_folder import Ui_dashboard, Ui_DayView
from graphic_utilisateur import GraphicUtilisateur

#graphique
goodgraph = GraphicUtilisateur()
#info de l'utilsateur
info_utilisateur = goodgraph.info

class journeemodif(QWidget):
    def __init__(self,journee_specifique=None):
        super().__init__() # Call the QWidget constructor

        # Create an instance of the UI generated class
        self.ui = Ui_DayView()

        # Call the setupUi method from the generated class,
        # passing 'self' (the QWidget instance) as the argument.
        # This populates the QWidget with the UI elements.
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.retourner_dashboard)

        #bouton exercice et affichage
        self.ui.exercisesList
        self.ui.addExerciseButton
        self.ui.removeExerciseButton.clicked.connect(self.supprimer_exercices)
        #
        #trouver l'index de la journee dans la liste

        if journee_specifique:
            for index, journee in enumerate(info_utilisateur.historique_journee):
                formatted_date = journee.date.strftime("%m/%d/%Y")
                if journee_specifique == formatted_date:
                    index_valide = index  # Store the index of the first match

                    break
        self.afficher_exercices(index_valide)
    #TODO : def exercices pas terminer :(
    def afficher_exercices(self,index_valide):
        self.ui.exercisesList.clear()

        exercice_liste_scrollbar = []
        for exercice in info_utilisateur.historique_journee[index_valide].obtenir_exercices_info():
            exercice_liste_scrollbar.append(exercice["nom"])

        self.ui.exercisesList.addItems(exercice_liste_scrollbar)
    def supprimer_exercices(self,index_valide):

        element_selectionner = self.ui.exercisesList.currentItem()
        if element_selectionner is not None:
            #ajouter une pop up avant de supprimer pour assurer que c'est correcte
            print(element_selectionner.text())
            self.afficher_exercices(index_valide)
        else:
            print("No item selected.")



    def retourner_dashboard(self):
        self.aller_dashboad = Dashboard()
        self.aller_dashboad.show()
        self.close()
class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        #bouton dispo
        self.button7Days =self.ui.button7Days
        self.button30Days = self.ui.button30Days
        self.depuis_debut = self.ui.buttonSinceStart
        self.ui.button7Days.clicked.connect(self.set_filter_7_days)
        self.ui.button30Days.clicked.connect(self.set_filter_30_days)  # Use .connect()
        self.ui.buttonSinceStart.clicked.connect(self.set_filter_365_days)
        #
        self.ui.searchLineEdit.textChanged.connect(self.filtrer_journees)
        self.ui.ajouterjournee.clicked.connect(self.ajouter_journee)
        self.ui.listejourney.itemClicked.connect(self.selection_scrollbar)

        #welcome en haut a droit
        welcometext = self.ui.welcomeLabel
        # ouvrir fichier compte

        self.creationcompte = info_utilisateur
        # afficher le salut a l'utilisateur
        welcometext.setText("bienvenue " + self.creationcompte.nom)
        self.actualiser_SCROLLBAR()
        self.afficher_muscu_graph()

    def selection_scrollbar(self, item):
        date = item.text()
        self.journeemodif = journeemodif(date)
        self.journeemodif.show()
        self.close()
    def ajouter_journee(self,date):
        self.journeemodif = journeemodif()
        self.journeemodif.show()
        self.close()



    def filtrer_journees(self, texte):
        self.ui.listejourney.clear()  # On vide la liste
        journeeformat = []

        for journee in self.creationcompte.historique_journee:
            date_str = journee.date.strftime("%m/%d/%Y")
            if texte.lower() in date_str.lower():  # filtre simple
                journeeformat.append(date_str)

        self.ui.listejourney.addItems(journeeformat)

        # ajout d'itemps dans la scroll bar
    def actualiser_SCROLLBAR(self):
        self.ui.listejourney.clear()  # On vide la liste
        journeeformat = []
        for journee in self.creationcompte.historique_journee:
            journeeformat.append(journee.date.strftime("%m/%d/%Y"))
        self.ui.listejourney.addItems(journeeformat)
        # il sait quand ca selectionne et le printe


        #valeur par defaut de la date filtre

    def afficher_muscu_graph(self):
        self.date_filtre = 30
        # (volume_par_seance)
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas1)
        self.ui.legraph1.setLayout(layout1)

        # (poid_journee)
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.canvas2)
        self.ui.legraph2.setLayout(layout2)

        # mettre dans le graph
        ax1 = self.figure1.add_subplot(111)
        goodgraph.volume_par_seance(ax1,self.date_filtre)
        self.canvas1.draw()

        ax2 = self.figure2.add_subplot(111)
        goodgraph.poid_journee(ax2, self.date_filtre)
        self.canvas2.draw()

    def set_filter_7_days(self):
        """Sets the filter to 7 days and updates graphs."""
        print("Setting filter to 7 days")
        self.date_filtre = 7
        self.update_graphs()

    def set_filter_30_days(self):
        """Sets the filter to 30 days and updates graphs."""
        print("Setting filter to 30 days")
        self.date_filtre = 30
        self.update_graphs()
    def set_filter_365_days(self):
        """Sets the filter to 30 days and updates graphs."""
        print("Setting filter to 30 days")
        self.date_filtre = 365
        self.update_graphs()



    def update_graphs(self):
        """Clears and redraws both graphs based on the current self.date_filtre."""
        print(f"Updating graphs with filter: {self.date_filtre}")

        # --- Update Graph 1 ---
        try:
            # Clear previous plot on figure 1
            self.figure1.clear()
            # Add new subplot
            ax1 = self.figure1.add_subplot(111)
            # Call your plotting function (doesn't depend on date_filtre here)
            goodgraph.volume_par_seance(ax1)
            # Redraw the canvas
            self.canvas1.draw()
            print("Graph 1 updated.")
        except Exception as e:
            print(f"Error updating graph 1: {e}")

        # --- Update Graph 2 ---
        try:
            # Clear previous plot on figure 2
            self.figure2.clear()
            # Add new subplot
            ax2 = self.figure2.add_subplot(111)
            # Call your plotting function, passing the CURRENT filter value
            # Ensure goodgraph.poid_journee handles the filter value (e.g., 0 for all time)
            goodgraph.poid_journee(ax2, date_filtre=self.date_filtre)
            # Redraw the canvas
            self.canvas2.draw()
            print("Graph 2 updated.")
        except Exception as e:
            print(f"Error updating graph 2: {e}")


if __name__ == "__main__":



    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
