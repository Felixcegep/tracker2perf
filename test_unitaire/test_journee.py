from Exercice import Exercice
from ExerciceCardio import ExerciceCardio
from ExerciceMusculation import ExerciceMusculation
from Seance import Seance
from Journee import Journee
import pytest
from datetime import datetime, timedelta

def test_ajouter_nutrition_quotidienne():

    pass
def test_ajouter_seance():
    # prend une seance et met des exercices a l'interieur et met a l'interieur de journee

    #creation d'un exercice et mit en objet

    Exercice.ajouter_mouvement_disponible("test", "test", ["Pectoraux"], "musculation")
    exercice1 = ExerciceMusculation("test", 5, 5, 5, 5)

    #cree seance et mettre exercice a l'interieur
    seance1 = Seance("test")
    seance1.ajouter_exercice(exercice1)

    journee1 = Journee("test",datetime.today() - timedelta(minutes=1), 150)
    assert len(journee1.seances_ajourdhui) == 0
    journee1.ajouter_seance(seance1)
    assert len(journee1.seances_ajourdhui) == 1

def test_obtenir_exercices_info():
    exercice1 = ExerciceMusculation("test", 5, 5, 5, 5)
    Exercice.ajouter_mouvement_disponible("wompwomp", "test", ["Pectoraux"], "musculation")
    #deuxieme
    exercice2 = ExerciceMusculation("wompwomp", 6, 6, 6, 6)
    # cree seance et mettre exercice a l'interieur
    seance1 = Seance("test")
    seance1.ajouter_exercice(exercice1)
    seance2 = Seance("test")
    seance2.ajouter_exercice(exercice2)
    journee1 = Journee("test", datetime.today() - timedelta(minutes=1), 150)
    journee1.ajouter_seance(seance1)

    assert journee1.obtenir_exercices_info() == [{'nom': 'test', 'rpe': 5, 'set': 5, 'rep': 5, 'poid_kg': 5}]
    journee1.ajouter_seance(seance2)
    assert journee1.obtenir_exercices_info() == [{'nom': 'test', 'rpe': 5, 'set': 5, 'rep': 5, 'poid_kg': 5}, {'nom': 'wompwomp', 'rpe': 6, 'set': 6, 'rep': 6, 'poid_kg': 6}]
