import pickle
from datetime import timedelta, datetime
from Muscu import ExerciceMusculation, Seance, Exercice, ExerciceCardio
from Utilisateur import Utilisateur
from Journee import Journee
from graphic_utilisateur import GraphicUtilisateur

if __name__ == '__main__':

    ExerciceCardio("fgfff",5,5,5)
"""
    User12 = Utilisateur("test", 199,23,241,"homme")
    holy = datetime.today()
    holy -= timedelta(days = 1)
    journee_aujourd = Journee("yolo", datetime.today() - timedelta(days=5),150)

    seance_aujourd = Seance("journee_aujourd", )

    User12.ajouter_journee(journee_aujourd)
    User12.sauvegarder_utilisateur()

    Exercice.ajouter_mouvement_disponible("cacaaaa", "aaa",["Pectoraux"],"musculation")
    Exercice.sauvegarder_mouvement_disponible()
"""