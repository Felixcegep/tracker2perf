import pickle
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from Utilisateur import Utilisateur
from datetime import datetime, timedelta
class GraphicUtilisateur:
    def __init__(self):
        with open("Utilisateurs.pkl", "rb") as f:
            self.info = pickle.load(f)
        print(self.info)
    def afficher_utilisateur(self):
        print(self.info)

    from datetime import datetime, timedelta
    import matplotlib.dates as mdates

    def volume_par_seance(self, ax, date_filtre=None):
        print("lancer...")
        axe_x = []
        axe_y = []
        liste_jours_volume = []

        if len(self.info.historique_journee) > 0:
            for journee in self.info.historique_journee:
                for seance in journee.seances_ajourdhui:
                    journeevolume = (journee.date, seance.volume_par_seance())
                    liste_jours_volume.append(journeevolume)

            sorted_journees = sorted(liste_jours_volume, key=lambda x: x[0])
            for date, poids in sorted_journees:
                if isinstance(date, datetime):
                    axe_x.append(date)
                    axe_y.append(poids)

            # Plotting on the given axis
            ax.clear()
            ax.plot(axe_x, axe_y)
            ax.set_title("Évolution du volume au fil des jours")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (lbs)")
            ax.grid(True)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            for label in ax.get_xticklabels():
                label.set_rotation(45)
                label.set_horizontalalignment('right')
            ax.figure.tight_layout()
            # fait un retation
        else:
            print("la liste est vide")











































    def poid_journee(self, ax, date_filtre):
        if len(self.info.historique_poids_journee) == 0:
            print("aucune date disponible")
            # TODO: pourrait afficher un message dans le graph
            ax.clear()
            ax.set_title("Aucune donnée disponible")
            ax.figure.tight_layout()
        else:
            date_limite = datetime.today() - timedelta(days=date_filtre)

            axe_x = []
            axe_y = []
            self.info.actualiser_data_poid_jours()
            sorted_journees = sorted(self.info.historique_poids_journee, key=lambda x: x[0])

            for poids, date in sorted_journees:
                if isinstance(date, str):
                    date = datetime.strptime(date, '%Y-%m-%d')
                if date >= date_limite:
                    axe_x.append(date)
                    axe_y.append(poids)

            ax.clear()
            ax.plot(axe_x, axe_y, marker='o')
            ax.set_title("Évolution du poids au fil des jours")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (lbs)")
            ax.grid(True)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            for label in ax.get_xticklabels():
                label.set_rotation(45)
                label.set_horizontalalignment('right')
            ax.figure.tight_layout()

    # graphique volume de la sessions


    
