from PySide6.QtWidgets import QWidget

from UI_folder import Ui_ModifyFoodView


class modifier_nourriture_obj(QWidget):
    def __init__(self,info_utilisateur,goodgraph,parent,nourriture):
        super().__init__()

        self.ui = Ui_ModifyFoodView()
        self.ui.setupUi(self)
        #
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        #
        self.ui.cancelButton.clicked.connect(lambda : self.retourner_journee(parent))
        self.ui.saveButton.clicked.connect(lambda : self.changer_objet_exercice(parent,nourriture))
        self.ui.nameLineEdit
        print(parent,nourriture)

    def retourner_journee(self, parent):
        from UI_journeemodif import journeemodif
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,parent)
        self.journeemodif.show()
        self.close()
    def changer_objet_exercice(self,parent,nourriture):
        print("lancer")
        for index, journee in enumerate(self.info_utilisateur.historique_journee):
            formatted_date = journee.date.strftime("%m/%d/%Y")
            if parent == formatted_date:
                index_valide = index
                print("a l'interieur", self.info_utilisateur.historique_journee[index_valide].nutrition_aujourdhui[nourriture].par_100_grammes)
                self.info_utilisateur.historique_journee[index_valide].nutrition_aujourdhui[nourriture].par_100_grammes = float(self.ui.nameLineEdit.text())
                print(self.info_utilisateur.historique_journee[index_valide].nutrition_aujourdhui[nourriture].par_100_grammes)
                self.info_utilisateur.sauvegarder_utilisateur()
                self.retourner_journee(parent)