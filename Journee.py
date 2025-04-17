from Muscu import Seance
from datetime import datetime


# Todo: faire des test unitaire


class Journee:
    def __init__(self,nom, date : datetime, poid_aujourdhui : float):
        #Todo : ajouter le poid lors de la journee
        self.nom = nom
        self.seances_ajourdhui = []
        self.nutrition_aujourdhui = []
        self.poid_aujourdhui = poid_aujourdhui
        self.date = date        
        self.date_creation = datetime.today()
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if datetime.now() >= date and isinstance(date, datetime):
            self._date = date
        else:
            raise ValueError("date ne peux pas etre dans le futur et doit etre de format datetime")
    @property
    def poid_aujourdhui(self):
        return self._poid_aujourdhui

    @poid_aujourdhui.setter
    def poid_aujourdhui(self, poid_aujourdhui):
        if poid_aujourdhui > 0:
            self._poid_aujourdhui = poid_aujourdhui
        else:
            raise ValueError("le poid doit etre superieur a 0")
            
    def ajouter_nutrition_quotidienne(self, nutrition_quotidienne):
        self.nutrition_aujourdhui.append(nutrition_quotidienne)

    def ajouter_seance(self, seance: Seance):
        self.seances_ajourdhui.append(seance)

    def afficher_exercice(self):
        for exercices in self.seances_ajourdhui:
            for exercice in exercices.exercice_seaces:
                print(exercice.nomexercice)
    def obtenir_exercices_info(self):
        exercices_liste = []

        for seance in self.seances_ajourdhui:
            for exercice in seance.exercice_seaces:
                exercice_individuel = {
                    "nom" : exercice.nomexercice,
                    "rpe" : exercice.rpe,
                    "set" : exercice.set,
                    "rep" : exercice.rep,
                    "poid_kg" : exercice.poid_kg,
                        
                    }
    

                exercices_liste.append(exercice_individuel)
        return exercices_liste

    #def ajouter_nutrition(self, nutrition: NutritionQuotidien):
    #    self.nutrition_aujourdhui.append(nutrition)
            

