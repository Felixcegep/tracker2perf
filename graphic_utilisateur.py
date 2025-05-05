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
        """
        affiche l'utilisateur de la sessions
        :return:
        """
        print(self.info)

    from datetime import datetime, timedelta
    import matplotlib.dates as mdates

    def volume_par_seance(self, ax, date_filtre=60):
        """
        passe a travers toutes les journee et regarde le volume de chaque seance pour ensuite pouvoir faire un diagramme
        de jours par jours
        :param ax:
        :param date_filtre:
        :return: None
        """
        print("Génération du graphique du volume par séance...")

        if not hasattr(self.info, 'historique_journee') or not self.info.historique_journee:
            print("Aucune donnée de séance disponible.")
            ax.clear()
            ax.text(0.5, 0.5, 'Aucune donnée disponible', ha='center', va='center', color='gray', fontsize=10)
            ax.set_title("Évolution du volume")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        date_limite = datetime.now() - timedelta(days=date_filtre)
        axe_x = []
        axe_y = []

        for journee in self.info.historique_journee:
            for seance in journee.seances_ajourdhui:
                if isinstance(journee.date, datetime):
                    volume = seance.volume_par_seance()
                    if isinstance(volume, (int, float)) and journee.date > date_limite:
                        axe_x.append(journee.date)
                        axe_y.append(volume)

        if not axe_x:
            ax.clear()
            ax.text(0.5, 0.5, 'Aucune donnée dans la période choisie', ha='center', va='center', color='orange',
                    fontsize=10)
            ax.set_title("Évolution du volume")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        # ✅ Tri des données par date croissante
        axe_x, axe_y = zip(*sorted(zip(axe_x, axe_y)))

        ax.clear()
        ax.plot(axe_x, axe_y, marker='o', linestyle='-', color='royalblue')  # couleur bleue
        ax.set_title("Évolution du volume par séance")
        ax.set_xlabel("Date")
        ax.set_ylabel("Volume (lbs)")
        ax.grid(True)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_horizontalalignment('right')
        ax.figure.tight_layout()

    def poid_journee(self, ax, date_filtre=None):
        """
        regarde le poid a chaque jours a l'aide de la tupple dans utilisateurs et zip permet de cree un deux liste avec
        premiers index liste journeee et deuxieme liste poids pour ensuite les mettre dans le graphique
        :param ax:
        :param date_filtre:
        :return:
        """
        print("Generating weight over time plot on provided axes...")
        date_limite = datetime.now() - timedelta(days=date_filtre)

        if not self.info:
            print("Error: User info not loaded.")
            ax.clear()
            ax.text(0.5, 0.5, 'User info not loaded', ha='center', va='center', color='red', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        if hasattr(self.info, 'actualiser_data_poid_jours') and callable(self.info.actualiser_data_poid_jours):
            try:
                print("Actualising weight data...")
                self.info.actualiser_data_poid_jours()
            except Exception as e:
                print(f"Warning: Error during data refresh: {e}")

        if not hasattr(self.info, 'historique_poids_journee') or not isinstance(self.info.historique_poids_journee,
                                                                                (list, tuple)):
            print("Invalid weight data structure.")
            ax.clear()
            ax.text(0.5, 0.5, 'Weight data structure invalid', ha='center', va='center', color='red', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        if not self.info.historique_poids_journee:
            print("No weight history data.")
            ax.clear()
            ax.text(0.5, 0.5, 'No weight data available', ha='center', va='center', color='grey', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        dates = []
        weights = []
        try:
            valid_data = []
            for item in self.info.historique_poids_journee:
                if isinstance(item, (list, tuple)) and len(item) == 2 and isinstance(item[1], datetime) and isinstance(
                        item[0], (int, float)) and item[1] > date_limite:
                    valid_data.append(item)
                else:
                    print(f"Skipping invalid entry: {item}")

            if not valid_data:
                print("No valid entries.")
                ax.clear()
                ax.text(0.5, 0.5, 'No valid weight data', ha='center', va='center', color='orange', fontsize=10)
                ax.set_title("Évolution du Poids")
                ax.set_xlabel("Date")
                ax.set_ylabel("Poids (unité)")
                ax.set_xticks([])
                ax.set_yticks([])
                return

            sorted_data = sorted(valid_data, key=lambda x: x[1])
            dates = [item[1] for item in sorted_data]
            weights = [item[0] for item in sorted_data]

        except Exception as e:
            print(f"Error processing weight data: {e}")
            ax.clear()
            ax.text(0.5, 0.5, f'Error: {e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Error")
            return

        try:
            ax.clear()
            ax.plot(dates, weights, marker='o', linestyle='-', color='coral')
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_title("Évolution du Poids au Fil du Temps")
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            for label in ax.get_xticklabels():
                label.set_rotation(45)
                label.set_horizontalalignment('right')
            ax.figure.tight_layout()
        except Exception as e:
            print(f"Plotting error: {e}")
            ax.clear()
            ax.text(0.5, 0.5, f'Plotting error:\n{e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Plot Error")








