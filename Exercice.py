import json  # ajouter intensiter pour chaque exercices pour ensuite pouvoir la calculer dans séance
    # a l'aide d'un calcule
class Exercice:
    # Todo: sauvegarder le json pour l'utilisateur
    # Todo: ajouter les musclecible disponible
    # Todo: supprimer un mouvement

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
        cls.mouvements[nom] = {
            "description": description,
            "muscle_cible": muscle_cible

        }




    def __str__(self):
        return f"nom de l'exercice : {self.nomexercice} "

Exercice("bench")
Exercice.ajouter_mouvement_disponible("nom", "petite description", ["chest"])