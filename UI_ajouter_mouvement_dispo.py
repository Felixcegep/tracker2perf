from PySide6.QtWidgets import QWidget, QCheckBox

from Muscu import Exercice, Muscledispo
from UI_folder import Ui_AddAvailableMovementWidget


class ajouter_mouvement_disponible_muscu(QWidget):
    def __init__(self,info_utilisateur,goodgraph,index_journee = None):
        super().__init__()
        self.ui = Ui_AddAvailableMovementWidget()
        self.ui.setupUi(self)
        #
        if index_journee is not None:
            self.index_journee = index_journee
        self.goodgraph = goodgraph
        self.info_utilisateur = info_utilisateur
        self.ajouter_les_muscles()

        #bouton utilisateurs
        self.ui.cardioRadioButton
        self.ui.musculationRadioButton
        self.ui.addButton.clicked.connect(lambda :self.cree_mouvement_a_liste())
        self.ui.cancelButton.clicked.connect(lambda : self.menu_exercice())
        print(self.ui.descriptionTextEdit.toPlainText())
    def menu_exercice(self):
        """
        aller dans le menu exercice
        :return:
        """
        from UI_cree_exercice import cree_exercice
        self.aller_exerice = cree_exercice(self.info_utilisateur,self.goodgraph,self.index_journee)
        self.aller_exerice.show()
        self.close()

    def cree_mouvement_a_liste(self):
        print(self.regarder_type_cocher())
        Exercice.ajouter_mouvement_disponible(self.ui.nomLineEdit.text(),self.ui.descriptionTextEdit.toPlainText(),self.regarder_si_cocher(),self.regarder_type_cocher())
        Exercice.sauvegarder_mouvement_disponible()
        self.menu_exercice()
    def ajouter_mouvement(self):
        self.ui.nomLineEdit.text()
        self.ui.descriptionTextEdit.text()
        self.ui.musclesScrollAreaContents

    def ajouter_les_muscles(self):
        """
        :return:
        """
        for muscle in Muscledispo:
            my_new_checkbox = QCheckBox(muscle.value)

            self.ui.musclesScrollAreaContents.layout().addWidget(my_new_checkbox)
    def regarder_si_cocher(self):
        muscle_exercice = []
        layout = self.ui.musclesScrollAreaContents.layout()
        for i in range(layout.count()):
            # Get the widget at index 'i' in the layout
            widget = layout.itemAt(i).widget()

            if isinstance(widget, QCheckBox):  # Ensure it's a QCheckBox
                if widget.isChecked():
                    muscle_exercice.append(widget.text())
        return muscle_exercice

    def regarder_type_cocher(self):
        if self.ui.cardioRadioButton.isChecked() == True:
            return "cardio"
        else:
            return "musculation"