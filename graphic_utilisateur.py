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

if __name__ == '__main__':
    g = GraphicUtilisateur()
    g.afficher_utilisateur()