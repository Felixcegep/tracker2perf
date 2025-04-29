from PySide6.QtWidgets import QWidget

from Nourriture import PortionAliment
from UI_folder import Ui_AddAvailableFoodWidget


class ajouter_aliment_disponible(QWidget):
    def __init__(self,info_utilisateur,goodgraph,index_journee = None):
        super().__init__()
        self.ui = Ui_AddAvailableFoodWidget()
        self.ui.setupUi(self)
        if index_journee is not None:
            self.index_journee = index_journee
        #
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur

        self.ui.cancelButton.clicked.connect(lambda : self.menu_nourriture())
        self.ui.addButton.clicked.connect(lambda :self.ajouter_nouveau_aliment_disponible() )

    def menu_nourriture(self):
        from UI_cree_nourriture import ajouter_nourriture
        self.aller_exerice = ajouter_nourriture(self.info_utilisateur,self.goodgraph,self.index_journee)
        self.aller_exerice.show()
        self.close()
    def ajouter_nouveau_aliment_disponible(self):
        self.ui.nomLineEdit.text()
        self.ui.proteinesLineEdit.text()
        self.ui.caloriesLineEdit.text()

        PortionAliment.ajouter_aliment_disponible(str(self.ui.nomLineEdit.text()),int(self.ui.proteinesLineEdit.text()),int(self.ui.caloriesLineEdit.text()))
        PortionAliment.sauvegarder_aliment_disponible()
        print("element a été ajouter")
        self.menu_nourriture()