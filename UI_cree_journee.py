from datetime import datetime

from PySide6.QtCore import QDate
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
        current_date = QDate.currentDate()
        self.ui.dateEdit.setDate(current_date)
        self.ui.dateEdit.setCalendarPopup(True)
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
            self.info_utilisateur.ajouter_journee(
                Journee(self.nomjournee.text(), self.convertir_date(), float(self.poid.text()))
            )

        except Exception as e:
            print(f"erreur de formulaire: {e}")

            # 👉 Créer le QMessageBox manuellement pour appliquer un style clair
            msg = QMessageBox(self)
            msg.setWindowTitle("Erreur Inattendue")
            msg.setText(
                "Une erreur est survenue lors de l'ajout ou de la sauvegarde.\n\nVeuillez vérifier que les données saisies sont valides et réessayez. Les données ne peuvent pas être postérieures à la date actuelle.")
            msg.setIcon(QMessageBox.Critical)

            # 🎨 Forcer mode clair
            msg.setStyleSheet("""
                QMessageBox {
                    background-color: white;
                    color: black;
                }
                QLabel {
                    color: black;
                }
                QPushButton {
                    background-color: #e0e0e0;
                    color: black;
                }
            """)

            msg.exec()

        self.info_utilisateur.sauvegarder_utilisateur()
        self.retourner_dashboard()