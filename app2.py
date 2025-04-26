import os
import sys

from PySide6.QtWidgets import QApplication

from UI_Dashboard import Dashboard
from UI_cree_utilisateur import Fenetre_cree_Utilisateur
from graphic_utilisateur import GraphicUtilisateur

if __name__ == "__main__":


    if not os.path.exists("Utilisateurs.pkl"):
        app = QApplication(sys.argv)
        window = Fenetre_cree_Utilisateur()
        window.show()
        sys.exit(app.exec())
    else:
        goodgraph = GraphicUtilisateur()
        # info de l'utilsateur
        info_utilisateur = goodgraph.info
        app = QApplication(sys.argv)
        window = Dashboard(info_utilisateur,goodgraph)
        window.show()
        sys.exit(app.exec())