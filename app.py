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

        # (volume_par_seance)
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas1)
        self.ui.legraph1.setLayout(layout1)

        # (poid_journee)
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.canvas2)
        self.ui.legraph2.setLayout(layout2)

        # mettre dans le graph
        ax1 = self.figure1.add_subplot(111)
        goodgraph.volume_par_seance(ax1)
        self.canvas1.draw()

        ax2 = self.figure2.add_subplot(111)
        goodgraph.poid_journee(ax2, date_filtre=30)
        self.canvas2.draw()
if __name__ == "__main__":



    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
