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

    def poid_journee(self, ax, date_filtre=None):
        """
        Draws a graph of weight over time onto the provided Matplotlib Axes object.

        Args:
            ax (matplotlib.axes.Axes): The Axes object to draw the plot on.
            date_filtre (datetime, optional): A filter date (currently not implemented). Defaults to None.
        """
        print("Generating weight over time plot on provided axes...")

        # --- Pre-checks ---
        if not self.info:
            print("Error: User info not loaded. Cannot generate plot.")
            ax.clear()
            ax.text(0.5, 0.5, 'User info not loaded', ha='center', va='center', color='red', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])  # Clear ticks for empty plot
            ax.set_yticks([])
            return

        # Optional: Call data refresh method if it exists
        if hasattr(self.info, 'actualiser_data_poid_jours') and callable(self.info.actualiser_data_poid_jours):
            try:
                print("Actualising weight data...")
                self.info.actualiser_data_poid_jours()
            except Exception as e:
                print(f"Warning: Error during actualiser_data_poid_jours: {e}.")
        # else: No need to print if it doesn't exist every time

        # Check if the weight history attribute exists and is list/tuple
        if not hasattr(self.info, 'historique_poids_journee') or \
                not isinstance(self.info.historique_poids_journee, (list, tuple)):
            print("Cannot plot: 'historique_poids_journee' attribute missing or not a list/tuple.")
            ax.clear()
            ax.text(0.5, 0.5, 'Weight data structure invalid', ha='center', va='center', color='red', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        if not self.info.historique_poids_journee:
            print("Cannot plot: No weight history data (historique_poids_journee is empty).")
            ax.clear()
            ax.text(0.5, 0.5, 'No weight data available', ha='center', va='center', color='grey', fontsize=10)
            ax.set_title("Évolution du Poids")
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")
            ax.set_xticks([])
            ax.set_yticks([])
            return

        # --- Data Preparation ---
        dates = []
        weights = []
        try:
            # Filter for valid entries AND apply date_filtre if needed (basic example)
            valid_data_tuples = []
            for item in self.info.historique_poids_journee:
                if isinstance(item, (list, tuple)) and len(item) == 2 and isinstance(item[1], datetime) and isinstance(
                        item[0], (int, float)):
                    # --- Apply date_filtre here if needed ---
                    # Example: Only include dates after the filter date
                    # if date_filtre is None or item[1] >= date_filtre:
                    #     valid_data_tuples.append(item)
                    # For now, include all valid items:
                    valid_data_tuples.append(item)
                else:
                    print(f"Warning: Skipping invalid data entry: {item}")

            if not valid_data_tuples:
                print("Error: No valid (numeric_weight, datetime) entries found after filtering.")
                ax.clear()
                ax.text(0.5, 0.5, 'No valid weight data points', ha='center', va='center', color='orange', fontsize=10)
                ax.set_title("Évolution du Poids")
                ax.set_xlabel("Date")
                ax.set_ylabel("Poids (unité)")
                ax.set_xticks([])
                ax.set_yticks([])
                return

            # Sort valid data by DATE (the second element, index 1)
            sorted_journees = sorted(valid_data_tuples, key=lambda x: x[1])

            # Separate dates and weights from the sorted, valid list
            dates = [item[1] for item in sorted_journees]
            weights = [item[0] for item in sorted_journees]

        except (TypeError, IndexError) as e:
            print(f"Error processing or sorting weight data: {e}")
            print(f"Sample data: {self.info.historique_poids_journee[:5]}")
            ax.clear()
            ax.text(0.5, 0.5, f'Error processing data:\n{e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Error")
            return
        except Exception as e:
            print(f"An unexpected error occurred during data preparation: {e}")
            ax.clear()
            ax.text(0.5, 0.5, f'Unexpected error:\n{e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Error")
            return

        # --- Plotting (on the provided ax) ---
        try:
            ax.clear()  # Clear previous content on the axes
            ax.plot(dates, weights, marker='o', linestyle='-', color='coral', label='Poids')  # Plot data

            # Format the plot
            ax.set_xlabel("Date")
            ax.set_ylabel("Poids (unité)")  # Specify unit (e.g., kg, lbs)
            ax.set_title("Évolution du Poids au Fil du Temps")
            ax.grid(True, linestyle='--', alpha=0.7)

            # Format the date axis
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            ax.figure.autofmt_xdate()  # Auto format date labels for readability

            # Optional: Add legend if needed
            # ax.legend()

            # Note: tight_layout() and show() should be called by the code *using* this method

        except Exception as e:
            print(f"An error occurred during plotting on the axes: {e}")
            ax.clear()
            ax.text(0.5, 0.5, f'Plotting error:\n{e}', ha='center', va='center', color='red', fontsize=9)
            ax.set_title("Évolution du Poids - Plot Error")


if __name__ == '__main__':

    test = GraphicUtilisateur()
    test.poid_journee(666)



