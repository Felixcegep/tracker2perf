from Muscu.Exercice import Exercice


def test_Exercice_ajout():
    # verifier si l'ajout fonctionne
    assert len(Exercice.MOUVEMENT_dispo) == 0
    Exercice.ajouter_mouvement_disponible("test","description",["Pectoraux"],"musculation")
    assert len(Exercice.MOUVEMENT_dispo) == 1
    Exercice.ajouter_mouvement_disponible("test1","description",["Pectoraux"],"musculation")
    assert len(Exercice.MOUVEMENT_dispo) == 2

def test_supressions():
    # il y a actuellement 2 mouvement
    Exercice.supprimer_mouvement_disponible("test")
    assert len(Exercice.MOUVEMENT_dispo) == 1
    Exercice.supprimer_mouvement_disponible("test1")
    assert len(Exercice.MOUVEMENT_dispo) == 0