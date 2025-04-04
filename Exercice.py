import pickle # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
from Mouvement import Mouvement
class Exercice:
    # Todo: sauvegarder le json pour l'utilisateur
    # Todo: ajouter les musclecible disponible
    # Todo: supprimer un mouvement
    # Todo: verifier snake_case pour nom de variable
    # Todo: faire des test unitaire
    #Todo : faire une classe mouvement

    # TODO: faire que ca l'ouvre un fichier jsonpickle
    with open("mouvement_disponible.pkl", "rb") as f:
        MOUVEMENT_dispo = pickle.load(f)
    type_valide = ["cardio","musculation"]


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
            raise ValueError(f"Exercice '{nom_exercice}' n'est pas valide. Veuillez l'ajouter à la liste.")

    @classmethod
    def ajouter_mouvement_disponible(cls,nom:str, description:str, muscle_cibles:list,type_exercice:str):
        #Todo : dans liste muscles cibles existe
        #Todo : changer if type_exercice not in ["cardio", "muscu"] pour quelque chose de mieux
        if nom in cls.MOUVEMENT_dispo.keys():
            raise ValueError("le mouvement existe deja")
        if len(muscle_cibles) < 1:
            raise ValueError("il faut au moins une muscle cible")
        for muscle in muscle_cibles:
            if type(muscle) != str:
                raise ValueError("les muscle sont des string")
        if type_exercice not in cls.type_valide:
            raise ValueError("le type est sois cardio ou muscu")
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