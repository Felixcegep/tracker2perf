import json  # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
class Exercice:
    # Todo: sauvegarder le json pour l'utilisateur
    # Todo: ajouter les musclecible disponible
    # Todo: supprimer un mouvement
    # Todo: verifier snake_case pour nom de variable
    # Todo: faire des test unitaire

    with open("mouvementdisponible.json", "r") as f:
        _mouvements = json.load(f)
    # Todo: ajout de sécuriter si il n'y a pas de fichier
    def __init__(self, nom_exercice:str):
        if nom_exercice in Exercice._mouvements:

            self._nom_exercice = nom_exercice
        else:
            raise ValueError("exercice invalide veuillez l'ajouter a liste d'exercices")

    @property
    def nomexercice(self):
        return self._nom_exercice

    @nomexercice.setter
    def nomexercice(self, nom_exercice):
        if nom_exercice in Exercice._mouvements:
            self._nom_exercice = nom_exercice
        else:
            raise ValueError("mauvais reessais")



    @classmethod
    def ajouter_mouvement_disponible(cls,nom:str, description:str, muscle_cibles:list,type_exercice:str):
        #Todo : dans liste muscles cibles existe
        #Todo : changer if type_exercice not in ["cardio", "muscu"] pour quelque chose de mieux
        if nom in cls._mouvements:
            raise ValueError("le mouvement existe deja")
        if len(muscle_cibles) < 1:
            raise ValueError("il faut au moins une muscle cible")
        for muscle in muscle_cibles:
            if type(muscle) != str:
                raise ValueError("les muscle sont des string")
        if type_exercice not in ["cardio", "muscu"]:
            raise ValueError("le type est sois cardio ou muscu")
        else:    
            cls._mouvements[nom] = {
                "description": description,
                "muscle_cible": muscle_cibles,
                "type" : type_exercice

        }

    @classmethod
    def supprimer_mouvement_disponible(cls,nom:str):
        if nom in cls._mouvements:
            del cls._mouvements[nom]
        else:
            raise ValueError("le mouvement n'existe pas")
    @classmethod
    def sauvegarder_mouvement_disponible(cls):
        with open("mouvementdisponible.json", "w") as f:
            json.dump(cls._mouvements, f, indent=4)
        




    def __str__(self):
        return f"exercice : {self.nomexercice} "

