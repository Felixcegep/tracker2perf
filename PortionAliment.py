import pickle
import os
class PortionAliment:

    with open("aliment_disponible.pkl", "rb") as f:
        aliment = pickle.load(f)

    def __init__(self,nom,par_100_grammes):
        self.nom = nom
        self.par_100_grammes = par_100_grammes

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,value):
        if value in PortionAliment.aliment.keys():
            self._nom = value
        else:
            raise ValueError("Aliment non disponible, veuillez l'ajouter.")

    def __str__(self):
        return f'{self.nom} contient {self.par_100_grammes}'

