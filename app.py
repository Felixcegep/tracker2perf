import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pickle
from UI_folder import Ui_UI_Base
from UI_folder import Ui_dashboard
from graphic_utilisateur import GraphicUtilisateur

goodgraph = GraphicUtilisateur()


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        #bouton dispo
        self.button7Days =self.ui.button7Days
        self.button30Days = self.ui.button30Days
        self.depuis_debut = self.ui.buttonSinceStart
        self.ui.button7Days.clicked.connect(self.set_filter_7_days)
        self.ui.button30Days.clicked.connect(self.set_filter_30_days)  # Use .connect()
        self.ui.buttonSinceStart.clicked.connect(self.set_filter_365_days)
        print("Connected button30Days")

        #valeur par defaut de la date filtre
        self.date_filtre = 30
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
        goodgraph.volume_par_seance(ax1,self.date_filtre)
        self.canvas1.draw()

        ax2 = self.figure2.add_subplot(111)
        goodgraph.poid_journee(ax2, self.date_filtre)
        self.canvas2.draw()

    def set_filter_7_days(self):
        """Sets the filter to 7 days and updates graphs."""
        print("Setting filter to 7 days")
        self.date_filtre = 7
        self.update_graphs()

    def set_filter_30_days(self):
        """Sets the filter to 30 days and updates graphs."""
        print("Setting filter to 30 days")
        self.date_filtre = 30
        self.update_graphs()
    def set_filter_365_days(self):
        """Sets the filter to 30 days and updates graphs."""
        print("Setting filter to 30 days")
        self.date_filtre = 365
        self.update_graphs()



    def update_graphs(self):
        """Clears and redraws both graphs based on the current self.date_filtre."""
        print(f"Updating graphs with filter: {self.date_filtre}")

        # --- Update Graph 1 ---
        try:
            # Clear previous plot on figure 1
            self.figure1.clear()
            # Add new subplot
            ax1 = self.figure1.add_subplot(111)
            # Call your plotting function (doesn't depend on date_filtre here)
            goodgraph.volume_par_seance(ax1)
            # Redraw the canvas
            self.canvas1.draw()
            print("Graph 1 updated.")
        except Exception as e:
            print(f"Error updating graph 1: {e}")

        # --- Update Graph 2 ---
        try:
            # Clear previous plot on figure 2
            self.figure2.clear()
            # Add new subplot
            ax2 = self.figure2.add_subplot(111)
            # Call your plotting function, passing the CURRENT filter value
            # Ensure goodgraph.poid_journee handles the filter value (e.g., 0 for all time)
            goodgraph.poid_journee(ax2, date_filtre=self.date_filtre)
            # Redraw the canvas
            self.canvas2.draw()
            print("Graph 2 updated.")
        except Exception as e:
            print(f"Error updating graph 2: {e}")


if __name__ == "__main__":



    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
