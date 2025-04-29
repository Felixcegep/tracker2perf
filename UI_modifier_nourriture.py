from PySide6.QtWidgets import QWidget

from UI_folder import Ui_ModifyFoodView


class modifier_nourriture_obj(QWidget):
    def __init__(self,info_utilisateur,goodgraph,index_journee,nourriture):
        super().__init__()

        self.ui = Ui_ModifyFoodView()
        self.ui.setupUi(self)
        self.index_journee = int(index_journee)
        print("dans modifier_nourriture_obj", index_journee, nourriture)
        #
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        #
        self.ui.cancelButton.clicked.connect(lambda : self.retourner_journee())
        self.ui.saveButton.clicked.connect(lambda : self.changer_objet_exercice(nourriture))


    def retourner_journee(self):
        from UI_journeemodif import journeemodif
        self.journeemodif = journeemodif(self.info_utilisateur,self.goodgraph,self.index_journee)
        self.journeemodif.show()
        self.close()
    def changer_objet_exercice(self,index_nourriture):

        print("a l'interieur", self.info_utilisateur.historique_journee[self.index_journee].nutrition_aujourdhui[index_nourriture].par_100_grammes)
        self.info_utilisateur.historique_journee[self.index_journee].nutrition_aujourdhui[index_nourriture].par_100_grammes = float(self.ui.nameLineEdit.text())
        print(self.info_utilisateur.historique_journee[self.index_journee].nutrition_aujourdhui[index_nourriture].par_100_grammes)
        self.info_utilisateur.sauvegarder_utilisateur()
        self.retourner_journee()