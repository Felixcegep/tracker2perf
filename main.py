import pickle
from datetime import timedelta, datetime
from ExerciceMusculation import ExerciceMusculation
from Utilisateur import Utilisateur
from Seance import Seance
from Journee import Journee
from Exercice import Exercice
if __name__ == '__main__':
    with open("Utilisateurs.pkl", "rb") as file:
        User12 = pickle.load(file)
    User12.actualiser_data_poid_jours()
    sorted_journees = sorted(User12.historique_poids_journee, key=lambda x: x[1])

    print(sorted_journees)
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