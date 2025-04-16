import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pickle
from UI_folder import Ui_UI_Base
from graphic_utilisateur import GraphicUtilisateur

goodgraph = GraphicUtilisateur()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UI_Base()
        self.ui.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.ui.legraph.setLayout(layout)

        # le graph volume par seance
        ax = self.figure.add_subplot(111)
        goodgraph.volume_par_seance(ax)
        self.canvas.draw()
        # poid journee
        #ax = self.figure.add_subplot(111)
        #goodgraph.poid_journee(ax, date_filtre=30)  # Show last 30 days
        #self.canvas.draw()
if __name__ == "__main__":



    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
