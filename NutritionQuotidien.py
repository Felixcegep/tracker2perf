import pickle
from Aliment import Aliment
class NutritionQuotidien:

    with open("aliment_disponible.pkl", "rb") as f:
        ALIMENT_dispo = pickle.load(f)

    def __init__(self):
        pass

    @classmethod
    def ajouter_aliment_disponible(cls, nom, proteines, calories):
        if nom in cls.ALIMENT_dispo.keys():
            raise ValueError("Cet aliment est deja dans la liste.")
        else:
            cls.ALIMENT_dispo[nom] = Aliment(nom, proteines, calories)
    @classmethod
    def supprimer_aliment_disponible(cls, nom):
        if nom in cls.ALIMENT_dispo.keys():
            del cls.ALIMENT_dispo[nom]
        else:
            raise ValueError("Cet aliment est n'est pas dans la liste.")

    @classmethod
    def sauvegarder_aliment_disponible(cls):
        with open("aliment_disponible.pkl", "wb") as f:
            pickle.dump(cls.ALIMENT_dispo, f)








