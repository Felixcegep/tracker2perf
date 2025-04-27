import pickle

from PySide6.QtWidgets import QWidget, QMessageBox

from Nourriture import PortionAliment
from UI_folder import Ui_AddFoodWidget

from UI_ajouter_aliment_dispo import ajouter_aliment_disponible


class ajouter_nourriture(QWidget):
    def __init__(self,info_utilisateur,goodgraph,parent = None):
        super().__init__()
        self.ui = Ui_AddFoodWidget()
        self.ui.setupUi(self)
        #
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        #
        self.ui.nomComboBox
        self.ui.quantityLineEdit
        self.afficher_nom_combobox()

        self.ui.cancelButton.clicked.connect(lambda: self.retourner_journee_cancel(parent))
        self.ui.saveButton.clicked.connect(lambda: self.cree_obj_nourriture(parent))
        self.ui.addAvailableFoodButton.clicked.connect(lambda :self.aller_nouveau_nutrition(parent))


    def aller_nouveau_nutrition(self,parent):
        self.afficher_nutrition = ajouter_aliment_disponible(self.info_utilisateur,self.goodgraph,parent)
        self.afficher_nutrition.show()
        self.close()
    def afficher_nom_combobox(self):
        self.ui.nomComboBox.clear()
        with open("aliment_disponible.pkl", "rb") as f:
            aliment_dispo = pickle.load(f)
        liste_nourriture = []
        for aliment in aliment_dispo.keys():
            liste_nourriture.append(aliment)
        self.ui.nomComboBox.addItems(liste_nourriture)
    def retourner_journee_cancel(self,parent):
        from UI_journeemodif import journeemodif
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Warning)
        confirm_msg.setWindowTitle("Confirm Deletion")
        confirm_msg.setText(f"es tu certain de vouloir quitter ?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg.setDefaultButton(QMessageBox.No)
        reply = confirm_msg.exec()
        if reply == QMessageBox.Yes:
            self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,parent)
            self.journeemodif.show()
            self.close()
        else:
            print("non annuler quitter ...")

    def retourner_journee(self,parent):
        from UI_journeemodif import journeemodif
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,parent)
        self.journeemodif.show()
        self.close()
    def cree_obj_nourriture(self,parent):
        for index, journee in enumerate(self.info_utilisateur.historique_journee):
            formatted_date = journee.date.strftime("%m/%d/%Y")
            if parent == formatted_date:
                index_valide = index
                bouffe = PortionAliment(self.ui.nomComboBox.currentText(),float(self.ui.quantityLineEdit.text()))
                self.info_utilisateur.historique_journee[index_valide].ajouter_nutrition_quotidienne(bouffe)
                print("avant", self.info_utilisateur.historique_journee[index_valide].nutrition_aujourdhui)
                self.retourner_journee(parent)