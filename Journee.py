from Seance import Seance
from ExerciceMusculation import ExerciceMusculation
from datetime import datetime



# Todo: changer les methode d'instance pour avor le format
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire


class Journee:
    def __init__(self,nom, date : datetime):
        self.nom = nom
        self.seances_ajourdhui = []
        self.nutrition_aujourdhui = []
        if datetime.now() > date:
            self.date = date
        else:
            raise ValueError("date ne peux pas etre dans le futur")
        self.date_creation = datetime.today()

    def ajouter_seance(self, seance: Seance):
        self.seances_ajourdhui.append(seance)

    def afficher_exercice(self):
        for exercices in self.seances_ajourdhui:
            for exercice in exercices.exercice_seaces:
                print(exercice.nomexercice)

    #def ajouter_nutrition(self, nutrition: Nutrition.NutritionQuotidien):
     #   self.nutrition_aujourdhui.append(nutrition)


   # TODO: ajouter une vérification de date dans le format datetime
exercice1 = ExerciceMusculation("test",1,1,1,1)
seance1 = Seance("test")
seance1.ajouter_exercice(exercice1)


