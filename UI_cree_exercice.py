import pickle

from PySide6.QtWidgets import QWidget, QMessageBox

from Muscu import ExerciceMusculation, ExerciceCardio, Seance
from UI_folder import Ui_ExerciseCreator
from UI_ajouter_mouvement_dispo import ajouter_mouvement_disponible_muscu



class cree_exercice(QWidget):
    #ajouter les erreur possible
    def __init__(self,info_utilisateur,goodgraph,parent = None):
        super().__init__()
        self.ui = Ui_ExerciseCreator()
        self.ui.setupUi(self)
        #
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        #bouton pour switch
        self.cardioButton= self.ui.cardioButton
        self.musculationButton = self.ui.musculationButton
        self.inputStackedWidget = self.ui.inputStackedWidget

        self.cardioPage = self.ui.cardioPage
        self.musculationPage = self.ui.musculationPage
        #changer l'affichage
        self.cardioButton.clicked.connect(lambda: self.inputStackedWidget.setCurrentWidget(self.cardioPage))
        self.musculationButton.clicked.connect(lambda: self.inputStackedWidget.setCurrentWidget(self.musculationPage))
        self.ui.cancelButton.clicked.connect(lambda :self.retourner_journee_cancel(parent))


        self.ui.addNewMovementButton.clicked.connect(lambda :self.aller_nouveau_mouvement(parent))

        #afficher dans la box de nom selon muscu ou cardio

        self.ui.musculationButton.clicked.connect(self.ajouter_exercice_deroulant)
        self.ui.cardioButton.clicked.connect(self.ajouter_cardio)


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
        self.ajouter_cardio()
        # les bouton du bas
        self.ui.saveButton.clicked.connect(lambda :self.ajouter_muscu(parent))

        self.ui.cancelButton
        self.ui.addNewMovementButton

    def aller_nouveau_mouvement(self,parent):
        self.afficher_mouvement = ajouter_mouvement_disponible_muscu(self.info_utilisateur,self.goodgraph,parent)
        self.afficher_mouvement.show()
        self.close()

    def enregister_exercice(self):
        exercice_type = self.ui.inputStackedWidget.currentWidget()
        if exercice_type:
            print(exercice_type.objectName())
            # si exercice page faire objet exercicemuscu
            #sinon faire exercicecardio
    def ajouter_muscu(self,parent):
        #pas de sauvegarde
        #info_utilisateur

        for index, journee in enumerate(self.info_utilisateur.historique_journee):
            formatted_date = journee.date.strftime("%m/%d/%Y")
            if parent == formatted_date:
                index_valide = index
                print(self.ui.nomExerciceComboBox.currentText())
                if self.ui.musculationButton.isChecked():

                    exercice = ExerciceMusculation(self.ui.nomExerciceComboBox.currentText(),int(self.ui.rpeLineEdit.text()),int(self.ui.setsLineEdit.text()),int(self.ui.repsLineEdit.text()),int(self.ui.poidsLineEdit.text()))
                    if len(self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui) != 0:
                        self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].ajouter_exercice(exercice)
                        self.retourner_journee(parent)
                    else:
                        self.info_utilisateur.historique_journee[index_valide].ajouter_seance(Seance("test"))
                        print("seance creee :)")
                        self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].ajouter_exercice(exercice)
                        self.retourner_journee(parent)
                        print("ajout a la seance et exercice muscu ")
                else:
                    exercice = ExerciceCardio(self.ui.nomExerciceComboBox.currentText(),
                                              int(self.ui.dureeLineEdit.text()), int(self.ui.distanceLineEdit.text()),
                                              int(self.ui.intensiteLineEdit.text()))
                    if len(self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui) != 0:
                        self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].ajouter_exercice(
                            exercice)
                        self.retourner_journee(parent)
                    else:
                        self.info_utilisateur.historique_journee[index_valide].ajouter_seance(Seance("test"))
                        print("seance creee :)")
                        self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].ajouter_exercice(
                            exercice)
                        self.retourner_journee(parent)
                        print("ajout a la seance et exercice cardio ")


    def retourner_journee(self,parent):
        from UI_journeemodif import journeemodif
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,parent)
        self.journeemodif.show()
        self.close()
    def retourner_journee_cancel(self,parent):
        from UI_journeemodif import journeemodif
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Warning)
        confirm_msg.setWindowTitle("Confirm Deletion")
        confirm_msg.setText(f"es tu certain de vouloir quitter'?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg.setDefaultButton(QMessageBox.No)
        reply = confirm_msg.exec()
        if reply == QMessageBox.Yes:
            self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,parent)
            self.journeemodif.show()
            self.close()
        else:
            print("non annuler")

    def ajouter_cardio(self):
        self.ui.nomExerciceComboBox.clear()

        with open("mouvement_disponible.pkl", "rb") as f:
            mouvement_disponible = pickle.load(f)
        liste_exercice = []
        for exercice, obj in mouvement_disponible.items():
            if obj.type == "cardio":
                liste_exercice.append(exercice)
        self.ui.nomExerciceComboBox.addItems(liste_exercice)

    def ajouter_exercice_deroulant(self):
        #TODO FAIRE QUE QUAND TU EST DANS CARDIO TU N'AS PAS LES MEME CHOIX QUE SI TU ES DAnS MUSCU
        self.ui.nomExerciceComboBox.clear()
        with open("mouvement_disponible.pkl", "rb") as f:
            mouvement_disponible = pickle.load(f)
        liste_exercice = []
        for exercice,obj in mouvement_disponible.items():
            if obj.type == "musculation":
                liste_exercice.append(exercice)

        self.ui.nomExerciceComboBox.addItems(liste_exercice)