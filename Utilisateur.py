from Journee import Journee
import pickle
# Todo: changer les methode d'instance pour avor le format
# Todo: ajout de jsonpickle pour sauvegarder les progrès de l'utilisateur
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire

class Utilisateur:
    def __init__(self, nom : str,taille: int, age: int, poid:float,genre:str):
        self.nom = nom
        self.taille = taille
        self.age = age
        #Todo : tracker le poid de l'utilisateur lorsqu'il change avec la date
        self.poid = poid
        self.historique_journee = []
        self.historique_poids_journee = []

        self.genre = genre

        self.personal_record = {

                }

    def actualiser_data_poid_jours(self):
        # passer a travers toutes les journee pour mettre toutes les donne de chaque journee
        liste_date_journee = []
        for journee in self.historique_journee:
            tupledate_poid = (journee.poid_aujourdhui, journee.date)
            liste_date_journee.append(tupledate_poid)
        self.historique_poids_journee = liste_date_journee

    def actualiser_pr(self):
        pass

    def mettre_a_jours_pr(self,journee:Journee):
        infojournee = journee.obtenir_exercices_info()
        for exercice in infojournee:
            if exercice["nom"] not in self.personal_record.keys():
                print(exercice["nom"], "a ete ajouter au personal record")
                self.personal_record[exercice["nom"]] = exercice["poid_kg"]

            elif exercice["nom"] in self.personal_record.keys():
                if exercice["poid_kg"] > self.personal_record[exercice["nom"]]:
                    print("le pr a agmenter felicitation :)")
                    self.personal_record[exercice["nom"]] = exercice["poid_kg"]
                else:
                    print("rien na changer dans pr")
    def ajouter_journee(self, journee:Journee):
        #TODO : cette methode contiens deux fonctionnaliter change la
        # changer le poid parce que poid va etre dans journee
        # de la maniere que pr a ete charger mais le faire dans un liste
        # historique de poid liste de tuple (date: poid)
        if isinstance(journee, Journee):
            self.historique_journee.append(journee)
            self.mettre_a_jours_pr(journee)

        else:
            raise ValueError("journee n'est pas une instance de Journee")


    def obtenir_exercices_info(self):
        exercices_liste = []
        # peut etre ameliorer
        for journee in self.historique_journee:
            for seance in journee.seances_ajourdhui:
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
    def sauvegarder_utilisateur(self):
        with open("Utilisateurs.pkl", "wb") as f:
            pickle.dump(self, f)
    def __str__(self):
        return f"Nom : {self.nom}\ntaille : {self.taille}\nage:  {self.age} \npoid: {self.poid} lbs"


