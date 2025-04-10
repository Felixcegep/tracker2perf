import pickle
from PortionAliment import PortionAliment
from  TemplateAliment import TemplateAliment
class NutritionQuotidien:
    try:
        with open("aliment_disponible.pkl", "rb") as f:
            ALIMENT_dispo = pickle.load(f)
    except FileNotFoundError:
        ALIMENT_dispo = {}

    def __init__(self,nom):
        self.nom = nom
        self.aliment_ajourdhui = []

    def ajouter_aliment_ajourdhui(self,aliment_tousseule:PortionAliment):

        if isinstance(aliment_tousseule,PortionAliment):
            self.aliment_ajourdhui.append(aliment_tousseule)
        else:
            raise TypeError("cette objet n'est pas valide")







    @classmethod
    def ajouter_aliment_disponible(cls, nom, proteines, calories):
        if nom in cls.ALIMENT_dispo.keys():
            raise ValueError("Cet aliment est deja dans la liste.")
        else:
            cls.ALIMENT_dispo[nom] = TemplateAliment(nom, proteines, calories)
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






