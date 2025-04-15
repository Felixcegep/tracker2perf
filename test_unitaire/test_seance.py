from Muscu.Exercice import Exercice
from Muscu.ExerciceMusculation import ExerciceMusculation
from Muscu.Seance import Seance


def test_seanche_volume_par_seance():
    Exercice.ajouter_mouvement_disponible("test","test",["Pectoraux"], "musculation")
    exercice1 = ExerciceMusculation("test",5,5,5,5)
    seance1 = Seance("test")
    seance1.ajouter_exercice(exercice1)
    assert seance1.volume_par_seance() == 125
    exercice2 = ExerciceMusculation("test", 5, 5, 5, 5)
    seance1.ajouter_exercice(exercice2)
    assert seance1.volume_par_seance() == 250

def test_ajouter_exercice():
    exercice1 = ExerciceMusculation("test", 5, 5, 5, 5)
    seance1 = Seance("test")
    assert len(seance1.exercice_seaces) == 0
    seance1.ajouter_exercice(exercice1)
    assert len(seance1.exercice_seaces) == 1


def test_supprimer_exercice():
    exercice1 = ExerciceMusculation("test", 5, 5, 5, 5)
    seance1 = Seance("test")
    assert len(seance1.exercice_seaces) == 0
    seance1.ajouter_exercice(exercice1)
    assert len(seance1.exercice_seaces) == 1
    seance1.supprimer_exercice("test")
    assert len(seance1.exercice_seaces) == 0
