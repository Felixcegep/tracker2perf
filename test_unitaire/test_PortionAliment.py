import pytest
from Nourriture import PortionAliment
from Nourriture import TemplateAliment

def test_ajouter_aliment_disponible():
    poulet = TemplateAliment("poulet",25, 240)
    len_initiale = len(PortionAliment.ALIMENT_dispo)

    PortionAliment.ajouter_aliment_disponible(poulet,25,240)
    assert len(PortionAliment.ALIMENT_dispo) == len_initiale+1


def test_supprimer_aliment_disponible():
    yogourt_grec = TemplateAliment("yogourt", 70, 8)
    PortionAliment.ajouter_aliment_disponible(yogourt_grec,70,8)
    len_initiale = len(PortionAliment.ALIMENT_dispo)

    PortionAliment.supprimer_aliment_disponible(yogourt_grec)
    assert len(PortionAliment.ALIMENT_dispo) == len_initiale -1