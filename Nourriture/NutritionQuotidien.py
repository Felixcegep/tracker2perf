import pickle
from .PortionAliment import PortionAliment
from  .TemplateAliment import TemplateAliment
from pathlib import Path

class NutritionQuotidien:

    try:
        file_path = Path(__file__).resolve().parent.parent / "mouvement_disponible.pkl"

        with open(file_path, "rb") as f:
            ALIMENT_dispo = pickle.load(f)
    except FileNotFoundError:
        ALIMENT_dispo = {}

    def __init__(self,nom):
        self.nom = nom
        self.aliment_ajourdhui = []

    def ajouter_aliment_ajourdhui(self,aliment_toutseul:PortionAliment):

        if isinstance(aliment_toutseul,PortionAliment):
            self.aliment_ajourdhui.append(aliment_toutseul)
        else:
            raise TypeError("Cet objet n'est pas valide.")

    def supprimer_aliment_ajourdhui(self):
        pass








