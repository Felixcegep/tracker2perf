from Seance import Seance
from Exercice import Exercice
from Journee import Journee
from Genre import Genre
from datetime import datetime
import pickle
import enum
from ExerciceCardio import ExerciceCardio
from ExerciceMusculation import ExerciceMusculation
# Todo: changer les methode d'instance pour avor le format
# Todo: ajout de jsonpickle pour sauvegarder les progrès de l'utilisateur
# Todo: verifier snake_case pour nom de variable
# Todo: faire des test unitaire

class Utilisateur:
    nombre_utilisateur = 0
    try:
        with open("Utilisateurs.pkl", "rb") as f:
            Utilisateurs = pickle.load(f)
    except FileNotFoundError:
        ALIMENT_dispo = {}
    def __init__(self, nom : str,taille: int, age: int, poid:float,genre:str):
        self.nom = nom
        self.taille = taille
        self.age = age
        #Todo : tracker le poid de l'utilisateur lorsqu'il change avec la date
        self.poid = poid
        self.historique_journee = []

        self.genre = genre

        self.personal_record = {

                }

        Utilisateur.nombre_utilisateur += 1
    def actualiser_poid(self):
        # passer a travers toutes les journee pour mettre toutes les donne de chaque journee 
        # 
        pass
    
    def actualiser_pr(self):
        pass
        

    def ajouter_journee(self, journee:Journee):
        #TODO : cette methode contiens deux fonctionnaliter change la 
        # changer le poid parce que poid va etre dans journee
        # de la maniere que pr a ete charger mais le faire dans un liste 
        # historique de poid liste de tuple (date: poid)
        if isinstance(journee, Journee):
            self.historique_journee.append(journee)
            
            infojournee = journee.obtenir_exercices_info()
            for exercice in infojournee:
                if exercice["nom"] not in self.personal_record.keys():
                    print(exercice["nom"],"a ete ajouter au personal record")
                    self.personal_record[exercice["nom"]] = exercice["poid_kg"]
                
                elif exercice["nom"] in self.personal_record.keys():
                    if exercice["poid_kg"] > self.personal_record[exercice["nom"]]:
                        print("le pr a agmenter felicitation :)")
                        self.personal_record[exercice["nom"]] = exercice["poid_kg"]
                    else:
                        print("rien na changer dans pr")
        else:
            raise ValueError("journee n'est pas une instance de Journee")
                
    @classmethod
    def afficher_total_utilisateur(cls):
        print(cls.nombre_utilisateur)
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
            pickle.dump(self.Utilisateurs, f)
    def __str__(self):
        return f"Nom : {self.nom}\ntaille : {self.taille}\nage:  {self.age} \npoid: {self.poid} lbs"


