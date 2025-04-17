import pickle
from datetime import timedelta, datetime
from Muscu import ExerciceMusculation, Seance, Exercice
from Utilisateur import Utilisateur
from Journee import Journee
from graphic_utilisateur import GraphicUtilisateur
if __name__ == '__main__':
    date = "01/25/2025"
    with open("Utilisateurs.pkl", "rb") as f:
        data = pickle.load(f)
    indexvalide = -1
    for journee in data.historique_journee:
        indexvalide +=1
        if date == journee.date.strftime("%m/%d/%Y"):
            break
    print(data.historique_journee[indexvalide].date)




    #ExerciceMusculation("test", 9,9,9,9)
"""
    User12 = Utilisateur("test", 199,23,241,"homme")
    holy = datetime.today()
    holy -= timedelta(days = 1)
    journee_aujourd = Journee("yolo", holy,150)

    seance_aujourd = Seance("journee_aujourd", )

    
    seance_aujourd.ajouter_exercice(ExerciceMusculation("Développé couché", 5,5,5,5))
    seance_aujourd.ajouter_exercice (ExerciceMusculation("test",5,4,3,10))
    seance_aujourd.ajouter_exercice(ExerciceMusculation("test", 5, 4, 3, 16))
    journee_aujourd.ajouter_seance(seance_aujourd)
    User12.ajouter_journee(journee_aujourd)
    User12.sauvegarder_utilisateur()
"""
