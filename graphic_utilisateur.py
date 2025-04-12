import pickle

from Utilisateur import Utilisateur
class GraphicUtilisateur:
    def __init__(self):
        with open("Utilisateurs.pkl", "rb") as f:
            self.info = pickle.load(f)
    def afficher_utilisateur(self):
        print(self.info)
    # graph poid et le temps
    # exercice les réaliser fait
    def poid_journee(self):
        self.info.actualiser_data_poid_jours()
        sorted_journees = sorted(self.info.historique_poids_journee, key=lambda x: x[1])
        print(sorted_journees)
    # graphique volume de la sessions
if __name__ == '__main__':
    g = GraphicUtilisateur()
    g.poid_journee()