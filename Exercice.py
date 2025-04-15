import pickle
from Mouvement import Mouvement
from MouvementType import MouvementType
from Muscledispo import Muscledispo

from collections import Counter
class Exercice:
    # Todo: faire des test unitaire
    # TODO: faire que ca l'ouvre un fichier jsonpickle
    try:
        with open("mouvement_disponible.pkl", "rb") as f:
            MOUVEMENT_dispo = pickle.load(f)
    except FileNotFoundError:
        MOUVEMENT_dispo = {}


    # Todo: ajout de sécuriter si il n'y a pas de fichier
    def __init__(self, nom_exercice:str):
        self.nomexercice = nom_exercice

    @property
    def nomexercice(self):
        return self._nom_exercice

    @nomexercice.setter
    def nomexercice(self, nom_exercice):
        if nom_exercice in Exercice.MOUVEMENT_dispo.keys():
            self._nom_exercice = nom_exercice
        else:
            raise ValueError(f"Exercice n'est pas valide. Veuillez l'ajouter à la liste.")

    @classmethod
    def ajouter_mouvement_disponible(cls,nom:str, description:str, muscle_cibles:list,type_exercice:str):
        #Todo : dans liste muscles cibles existe
        if nom in cls.MOUVEMENT_dispo.keys():
            raise ValueError("le mouvement existe deja")
        if len(muscle_cibles) < 1:
            raise ValueError("il faut au moins une muscle cible")

        for muscle_check in muscle_cibles:
            if muscle_check not in [muscle.value for muscle in Muscledispo]:
                muscle_invalide = muscle_check
                raise ValueError(f"ce muscle n'est pas valide{muscle_invalide}")
        counter = Counter(muscle_cibles)
        if not all(count == 1 for count in counter.values()):
            raise ValueError("un muscle peut seulement etre cibler une fois")

        if type_exercice not in [mouvement.value for mouvement in MouvementType]:
            raise ValueError("le type est sois cardio ou musculation")
        else:
            #TODO: faire que ca crée un objet Mouvement là
            cls.MOUVEMENT_dispo[nom] = Mouvement(
                name=nom,
                description=description,
                muscle=muscle_cibles,
                type=type_exercice
                    )

    @classmethod
    def supprimer_mouvement_disponible(cls,nom:str):
        if nom in cls.MOUVEMENT_dispo:
            del cls.MOUVEMENT_dispo[nom]
        else:
            raise ValueError("le mouvement n'existe pas")
    @classmethod
    def sauvegarder_mouvement_disponible(cls):
        with open("mouvement_disponible.pkl", "wb") as f:
            pickle.dump(cls.MOUVEMENT_dispo, f)
        




    def __str__(self):
        return f"exercice : {self.nomexercice} "
