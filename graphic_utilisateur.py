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
        #TODO COMPRENDRE LA LOGIQUE DES DEUX GRAPHIQUE
        """
        Trace l’évolution du volume total par séance (kg·rép) au fil des jours.

        Paramètres
        ----------
        ax : matplotlib.axes.Axes
            Axe déjà créé (par ex. figure.add_subplot()).
        date_filtre : int | None
            Nombre de jours à conserver. Ex. 90 => affiche les 90 derniers jours.
            Si None, on affiche tout l’historique.
        """

        # -- remise à zéro de l’axe --
        ax.clear()

        # -- données manquantes ? --
        if not self.info.historique_journee:
            ax.set_title("Aucune donnée disponible")
            ax.figure.tight_layout()
            return

        # -- limite temporelle --
        date_limite = (
            datetime.today() - timedelta(days=date_filtre)
            if date_filtre is not None
            else datetime.min
        )

        # -- récolte & filtre --
        donnees = []  # [(date, volume), …]
        for journee in self.info.historique_journee:
            # Conversion éventuelle en datetime
            d = journee.date
            if isinstance(d, str):
                d = datetime.strptime(d, "%Y-%m-%d")

            if d < date_limite:
                continue  # on ignore cette journée

            for seance in journee.seances_ajourdhui:
                donnees.append((d, seance.volume_par_seance()))

        if not donnees:  # il ne reste rien après filtrage
            ax.set_title("Aucune donnée disponible")
            ax.figure.tight_layout()
            return

        # -- tri chronologique --
        donnees.sort(key=lambda t: t[0])

        # -- séparation X/Y --
        axe_x, axe_y = zip(*donnees)

        # -- tracé --
        ax.plot_date(axe_x, axe_y, "-o")
        ax.set_title("Évolution du volume par séance")
        ax.set_xlabel("Date")
        ax.set_ylabel("Volume (kg·rép)")  # adapte le libellé si besoin
        ax.grid(True)

        # formatage de l’axe X
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax.tick_params(axis="x", rotation=45)
        ax.figure.tight_layout()

    def poid_journee(self, ax, date_filtre):
        ax.clear()

        # Rien à tracer ?
        if not self.info.historique_poids_journee:
            ax.set_title("Aucune donnée disponible")
            ax.figure.tight_layout()
            return

        date_limite = datetime.today() - timedelta(days=date_filtre)

        # -- convertir une bonne fois les dates en datetime et filtrer --
        donnees = []
        for poids, date in self.info.historique_poids_journee:
            if isinstance(date, str):
                date = datetime.strptime(date, "%Y-%m-%d")
            if date >= date_limite:
                donnees.append((date, poids))  # <- (date, poids) !

        if not donnees:
            ax.set_title("Aucune donnée disponible")
            ax.figure.tight_layout()
            return

        # -- trier par date --
        donnees.sort(key=lambda t: t[0])  # t[0] = date

        # -- séparer X et Y --
        axe_x, axe_y = zip(*donnees)

        # -- tracer --
        ax.plot_date(axe_x, axe_y, "-o")  # plot_date gère mieux les dates
        ax.set_title("Évolution du poids au fil des jours")
        ax.set_xlabel("Date")
        ax.set_ylabel("Poids (lbs)")
        ax.grid(True)

        # Formatage de l’axe X
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax.tick_params(axis="x", rotation=45)
        ax.figure.tight_layout()

    # graphique volume de la sessions


    
