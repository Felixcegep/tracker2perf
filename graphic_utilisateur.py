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
    def afficher_utilisateur(self):
        print(self.info)

    def volume_par_seance(self):
        liste_jours_volume = []
        for journee in self.info.historique_journee:
            print(journee)
            #TODO:  regarder si la liste est vide
            for seance in journee.seances_ajourdhui:
                journeevolume = (journee.date,seance.volume_par_seance())
                liste_jours_volume.append(journeevolume)
            print(liste_jours_volume)
            #ajouter date limite
            #filtre
            #et faire le graph


    def poid_journee(self,date_filtre):
        if len(self.info.historique_poids_journee) == 0:
            print("aucune date disponible")
            #TODO: devrait etre en graph
        else:
            date_limite = datetime.today() - timedelta(days = date_filtre)

            axe_x = []
            axe_y = []
            self.info.actualiser_data_poid_jours()
            sorted_journees = sorted(self.info.historique_poids_journee, key=lambda x: x[0])  # Sort by date

            for poids, date in sorted_journees:
                # Convert string date to datetime object if necessary
                if isinstance(date, str):
                    date = datetime.strptime(date, '%Y-%m-%d')
                if date >= date_limite:
                    axe_x.append(date)
                    axe_y.append(poids)
                    print(axe_x)

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
            plt.savefig("evolution_poids.png")
            plt.show()



    # graphique volume de la sessions


    
