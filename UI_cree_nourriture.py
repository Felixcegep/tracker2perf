import pickle

from PySide6.QtWidgets import QWidget, QMessageBox

from Nourriture import PortionAliment
from UI_folder import Ui_AddFoodWidget

from UI_ajouter_aliment_dispo import ajouter_aliment_disponible


class ajouter_nourriture(QWidget):
    def __init__(self,info_utilisateur,goodgraph,index_journee = None):
        super().__init__()
        self.ui = Ui_AddFoodWidget()
        self.ui.setupUi(self)
        #
        if index_journee is not None:
            self.index_journee = index_journee
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        #
        self.ui.nomComboBox
        self.ui.quantityLineEdit
        self.afficher_nom_combobox()

        self.ui.cancelButton.clicked.connect(lambda: self.retourner_journee_cancel())
        self.ui.saveButton.clicked.connect(lambda: self.cree_obj_nourriture())
        self.ui.addAvailableFoodButton.clicked.connect(lambda :self.aller_nouveau_nutrition())


    def aller_nouveau_nutrition(self):
        self.afficher_nutrition = ajouter_aliment_disponible(self.info_utilisateur,self.goodgraph,self.index_journee)
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
    def retourner_journee_cancel(self):
        from UI_journeemodif import journeemodif
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Warning)
        confirm_msg.setWindowTitle("Confirm Deletion")
        confirm_msg.setText(f"es tu certain de vouloir quitter ?")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_msg.setDefaultButton(QMessageBox.No)
        reply = confirm_msg.exec()
        if reply == QMessageBox.Yes:
            self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,self.index_journee)
            self.journeemodif.show()
            self.close()
        else:
            print("non annuler quitter ...")

    def retourner_journee(self):
        from UI_journeemodif import journeemodif
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,self.index_journee)
        self.journeemodif.show()
        self.close()
    def cree_obj_nourriture(self):
        bouffe = PortionAliment(self.ui.nomComboBox.currentText(),float(self.ui.quantityLineEdit.text()))
        self.info_utilisateur.historique_journee[self.index_journee].ajouter_nutrition_quotidienne(bouffe)
        print("avant", self.info_utilisateur.historique_journee[self.index_journee].nutrition_aujourdhui)
        self.retourner_journee()