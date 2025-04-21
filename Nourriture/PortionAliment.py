import pickle
from pathlib import Path
from .TemplateAliment import TemplateAliment
class PortionAliment:
    file_path = Path(__file__).resolve().parent.parent / "aliment_disponible.pkl"
    try:

        with open(file_path, "rb") as f:
            ALIMENT_dispo = pickle.load(f)
    except FileNotFoundError:
        ALIMENT_dispo = {}

    def __init__(self,nom,par_100_grammes):
        self.nom = nom
        self.par_100_grammes = par_100_grammes

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,value):
        if value in PortionAliment.ALIMENT_dispo.keys():
            self._nom = value
        else:
            raise ValueError("Aliment non disponible, veuillez l'ajouter.")

    @property
    #probleme de logique
    def par_100_grammes(self):
        return self._par_100_grammes
    @par_100_grammes.setter
    def par_100_grammes(self,value:float):
        value = float(value)
        if isinstance(value,float) and value > 0:
            self._par_100_grammes = value
        else:
            raise ValueError("La valeur par 100 grammes doit etre un nombre positif. ")

    @classmethod
    def ajouter_aliment_disponible(cls, nom, proteines, calories):
        """
        Ajoute un aliment a la banque d'aliments disponibles
        :param nom:
        :param proteines:
        :param calories:
        :return: None
        """
        if nom in cls.ALIMENT_dispo.keys():
            raise ValueError("Cet aliment est deja dans la liste.")
        else:
            cls.ALIMENT_dispo[nom] = TemplateAliment(nom, proteines, calories)

    @classmethod
    def supprimer_aliment_disponible(cls, nom):
        """
        Retire un aliment de la banque d'aliments disponibles
        :param nom:
        :return: None
        """
        if nom in cls.ALIMENT_dispo.keys():
            del cls.ALIMENT_dispo[nom]
        else:
            raise ValueError("Cet aliment est n'est pas dans la liste.")

    @classmethod
    def sauvegarder_aliment_disponible(cls):
        """
        Met a jour la banque d'aliments disponible
        :return:
        """
        with open(cls.file_path, "wb") as f:
            pickle.dump(cls.ALIMENT_dispo, f)
    def __str__(self):
        return f"L'aliment : {self.nom} contient {self.par_100_grammes} grammes de ... par 100 grammes."

