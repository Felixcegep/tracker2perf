import pickle

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

    @property
    #probleme de logique
    def par_100_grammes(self):
        return self._par_100_grammes

    @par_100_grammes.setter
    def par_100_grammes(self,value:float):
        value = float(value)
        if isinstance(value,float) and value > 0:
            self._par_100_grammes = value
        #rajouter un elif pour raise les probleme plus clairement
        else:
            raise ValueError("La valeur par 100 grammes doit etre un nombre positif. ")


    def __str__(self):
        return f"L'aliment : {self.nom} contient {self.par_100_grammes} grammes de ... par 100 grammes."

