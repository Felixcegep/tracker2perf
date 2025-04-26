import os
import sys

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QApplication
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from UI_folder import Ui_dashboard
from UI_journeemodif import journeemodif
from UI_cree_journee import cree_journee
from app import Fenetre_cree_Utilisateur
from graphic_utilisateur import GraphicUtilisateur


class Dashboard(QMainWindow):
    def __init__(self,info_utilisateur,goodgraph):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        #
        self.info_utilisateur = info_utilisateur
        self.goodgraph = goodgraph
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
        self.date_filtre = 7
        #welcome en haut a droit
        welcometext = self.ui.welcomeLabel
        # ouvrir fichier compte

        self.creationcompte = self.info_utilisateur
        # afficher le salut a l'utilisateur
        welcometext.setText("bienvenue " + self.creationcompte.nom)
        self.actualiser_SCROLLBAR()
        self.afficher_muscu_graph()

        #afficher volume total
        self.volume_total()
        self.nombre_defois_gym()
    def volume_total(self):
        total_volume_debut = 0
        tous_exercice = self.info_utilisateur.obtenir_exercices_info()
        for exerce in tous_exercice:
            total_volume_debut +=(int(exerce["set"]) * int(exerce["rep"]) * int(exerce["poid_kg"]))
        print(total_volume_debut)
        texte_formater_volume = "volume total " + str(total_volume_debut)
        self.ui.description_1.setText(texte_formater_volume)

    def nombre_defois_gym(self):
        total_gym = 0
        test = 0
        for journee in self.info_utilisateur.historique_journee:
            total_gym += len(journee.seances_ajourdhui)
        self.ui.description_2.setText("nombre de seance depuis le debut" + str(total_gym))


    def selection_scrollbar(self, item):
        date = item.text()
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,date)
        self.journeemodif.show()
        self.close()
    def ajouter_journee(self,date):
        self.ajouter_journee = cree_journee(self.info_utilisateur,self.goodgraph)
        self.ajouter_journee.show()
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
        # ---------------- Figure / Canvas 1 ----------------
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas1)
        self.ui.legraph1.setLayout(layout1)

        # ---------------- Figure / Canvas 2 ----------------
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.canvas2)
        self.ui.legraph2.setLayout(layout2)

        # ---------------- Tracé volume_par_seance ----------
        ax1 = self.figure1.add_subplot(111)
        self.goodgraph.volume_par_seance(ax1, self.date_filtre)  # gère le « vide »
        self.canvas1.draw()

        # ---------------- Tracé poid_journee ---------------
        ax2 = self.figure2.add_subplot(111)
        self.goodgraph.poid_journee(ax2, self.date_filtre)  # gère le « vide »
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
        self.date_filtre = 99999
        self.update_graphs()

    def update_graphs(self):
        """Redessine les deux graphiques avec le filtre courant."""
        print(f"Updating graphs with filter: {self.date_filtre}")

        # ---------- Graphique 1 : volume_par_seance ----------
        try:
            self.figure1.clear()  # on vide la figure
            ax1 = self.figure1.add_subplot(111)
            self.goodgraph.volume_par_seance(ax1,  # 🔴 passer le filtre !
                                        date_filtre=self.date_filtre)
            self.canvas1.draw_idle()  # ✔️ draw_idle
            print("Graph 1 updated.")
        except Exception as e:
            print(f"Error updating graph 1: {e}")

        # ---------- Graphique 2 : poid_journee -------------
        try:
            self.figure2.clear()
            ax2 = self.figure2.add_subplot(111)
            self.goodgraph.poid_journee(ax2,
                                   date_filtre=self.date_filtre)
            self.canvas2.draw_idle()
            print("Graph 2 updated.")
        except Exception as e:
            print(f"Error updating graph 2: {e}")
if __name__ == "__main__":
    goodgraph = GraphicUtilisateur()
    # info de l'utilsateur
    info_utilisateur = goodgraph.info

    if not os.path.exists("Utilisateurs.pkl"):
        app = QApplication(sys.argv)
        window = Fenetre_cree_Utilisateur()
        window.show()
        sys.exit(app.exec())
    else:
        app = QApplication(sys.argv)
        window = Dashboard(info_utilisateur,goodgraph)
        window.show()
        sys.exit(app.exec())