from Seance import Seance
from ExerciceMusculation import ExerciceMusculation
from datetime import datetime
from NutritionQuotidien import NutritionQuotidien



# Todo: changer les methode d'instance pour avor le format
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire


class Journee:
    def __init__(self,nom, date : datetime, poid_aujourdhui : float):
        #Todo : ajouter le poid lors de la journee
        self.nom = nom
        self.seances_ajourdhui = []
        self.nutrition_aujourdhui = []
        self.poid_aujourdhui = poid_aujourdhui
        if datetime.now() > date and isinstance(date, datetime):
            self.date = date
        else:
            raise ValueError("date ne peux pas etre dans le futur")
        self.date_creation = datetime.today()

    def ajouter_seance(self, seance: Seance):
        self.seances_ajourdhui.append(seance)

    def afficher_exercice(self):
        for exercices in self.seances_ajourdhui:
            for exercice in exercices.exercice_seaces:
                print(exercice._nom_exercice)
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
            

   # TODO: ajouter une vérification de date dans le format datetime
