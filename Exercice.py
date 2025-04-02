import json  # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
class Exercice:
    # Todo: sauvegarder le json pour l'utilisateur
    # Todo: ajouter les musclecible disponible
    # Todo: supprimer un mouvement
    # Todo: verifier snake_case pour nom de variable
    # Todo: faire des test unitaire
    with open("mouvementdisponible.json", "r") as f:
        mouvements = json.load(f)
    # Todo: ajout de sécuriter si il n'y a pas de fichier
    def __init__(self, nomexercice:str):
        if nomexercice in Exercice.mouvements:

            self._nomexercice = nomexercice
        else:
            raise ValueError("exercice invalide veuillez l'ajouter a liste d'exercices")

    @property
    def nomexercice(self):
        return self._nomexercice

    @nomexercice.setter
    def nomexercice(self, nomexercice):
        if nomexercice in Exercice.mouvements:
            self._nomexercice = nomexercice
        else:
            raise ValueError("mauvais reessais")



    @classmethod
    def ajouter_mouvement_disponible(cls,nom:str, description:str, muscle_cible:list):
        #Todo : dans liste muscles cibles existe
        if nom in cls.mouvements:
            raise ValueError("le mouvement existe deja")
        if len(muscle_cible) < 1:
            raise ValueError("il faut au moins une muscle cible")
        else:    
            cls.mouvements[nom] = {
                "description": description,
                "muscle_cible": muscle_cible

        }
        with open("mouvementdisponible.json", "w") as f:
            json.dump(cls.mouvements, f,indent=4)
    
    @classmethod
    def supprimer_mouvement_disponible(cls,nom:str):
        if nom in cls.mouvements:
            del cls.mouvements[nom]
            with open("mouvementdisponible.json", "w") as f:
                json.dump(cls.mouvements, f,indent=4)
        else:
            raise ValueError("le mouvement n'existe pas")
        




    def __str__(self):
        return f"nom de l'exercice : {self.nomexercice} "
Exercice.ajouter_mouvement_disponible("test","petit description", [])