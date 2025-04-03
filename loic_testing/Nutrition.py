from Utilisateur import Utilisateur

class Nutrition:
    def __init__(self, objectif:str):
        self.objectif = objectif
        super().__init__(Utilisateur)

    def objectif(self):
        self.objectif = input("Choisir un objectif (1,2,3)\n 1.Perte de poids\n2.Maintien\n3.Prise de masse")
        print(12)

    def apport_calorique_quotidien(self):
        pass

