from PySide6.QtWidgets import QWidget, QMessageBox

from UI_folder import Ui_DayView
from UI_cree_exercice import cree_exercice
from UI_cree_nourriture import ajouter_nourriture
from UI_modifier_nourriture import modifier_nourriture_obj
from UI_afficher_tous_exercices import afficher_tous_exercice
from UI_afficher_tous_aliments import afficher_tous_aliments


from graphic_utilisateur import GraphicUtilisateur



class journeemodif(QWidget):
    def __init__(self,info_utilisateur,goodgraph,journee_specifique=None):
        super().__init__() # Call the QWidget constructor


        self.ui = Ui_DayView()

        self.ui.setupUi(self)
        ##
        self.info_utilisateur = info_utilisateur
        self.goodgraph = goodgraph

        self.ui.backButton.clicked.connect(self.retourner_dashboard)
        self.texte_date = self.ui.headerLabel

        #si appuis sur le bouton supprimer journee ca supprime la journee
        self.ui.deleteDayButton.clicked.connect(lambda : self.supprimer_journeee(journee_specifique))

        #bouton exercice et affichage

        #addexercice renvois a la page cree exercice
        self.ui.addExerciseButton.clicked.connect(lambda: self.menu_exercice(journee_specifique))

        self.ui.removeExerciseButton.clicked.connect(self.supprimer_exercices)
        self.ui.removeFoodButton.clicked.connect(self.supprimer_nourriture_person)
        #bouton nourriture addFoodButton
        self.ui.addFoodButton.clicked.connect(lambda :self.menu_nourriture(journee_specifique))
        self.ui.pushButton_2.clicked.connect(self.afficher_tous_nourriture_dispo)
        self.ui.pushButton_3.clicked.connect(lambda : self.aller_modifier_nourriture_page(journee_specifique))



        #volume total


        #
        #trouver l'index de la journee dans la liste

        if journee_specifique:
            self.texte_date.setText(journee_specifique)
            for index, journee in enumerate(self.info_utilisateur.historique_journee):
                formatted_date = journee.date.strftime("%m/%d/%Y")
                if journee_specifique == formatted_date:
                    index_valide = index  # Store the index of the first match

                    break
        self.afficher_exercices(index_valide)
        self.afficher_nourriture(index_valide)

        self.ui.pushButton.clicked.connect(self.afficher_tous_exercice_dispo)

    def afficher_tous_nourriture_dispo(self):
        self.afficher_lesexercice = afficher_tous_aliments()
        self.afficher_lesexercice.show()

    def afficher_tous_exercice_dispo(self):
        self.afficher_lesexercice = afficher_tous_exercice()
        self.afficher_lesexercice.show()
    def menu_exercice(self,journee_specifique):
        self.aller_exerice = cree_exercice(self.info_utilisateur,self.goodgraph,journee_specifique)
        self.aller_exerice.show()
        self.close()
    def menu_nourriture(self,journee_specifique):
        self.aller_nourriture = ajouter_nourriture(self.info_utilisateur,self.goodgraph,journee_specifique)
        self.aller_nourriture.show()
        self.close()


    def supprimer_journeee(self,journee_specifique):
        print(journee_specifique)
        for index, journee in enumerate(self.info_utilisateur.historique_journee):
            if journee.date.strftime("%m/%d/%Y") == journee_specifique:
                del self.info_utilisateur.historique_journee[index]
                self.info_utilisateur.sauvegarder_utilisateur()
                self.retourner_dashboard()
                break


    #TODO : def exercices pas terminer :(
    def afficher_exercices(self,index_valide):
        print("ouioui")
        self.ui.exercisesList.clear()

        exercice_liste_scrollbar = []
        for exercice in self.info_utilisateur.historique_journee[index_valide].obtenir_exercices_info():


            exercice_liste_scrollbar.append(exercice["nom"])


        self.ui.exercisesList.addItems(exercice_liste_scrollbar)
    def afficher_nourriture(self,index_valide):
        self.ui.foodList.clear()
        nourriture_liste_scrollbar = []
        for nourriture in self.info_utilisateur.historique_journee[index_valide].nutrition_aujourdhui:

            nourriture_liste_scrollbar.append(nourriture.nom)
        self.ui.foodList.addItems(nourriture_liste_scrollbar)
    def supprimer_nourriture_person(self,index_valide):
        element_selectionner = self.ui.foodList.currentItem()
        if element_selectionner is not None:
            element_selectionner = element_selectionner.text()
            confirm_msg = QMessageBox()
            confirm_msg.setIcon(QMessageBox.Warning)
            confirm_msg.setWindowTitle("Confirm Deletion")
            confirm_msg.setText(f"es tu certain de vouloir supprimer '{element_selectionner}'?")
            confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg.setDefaultButton(QMessageBox.No)
            reply = confirm_msg.exec()
            if reply == QMessageBox.Yes:
                print(element_selectionner)
                self.info_utilisateur.historique_journee[index_valide].supprimer_nutrition_quotidienne(element_selectionner)
                print("supprimer avec succes")
                self.afficher_nourriture(index_valide)
            else:
                print("non annuler")
        else:
            print("rien n'a été selectionner")

    def supprimer_exercices(self, index_valide):
        if index_valide == -1:
             print("Cannot delete exercise: invalid day index.")
             return # Prevent error if index wasn't found in init

        element_selectionner = self.ui.exercisesList.currentItem()
        if element_selectionner is not None:
            element_selectionner_text = element_selectionner.text()

            # --- Confirmation Dialog ---
            confirm_msg = QMessageBox()
            confirm_msg.setIcon(QMessageBox.Warning)
            confirm_msg.setWindowTitle("Confirm Deletion")
            confirm_msg.setText(f"es tu certain de vouloir supprimer '{element_selectionner_text}'?")
            confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm_msg.setDefaultButton(QMessageBox.No)
            reply = confirm_msg.exec()
            # -------------------------

            if reply == QMessageBox.Yes:
                try:
                    # Make sure the structure is correct for deletion
                    # Assuming seances_aujourdhui is a list and has at least one element
                    if self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui:
                         self.info_utilisateur.historique_journee[index_valide].seances_ajourdhui[0].supprimer_exercice(element_selectionner_text)
                         self.afficher_exercices(index_valide)
                         print(f"Exercise '{element_selectionner_text}' deleted successfully.")
                         # Consider adding save logic here too if needed immediately
                    else:
                         print("Error: No workout session found for today to delete exercise from.")

                except IndexError:
                    print(f"Error: Invalid index {index_valide} for historique_journee.")
                except Exception as e:
                    print(f"An error occurred during exercise deletion: {e}")
            else:
                print("Deletion cancelled.")

        else:
            QMessageBox.warning(self, "Selection Error", "No exercise selected to delete.") # Use QMessageBox for user feedback
            print("No item selected.")


    def retourner_dashboard(self):
        from UI_Dashboard import Dashboard
        self.info_utilisateur.sauvegarder_utilisateur()
        self.aller_dashboad = Dashboard(self.info_utilisateur,self.goodgraph)
        self.aller_dashboad.show()
        self.close()
    def aller_modifier_nourriture_page(self,journee_specifique):
        element_selectionner = self.ui.foodList.currentItem()
        if element_selectionner is not None:
            element_selectionner = element_selectionner.text()
            self.aller_modif_nourriture = modifier_nourriture_obj(self.info_utilisateur,self.goodgraph,journee_specifique,element_selectionner)
            self.aller_modif_nourriture.show()
            self.close()
        else:
            print("No item selected.")