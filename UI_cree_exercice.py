import pickle

from PySide6.QtWidgets import QWidget, QMessageBox

from Muscu import ExerciceMusculation, ExerciceCardio, Seance
from UI_folder import Ui_ExerciseCreator
from UI_ajouter_mouvement_dispo import ajouter_mouvement_disponible_muscu



class cree_exercice(QWidget):
    #ajouter les erreur possible
    def __init__(self,info_utilisateur,goodgraph,index_journee = None):
        super().__init__()
        self.ui = Ui_ExerciseCreator()
        self.ui.setupUi(self)
        if index_journee is not None:
            self.index_journee = index_journee
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
        self.ui.cancelButton.clicked.connect(lambda :self.retourner_journee_cancel())


        self.ui.addNewMovementButton.clicked.connect(lambda :self.aller_nouveau_mouvement())

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
        self.ui.saveButton.clicked.connect(lambda :self.ajouter_muscu())

        self.ui.cancelButton
        self.ui.addNewMovementButton

    def aller_nouveau_mouvement(self):
        self.afficher_mouvement = ajouter_mouvement_disponible_muscu(self.info_utilisateur,self.goodgraph,self.index_journee)
        self.afficher_mouvement.show()
        self.close()

    def enregister_exercice(self):
        exercice_type = self.ui.inputStackedWidget.currentWidget()
        if exercice_type:
            print(exercice_type.objectName())
            # si exercice page faire objet exercicemuscu
            #sinon faire exercicecardio

    def ajouter_muscu(self):
        # pas de sauvegarde
        # info_utilisateur
        self.index_journee

        if self.ui.musculationButton.isChecked():
            try:
                exercice = ExerciceMusculation(
                    self.ui.nomExerciceComboBox.currentText(),
                    int(self.ui.rpeLineEdit.text()),
                    int(self.ui.setsLineEdit.text()),
                    int(self.ui.repsLineEdit.text()),
                    int(self.ui.poidsLineEdit.text())
                )
            except ValueError as e:
                error_message = (
                    "Erreur lors de la création de l'exercice\n"
                    "Veuillez vous assurer que RPE, Séries, Répétitions et Poids sont des nombres entiers valides."
                )
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Input Error")
                msgBox.setText(error_message)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                if len(self.info_utilisateur.historique_journee[self.index_journee].seances_ajourdhui) != 0:
                    self.info_utilisateur.historique_journee[self.index_journee].seances_ajourdhui[0].ajouter_exercice(
                        exercice)
                    self.retourner_journee()
                else:
                    self.info_utilisateur.historique_journee[self.index_journee].ajouter_seance(Seance("test"))
                    print("Séance créée :)")
                    self.info_utilisateur.historique_journee[self.index_journee].seances_ajourdhui[0].ajouter_exercice(
                        exercice)
                    self.retourner_journee()
                    print("Ajout à la séance et exercice musculation")
        else:
            try:
                exercice = ExerciceCardio(
                    self.ui.nomExerciceComboBox.currentText(),
                    int(self.ui.dureeLineEdit.text()),
                    int(self.ui.distanceLineEdit.text()),
                    int(self.ui.intensiteLineEdit.text())
                )
            except ValueError as e:
                error_message = (
                    "Erreur lors de la création de l'exercice\n"
                    "Veuillez vous assurer que Durée, Distance et Intensité sont des nombres entiers valides."
                )
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Input Error")
                msgBox.setText(error_message)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                if len(self.info_utilisateur.historique_journee[self.index_journee].seances_ajourdhui) != 0:
                    self.info_utilisateur.historique_journee[self.index_journee].seances_ajourdhui[0].ajouter_exercice(
                        exercice)
                    self.retourner_journee()
                else:
                    self.info_utilisateur.historique_journee[self.index_journee].ajouter_seance(Seance("test"))
                    print("Séance créée :)")
                    self.info_utilisateur.historique_journee[self.index_journee].seances_ajourdhui[0].ajouter_exercice(
                        exercice)
                    self.retourner_journee()
                    print("Ajout à la séance et exercice cardio")

    def retourner_journee(self):
        from UI_journeemodif import journeemodif
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,self.index_journee)
        self.journeemodif.show()
        self.close()
    def retourner_journee_cancel(self):
        from UI_journeemodif import journeemodif
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Warning)
        confirm_msg.setWindowTitle("Confirm Deletion")
        confirm_msg.setText(f"es tu certain de vouloir quitter'?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg.setDefaultButton(QMessageBox.No)
        reply = confirm_msg.exec()
        if reply == QMessageBox.Yes:
            self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,self.index_journee)
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