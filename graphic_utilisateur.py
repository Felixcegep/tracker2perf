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
        Parcourt toutes les journées et calcule le volume de chaque séance afin de créer un graphique jour par jour.
        :param ax: L’axe Matplotlib sur lequel tracer.
        :param date_filtre: Nombre de jours à afficher (par défaut 60).
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

        axe_x, axe_y = zip(*sorted(zip(axe_x, axe_y)))

        ax.clear()
        ax.plot(axe_x, axe_y, marker='o', linestyle='-', color='royalblue')
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
        Affiche l'évolution du poids jour après jour à l'aide de l'historique des données enregistrées.
        :param ax: L’axe Matplotlib sur lequel tracer.
        :param date_filtre: Nombre de jours à prendre en compte.
        :return: None
        """
        print("Génération du graphique du poids dans le temps...")
        date_limite = datetime.now() - timedelta(days=date_filtre)

        if not self.info:
            print("Erreur : les informations de l'utilisateur ne sont pas chargées.")
            ax.clear()
            ax.text(0.5, 0.5, 'Informations utilisateur non chargées', ha='center', va='center', color='red',
                    fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        if hasattr(self.info, 'actualiser_data_poid_jours') and callable(self.info.actualiser_data_poid_jours):
            try:
                print("Actualisation des données de poids...")
                self.info.actualiser_data_poid_jours()
            except Exception as e:
                print(f"Attention : erreur lors de l’actualisation des données : {e}")

        if not hasattr(self.info, 'historique_poids_journee') or not isinstance(self.info.historique_poids_journee,
                                                                                (list, tuple)):
            print("Structure des données de poids invalide.")
            ax.clear()
            ax.text(0.5, 0.5, 'Structure des données invalide', ha='center', va='center', color='red', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        if not self.info.historique_poids_journee:
            print("Aucune donnée de poids disponible.")
            ax.clear()
            ax.text(0.5, 0.5, 'Aucune donnée disponible', ha='center', va='center', color='grey', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        dates = []
        poids = []
        try:
            donnees_valides = []
            for item in self.info.historique_poids_journee:
                if isinstance(item, (list, tuple)) and len(item) == 2 and isinstance(item[1], datetime) and isinstance(
                        item[0], (int, float)) and item[1] > date_limite:
                    donnees_valides.append(item)
                else:
                    print(f"Donnée ignorée : {item}")

            if not donnees_valides:
                print("Aucune donnée valide.")
                ax.clear()
                ax.text(0.5, 0.5, 'Aucune donnée de poids valide', ha='center', va='center', color='orange',
                        fontsize=10)
                ax.set_title("Évolution du Poids")
                ax.set_xlabel("Date")
                ax.set_ylabel("Poids (unité)")
                ax.set_xticks([])
                ax.set_yticks([])
                return

            donnees_tries = sorted(donnees_valides, key=lambda x: x[1])
            dates = [item[1] for item in donnees_tries]
            poids = [item[0] for item in donnees_tries]

        except Exception as e:
            print(f"Erreur lors du traitement des données : {e}")
            ax.clear()
            ax.text(0.5, 0.5, f'Erreur : {e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Erreur")
            return

        try:
            ax.clear()
            ax.plot(dates, poids, marker='o', linestyle='-', color='royalblue')
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_title("Évolution du Poids au fil du temps")
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            for label in ax.get_xticklabels():
                label.set_rotation(45)
                label.set_horizontalalignment('right')
            ax.figure.tight_layout()
        except Exception as e:
            print(f"Erreur de tracé : {e}")
            ax.clear()
            ax.text(0.5, 0.5, f'Erreur de tracé :\n{e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Erreur de tracé")








