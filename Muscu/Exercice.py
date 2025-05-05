from .Mouvement import Mouvement
from .MouvementType import MouvementType
from .Muscledispo import Muscledispo
import pickle
from pathlib import Path
from collections import Counter

class Exercice:

    try:
        file_path = Path(__file__).resolve().parent.parent / "mouvement_disponible.pkl"

        with open(file_path, "rb") as f:
            MOUVEMENT_dispo = pickle.load(f)

    except FileNotFoundError:
        MOUVEMENT_dispo = {}

    def __init__(self, nom_exercice: str):
        self.nomexercice = nom_exercice
    @property
    def nomexercice(self):
        return self._nom_exercice

    @nomexercice.setter
    def nomexercice(self, nom_exercice):
        if nom_exercice in Exercice.MOUVEMENT_dispo.keys():
            self._nom_exercice = nom_exercice
        else:
            raise ValueError(f"Cet exercice n'est pas valide. Veuillez l'ajouter à la liste.")

    @classmethod
    def ajouter_mouvement_disponible(cls, nom: str, description: str, muscle_cibles: list, type_exercice: str):
        """
        cree un nouveau mouvement disponible
        :param nom:
        :param description:
        :param muscle_cibles:
        :param type_exercice:
        :return: None
        """

        if nom in cls.MOUVEMENT_dispo.keys():
            raise ValueError("Le mouvement existe deja.")
        if len(muscle_cibles) < 1:
            raise ValueError("Il faut au moins un muscle ciblé.")

        for muscle_check in muscle_cibles:
            if muscle_check not in [muscle.value for muscle in Muscledispo]:
                muscle_invalide = muscle_check
                raise ValueError(f"Ce muscle n'est pas valide. {muscle_invalide}")
        counter = Counter(muscle_cibles)
        if not all(count == 1 for count in counter.values()):
            raise ValueError("Un muscle ne peut être ciblé qu'une seule fois.")

        if type_exercice not in [mouvement.value for mouvement in MouvementType]:
            raise ValueError("Le type est Cardio ou Musculation")
        else:
            # TODO: faire que ca crée un objet Mouvement là
            cls.MOUVEMENT_dispo[nom] = Mouvement(
                name=nom,
                description=description,
                muscle=muscle_cibles,
                type=type_exercice
            )

    @classmethod
    def supprimer_mouvement_disponible(cls, nom: str):
        """
        supprime un mouvement a l'aide de son nom en regardant si il est dans la liste de mouvement
        :param nom:
        :return:
        """
        if nom in cls.MOUVEMENT_dispo:
            del cls.MOUVEMENT_dispo[nom]
        else:
            raise ValueError("Le mouvement n'existe pas.")

    @classmethod
    def sauvegarder_mouvement_disponible(cls):
        """
        sauvegarde les mouvements disponibles
        :return:
        """
        with open(cls.file_path, "wb") as f:
            pickle.dump(cls.MOUVEMENT_dispo, f)

    def __str__(self):
        return f"Exercice : {self.nomexercice} "
