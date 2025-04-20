import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDialog, QCheckBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pickle
from datetime import datetime
from Journee import Journee
from Muscu import ExerciceMusculation, Muscledispo, Exercice

from UI_folder import Ui_dashboard, Ui_DayView, Ui_CreateJourneeWidget,Ui_ExerciseCreator, Ui_AvailableExercisesDialog,Ui_AddAvailableMovementWidget
from graphic_utilisateur import GraphicUtilisateur

#graphique
goodgraph = GraphicUtilisateur()
#info de l'utilsateur
info_utilisateur = goodgraph.info
with open("mouvement_disponible.pkl", "rb") as f:
    mouvement_disponible = pickle.load(f)
#test


class ajouter_mouvement_disponible_muscu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddAvailableMovementWidget()
        self.ui.setupUi(self)
        self.ajouter_les_muscles()

        #bouton utilisateurs
        self.ui.cardioRadioButton
        self.ui.musculationRadioButton
        self.ui.addButton.clicked.connect(self.cree_mouvement_a_liste)
        print(self.ui.descriptionTextEdit.toPlainText())

    def cree_mouvement_a_liste(self):

        Exercice.ajouter_mouvement_disponible(self.ui.nomLineEdit.text(),self.ui.descriptionTextEdit.toPlainText(),self.regarder_si_cocher(),self.regarder_type_cocher())
        print("le mouvement a été ajouter")
    def ajouter_mouvement(self):
        self.ui.nomLineEdit.text()
        self.ui.descriptionTextEdit.text()
        self.ui.musclesScrollAreaContents

    def ajouter_les_muscles(self):
        for muscle in Muscledispo:
            my_new_checkbox = QCheckBox(muscle.value)

            self.ui.musclesScrollAreaContents.layout().addWidget(my_new_checkbox)
    def regarder_si_cocher(self):
        muscle_exercice = []
        layout = self.ui.musclesScrollAreaContents.layout()
        for i in range(layout.count()):
            # Get the widget at index 'i' in the layout
            widget = layout.itemAt(i).widget()

            if isinstance(widget, QCheckBox):  # Ensure it's a QCheckBox
                if widget.isChecked():
                    muscle_exercice.append(widget.text())
        return muscle_exercice

    def regarder_type_cocher(self):
        if self.ui.cardioRadioButton.isChecked() == True:
            return "musculation"
        else:
            return "cardio"


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

        for exercice in mouvement_disponible.keys():
            print(exercice)
            liste_exercices.append(exercice)
        self.ui.availableExercisesList.addItems(liste_exercices)

class cree_exercice(QWidget):
    #ajouter les erreur possible
    def __init__(self,parent = None):
        super().__init__()
        self.ui = Ui_ExerciseCreator()
        self.ui.setupUi(self)
        #bouton pour switch
        self.cardioButton= self.ui.cardioButton
        self.musculationButton = self.ui.musculationButton
        self.inputStackedWidget = self.ui.inputStackedWidget

        self.cardioPage = self.ui.cardioPage
        self.musculationPage = self.ui.musculationPage
        #changer l'affichage
        self.cardioButton.clicked.connect(lambda: self.inputStackedWidget.setCurrentWidget(self.cardioPage))
        self.musculationButton.clicked.connect(lambda: self.inputStackedWidget.setCurrentWidget(self.musculationPage))
        self.ui.cancelButton.clicked.connect(lambda :self.retourner_journee(parent))

        self.ui.addNewMovementButton.clicked.connect(self.aller_nouveau_mouvement)

        #EXTRAIRE CARDIO
        self.ui.nomExerciceComboBox
        self.ui.dureeLineEdit
        self.ui.distanceLineEdit
        self.ui.intensiteLineEdit
        #EXTRAIRE MUSCULATION
        self.ui.rpeLineEdit
        self.ui.setsLineEdit
        self.ui.repsLineEdit
        self.ui.poidsLineEdit
        self.ajouter_exercice_deroulant()
        # les bouton du bas
        self.ui.saveButton.clicked.connect(lambda :self.ajouter_muscu(parent))

        self.ui.cancelButton
        self.ui.addNewMovementButton

    def aller_nouveau_mouvement(self):
        self.afficher_mouvement = ajouter_mouvement_disponible_muscu()
        self.afficher_mouvement.show()

    def enregister_exercice(self):
        exercice_type = self.ui.inputStackedWidget.currentWidget()
        if exercice_type:
            print(exercice_type.objectName())
            # si exercice page faire objet exercicemuscu
            #sinon faire exercicecardio
    def ajouter_muscu(self,parent):
        #pas de sauvegarde
        #info_utilisateur

        for index, journee in enumerate(info_utilisateur.historique_journee):
            formatted_date = journee.date.strftime("%m/%d/%Y")
            if parent == formatted_date:
                index_valide = index
                print(self.ui.nomExerciceComboBox.currentText())
                exercice = ExerciceMusculation(self.ui.nomExerciceComboBox.currentText(),int(self.ui.rpeLineEdit.text()),int(self.ui.setsLineEdit.text()),int(self.ui.repsLineEdit.text()),int(self.ui.poidsLineEdit.text()))
                if len(info_utilisateur.historique_journee[index_valide].seances_ajourdhui) != 0:
                    info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].ajouter_exercice(exercice)
                    self.retourner_journee(parent)
                else:
                    print("il ny a pas de seance :(")
    def retourner_journee(self,parent):
        self.journeemodif = journeemodif(parent)
        self.journeemodif.show()
        self.close()

    def ajouter_cardio(self):
        pass


    def ajouter_exercice_deroulant(self):
        #TODO FAIRE QUE QUAND TU EST DANS CARDIO TU N'AS PAS LES MEME CHOIX QUE SI TU ES DAnS MUSCU
        with open("mouvement_disponible.pkl", "rb") as f:
            mouvement_disponible = pickle.load(f)
        liste_exercice = []
        for exercice in mouvement_disponible:
            liste_exercice.append(exercice)

        self.ui.nomExerciceComboBox.addItems(liste_exercice)
class cree_journee(QWidget):
    #ajouter les erreur possible
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateJourneeWidget()
        self.ui.setupUi(self)
        #info a extraire de l'utilisateur
        self.nomjournee = self.ui.nomJourneeLineEdit
        self.date = self.ui.dateEdit
        self.poid = self.ui.poidsAujourdhuiLineEdit
        #bouton annuler et accepter
        self.annuler = self.ui.cancelButton
        self.accepter = self.ui.saveButton
        self.annuler.clicked.connect(self.retourner_dashboard)
        self.accepter.clicked.connect(self.ajouter_journee)
    def retourner_dashboard(self):
        self.aller_dashboad = Dashboard()
        self.aller_dashboad.show()
        self.close()
    def convertir_date(self):
        bon_datetime = datetime.strptime(self.date.text(), "%Y-%m-%d")
        return bon_datetime
    def ajouter_journee(self):
        info_utilisateur.ajouter_journee(Journee(self.nomjournee.text(),self.convertir_date(),float(self.poid.text())))
        info_utilisateur.sauvegarder_utilisateur()
        self.retourner_dashboard()


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
        self.texte_date = self.ui.headerLabel

        #si appuis sur le bouton supprimer journee ca supprime la journee
        self.ui.deleteDayButton.clicked.connect(lambda : self.supprimer_journeee(journee_specifique))

        #bouton exercice et affichage
        self.ui.exercisesList
        #addexercice renvois a la page cree exercice
        self.ui.addExerciseButton.clicked.connect(lambda: self.menu_exercice(journee_specifique))

        self.ui.removeExerciseButton.clicked.connect(self.supprimer_exercices)
        #
        #trouver l'index de la journee dans la liste

        if journee_specifique:
            self.texte_date.setText(journee_specifique)
            for index, journee in enumerate(info_utilisateur.historique_journee):
                formatted_date = journee.date.strftime("%m/%d/%Y")
                if journee_specifique == formatted_date:
                    index_valide = index  # Store the index of the first match

                    break
        self.afficher_exercices(index_valide)

        self.ui.pushButton.clicked.connect(self.afficher_tous_exercice_dispo)
    def afficher_tous_exercice_dispo(self):
        self.afficher_lesexercice = afficher_tous_exercice()
        self.afficher_lesexercice.show()
    def menu_exercice(self,journee_specifique):
        self.aller_exerice = cree_exercice(journee_specifique)
        self.aller_exerice.show()
        self.close()


    def supprimer_journeee(self,journee_specifique):
        print(journee_specifique)
        for index, journee in enumerate(info_utilisateur.historique_journee):
            if journee.date.strftime("%m/%d/%Y") == journee_specifique:
                del info_utilisateur.historique_journee[index]
                self.retourner_dashboard()
                break


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
            element_selectionner = element_selectionner.text()
            #ajouter une pop up avant de supprimer pour assurer que c'est correcte

            info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].supprimer_exercice(element_selectionner)
            self.afficher_exercices(index_valide)

            #TODO : ajout que quand il quitte la page si il a modifier le fichier il doit sauvegarder

        else:
            print("No item selected.")
            #ajouter un message d'erreur aucun message
    def supprimer_journee(self):
        pass
    def ajouter_exercice(self,index_valide):
        pass


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
        self.date_filtre = 7
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
        self.ajouter_journee = cree_journee()
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
        goodgraph.volume_par_seance(ax1, self.date_filtre)  # gère le « vide »
        self.canvas1.draw()

        # ---------------- Tracé poid_journee ---------------
        ax2 = self.figure2.add_subplot(111)
        goodgraph.poid_journee(ax2, self.date_filtre)  # gère le « vide »
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
            goodgraph.volume_par_seance(ax1,  # 🔴 passer le filtre !
                                        date_filtre=self.date_filtre)
            self.canvas1.draw_idle()  # ✔️ draw_idle
            print("Graph 1 updated.")
        except Exception as e:
            print(f"Error updating graph 1: {e}")

        # ---------- Graphique 2 : poid_journee -------------
        try:
            self.figure2.clear()
            ax2 = self.figure2.add_subplot(111)
            goodgraph.poid_journee(ax2,
                                   date_filtre=self.date_filtre)
            self.canvas2.draw_idle()
            print("Graph 2 updated.")
        except Exception as e:
            print(f"Error updating graph 2: {e}")


if __name__ == "__main__":



    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
