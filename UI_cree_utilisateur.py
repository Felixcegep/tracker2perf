from PySide6.QtWidgets import QWidget
from datetime import datetime
from UI_folder import Ui_FormCreationCompte
from Utilisateur import Utilisateur
from graphic_utilisateur import GraphicUtilisateur


class Fenetre_cree_Utilisateur(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.ui = Ui_FormCreationCompte()
        self.ui.setupUi(self)
        #user input
        self.ui.lineEdit_Nom
        self.ui.dateEdit_Naissance
        self.ui.comboBox_Genre
        self.ui.spinBox_Taille
        self.ui.spinBox_Poids
        self.ui.pushButton_Confirm.clicked.connect(self.cree_obj_utilisateur)
    def afficher_info(self):
        #def __init__(self, nom: str, taille: int, age: int, poid: float, genre: str):
        print(self.ui.lineEdit_Nom.text())
        print(self.ui.dateEdit_Naissance.text())
        print(self.ui.spinBox_Taille.text())
        print(self.ui.spinBox_Poids.text())

    def cree_obj_utilisateur(self):


        user = Utilisateur(self.ui.lineEdit_Nom.text(),self.ui.spinBox_Taille.text(), self.caluculer_age_datenaissance(), self.ui.spinBox_Poids.text(), self.ui.comboBox_Genre.currentText())
        user.sauvegarder_utilisateur()
        goodgraph = GraphicUtilisateur()
        info_utilisateur = goodgraph.info
        print(info_utilisateur.nom)
        self.aller_dashboard(info_utilisateur,goodgraph)


    def caluculer_age_datenaissance(self):
        date_aujourdhui = datetime.now()
        date_naissance = datetime.strptime(self.ui.dateEdit_Naissance.text(), "%d/%m/%Y")
        age = date_aujourdhui.year - date_naissance.year
        if (date_aujourdhui.month, date_aujourdhui.day) < (date_naissance.month, date_naissance.day):
            age -= 1
        return age

    def aller_dashboard(self,info_utilisateur,goodgraph):
        from UI_Dashboard import Dashboard
        self.afficher_dashboard = Dashboard(info_utilisateur,goodgraph)
        self.afficher_dashboard.show()
        self.close()