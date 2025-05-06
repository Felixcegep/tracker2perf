import pickle
from time import strptime, strftime

from PySide6.QtWidgets import QWidget, QMessageBox, QInputDialog, QDialog
from datetime import datetime

from Muscu import Seance, Exercice, ExerciceMusculation
from UI_folder import Ui_DayView
from UI_cree_exercice import cree_exercice
from UI_cree_nourriture import ajouter_nourriture
from UI_modifier_nourriture import modifier_nourriture_obj
from UI_afficher_tous_exercices import afficher_tous_exercice
from UI_afficher_tous_aliments import afficher_tous_aliments
from DialogSeanceUi import SeanceDialog

from graphic_utilisateur import GraphicUtilisateur


class journeemodif(QWidget):
    def __init__(self,info_utilisateur,goodgraph,index_specifique=None):
        super().__init__() # Call the QWidget constructor



        self.ui = Ui_DayView()

        self.ui.setupUi(self)
        ##
        self.info_utilisateur = info_utilisateur
        self.goodgraph = goodgraph
        with open("aliment_disponible.pkl", "rb") as file:
              self.aliment_info = pickle.load(file)

        self.ui.backButton.clicked.connect(self.retourner_dashboard)


        #si appuis sur le bouton supprimer journee ca supprime la journee
        self.ui.deleteDayButton.clicked.connect(lambda : self.supprimer_journeee())

        #bouton exercice et affichage

        #addexercice renvois a la page cree exercice
        self.ui.addExerciseButton.clicked.connect(lambda: self.menu_exercice())

        self.ui.removeExerciseButton.clicked.connect(self.supprimer_exercices)
        self.ui.removeFoodButton.clicked.connect(self.supprimer_nourriture_person)
        #bouton nourriture addFoodButton
        self.ui.addFoodButton.clicked.connect(lambda :self.menu_nourriture())
        self.ui.pushButton_2.clicked.connect(self.afficher_tous_nourriture_dispo)
        self.ui.pushButton_3.clicked.connect(lambda : self.aller_modifier_nourriture_page())



        #volume total


        #
        #trouver l'index de la journee dans la liste
        if index_specifique != None:
            self.index_specifique = int(index_specifique)
            date = self.info_utilisateur.historique_journee[self.index_specifique].date.strftime("%d/%m/%Y")
            self.ui.headerLabel.setText(date)


        self.afficher_exercices()
        self.afficher_nourriture()

        self.ui.pushButton.clicked.connect(self.afficher_tous_exercice_dispo)

    def afficher_tous_nourriture_dispo(self):
        self.afficher_lesexercice = afficher_tous_aliments()
        self.afficher_lesexercice.show()

    def afficher_tous_exercice_dispo(self):
        self.afficher_lesexercice = afficher_tous_exercice()
        self.afficher_lesexercice.show()
    def menu_exercice(self):
        if len(self.info_utilisateur.historique_journee[self.index_specifique].seances_ajourdhui) == 0:
            print("il n'y a aucune seance dans la journee :(")

            dialog = SeanceDialog(self)
            if dialog.exec() == QDialog.Accepted:
                nom, duree = dialog.get_values()
                if nom.strip() and duree.strip().isdigit():
                    print(f"Séance : {nom}, durée : {duree} minutes")
                    # self.ajouter_seance(nom, int(duree))  # à adapter selon ta logique
                    self.info_utilisateur.historique_journee[self.index_specifique].ajouter_seance(Seance(str(nom), int(duree)))

                    self.aller_exerice = cree_exercice(self.info_utilisateur, self.goodgraph, self.index_specifique)
                    self.aller_exerice.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom et une durée valide.")
        else:
            self.aller_exerice = cree_exercice(self.info_utilisateur, self.goodgraph, self.index_specifique)
            self.aller_exerice.show()
            self.close()
    def menu_nourriture(self):
        self.aller_nourriture = ajouter_nourriture(self.info_utilisateur,self.goodgraph,self.index_specifique )
        self.aller_nourriture.show()
        self.close()


    def supprimer_journeee(self):
        print(self.index_specifique)
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Warning)
        confirm_msg.setWindowTitle("Confirm Deletion")
        confirm_msg.setText(f"es tu certain de vouloir supprimer la journee'?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg.setDefaultButton(QMessageBox.No)
        reply = confirm_msg.exec()
        if reply == QMessageBox.Yes:

            del self.info_utilisateur.historique_journee[self.index_specifique]
            self.info_utilisateur.sauvegarder_utilisateur()
            self.retourner_dashboard()

        else:
            print("non annulation de suppresion")

    #TODO : def exercices pas terminer :(
    def afficher_exercices(self):
        print("ouioui")
        self.ui.exercisesList.clear()
        exercice_liste_scrollbar = []

        journee = self.info_utilisateur.historique_journee[self.index_specifique]
        for exercice in journee.obtenir_exercices_info():
            try:
                if "set" in exercice and "rep" in exercice and "rpe" in exercice:
                    # Exercice de musculation
                    formatted_string = (
                        f'{exercice["nom"]} — {exercice["set"]} x {exercice["rep"]} | RPE: {exercice["rpe"]}'
                    )
                elif "duree" in exercice and "distance" in exercice and "intensite" in exercice:
                    # Exercice cardio
                    formatted_string = (
                        f'{exercice["nom"]} — Durée : {exercice["duree"]} min | '
                        f'Distance : {exercice["distance"]} km | Intensité : {exercice["intensite"]}/10'
                    )
                else:
                    # Cas par défaut
                    formatted_string = f'{exercice.get("nom", "Exercice inconnu")} — données incomplètes'
            except Exception as e:
                formatted_string = f'Erreur lors du formatage : {e}'

            exercice_liste_scrollbar.append(formatted_string)

        self.ui.exercisesList.addItems(exercice_liste_scrollbar)

    def afficher_nourriture(self):
        self.ui.foodList.clear()
        nourriture_liste_scrollbar = []
        for nourriture in self.info_utilisateur.historique_journee[self.index_specifique].nutrition_aujourdhui:
            nourriture_pour_100 = nourriture.par_100_grammes / 100
            print(nourriture_pour_100,self.aliment_info[nourriture.nom].calories)
            nombre_prot_total = str(self.aliment_info[nourriture.nom].proteines*nourriture_pour_100)
            nombre_calories_total = str(self.aliment_info[nourriture.nom].calories*nourriture_pour_100)
            nourriture_formater = f'{nourriture.nom} — {nourriture.par_100_grammes}g | Calories : {nombre_calories_total} | Protéines : {nombre_prot_total}g'

            print(self.aliment_info[nourriture.nom].calories)

            nourriture_liste_scrollbar.append(nourriture_formater)
        self.ui.foodList.addItems(nourriture_liste_scrollbar)

    def supprimer_nourriture_person(self):
        row_index = self.ui.foodList.currentRow()

        if row_index != -1:
            confirm_msg = QMessageBox()
            confirm_msg.setIcon(QMessageBox.Warning)
            confirm_msg.setWindowTitle("Confirm Deletion")
            confirm_msg.setText(f"Es-tu certain de vouloir supprimer l'élément à la ligne {row_index + 1} ?")
            confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg.setDefaultButton(QMessageBox.No)

            if confirm_msg.exec() == QMessageBox.Yes:
                nutrition_list = self.info_utilisateur.historique_journee[self.index_specifique].nutrition_aujourdhui
                print("Avant suppression :", nutrition_list)

                try:
                    del nutrition_list[row_index]
                    print("Supprimé avec succès.")
                except IndexError:
                    print(f"Index {row_index} invalide.")

                self.afficher_nourriture()
            else:
                print("Suppression annulée.")
        else:
            print("Aucun élément sélectionné.")

    def supprimer_exercices(self):
        if self.index_specifique == -1:
            print("Cannot delete exercise: invalid day index.")
            return

        row_index = self.ui.exercisesList.currentRow()

        if row_index != -1:
            confirm_msg = QMessageBox()
            confirm_msg.setIcon(QMessageBox.Warning)
            confirm_msg.setWindowTitle("Confirm Deletion")
            confirm_msg.setText(f"Es-tu certain de vouloir supprimer l'exercice à la ligne {row_index + 1} ?")
            confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg.setDefaultButton(QMessageBox.No)

            if confirm_msg.exec() == QMessageBox.Yes:
                try:
                    journee = self.info_utilisateur.historique_journee[self.index_specifique]
                    if journee.seances_ajourdhui:
                        exercices = journee.seances_ajourdhui[0].exercice_seaces
                        print("Avant suppression :", exercices)

                        del exercices[row_index]

                        print("Exercice supprimé avec succès.")
                        self.afficher_exercices()
                    else:
                        print("Erreur : aucune séance trouvée pour aujourd'hui.")

                except IndexError:
                    print(f"Erreur : index {row_index} invalide pour les exercices.")
                except Exception as e:
                    print(f"Une erreur est survenue lors de la suppression : {e}")
            else:
                print("Suppression annulée.")
        else:
            QMessageBox.warning(self, "Erreur de sélection", "Aucun exercice sélectionné pour la suppression.")
            print("Aucun élément sélectionné.")

    def retourner_dashboard(self):
        from UI_Dashboard import Dashboard
        self.info_utilisateur.sauvegarder_utilisateur()
        self.aller_dashboad = Dashboard(self.info_utilisateur,self.goodgraph)
        self.aller_dashboad.show()
        self.close()
    def aller_modifier_nourriture_page(self):
        element_selectionner = self.ui.foodList.currentItem()
        print(self.ui.foodList.currentRow())
        if element_selectionner is not None:
            self.aller_modif_nourriture = modifier_nourriture_obj(self.info_utilisateur,self.goodgraph,self.index_specifique,self.ui.foodList.currentRow())
            print(self.index_specifique,self.ui.foodList.currentRow())
            self.aller_modif_nourriture.show()
            self.close()
        else:
            print("No item selected.")