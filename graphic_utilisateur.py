import pickle
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from Utilisateur import Utilisateur
from datetime import datetime
class GraphicUtilisateur:
    def __init__(self):
        with open("Utilisateurs.pkl", "rb") as f:
            self.info = pickle.load(f)
    def afficher_utilisateur(self):
        print(self.info)
    # graph poid et le temps
    # exercice les réaliser fait
    def poid_journee(self):
        axe_x = []
        axe_y = []
        self.info.actualiser_data_poid_jours()
        sorted_journees = sorted(self.info.historique_poids_journee, key=lambda x: x[0])  # Sort by date

        for poids, date in sorted_journees:
            # Convert string date to datetime object if necessary
            if isinstance(date, str):
                date = datetime.strptime(date, '%Y-%m-%d')

            axe_x.append(date)
            axe_y.append(poids)

        fig, ax = plt.subplots()
        ax.plot(axe_x, axe_y)

        # Format the x-axis to show dates properly
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        # Auto format x-axis labels
        fig.autofmt_xdate()

        plt.xlabel("Date")
        plt.ylabel("Poids (lbs)")
        plt.title("Évolution du poids au fil des jours")
        plt.grid(True)

        plt.show()



    # graphique volume de la sessions
if __name__ == '__main__':
    g = GraphicUtilisateur()
    g.poid_journee()