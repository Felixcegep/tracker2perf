from datetime import datetime
from PySide6.QtWidgets import QWidget, QMessageBox

from Journee import Journee

from UI_folder import Ui_CreateJourneeWidget
from graphic_utilisateur import GraphicUtilisateur


class cree_journee(QWidget):
    #ajouter les erreur possible
    def __init__(self,info_utilisateur,goodgraph):
        super().__init__()
        self.ui = Ui_CreateJourneeWidget()
        self.ui.setupUi(self)
        #
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        #info a extraire de l'utilisateur
        self.nomjournee = self.ui.nomJourneeLineEdit
        self.date = self.ui.dateEdit
        self.poid = self.ui.poidsAujourdhuiLineEdit
        #bouton annuler et accepter
        self.annuler = self.ui.cancelButton
        self.accepter = self.ui.saveButton
        self.annuler.clicked.connect(self.retourner_dashboard)
        self.accepter.clicked.connect(self.ajouter_journee)
    def retourner_dashboard(self):
        from UI_Dashboard import Dashboard
        self.aller_dashboad = Dashboard(self.info_utilisateur,self.goodgraph)
        self.aller_dashboad.show()
        self.close()
    def convertir_date(self):
        bon_datetime = datetime.strptime(self.date.text(), "%Y-%m-%d")
        return bon_datetime
    def ajouter_journee(self):
        try:
            self.info_utilisateur.ajouter_journee(Journee(self.nomjournee.text(),self.convertir_date(),float(self.poid.text())))

        except Exception as e:
        # Catch any other unexpected errors during add/save
            print(f"erreur de formulaire: {e}")  # Log for debugging
            QMessageBox.critical(self, "Erreur Inattendue",
                                f"Une erreur est survenue lors de l'ajout ou de la sauvegarde verifier vos donner dans les formulaire:\n\nVeuillez réessayer")

        self.info_utilisateur.sauvegarder_utilisateur()
        self.retourner_dashboard()