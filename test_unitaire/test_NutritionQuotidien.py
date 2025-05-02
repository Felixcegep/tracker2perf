import pytest
from Nourriture import NutritionQuotidien, PortionAliment, TemplateAliment

def test_ajouter_aliment_disponible():

    lundi = NutritionQuotidien("lundi")
    len_initiale = len(lundi.aliment_ajourdhui)

    PortionAliment.ajouter_aliment_disponible("yaourt", 100, 100)
    NutritionQuotidien.ajouter_aliment_ajourdhui(lundi,PortionAliment("yaourt",150))

    assert len_initiale == len(lundi.aliment_ajourdhui)-1

def test_supprimer_aliment_disponible():

    lundi = NutritionQuotidien("lundi")

    NutritionQuotidien.ajouter_aliment_ajourdhui(lundi, PortionAliment("yaourt", 150))
    len_apres_ajout = len(lundi.aliment_ajourdhui)

    NutritionQuotidien.supprimer_aliment_ajourdhui(lundi, "yaourt")
    len_apres_supprimer = len(lundi.aliment_ajourdhui)

    assert len_apres_supprimer == len_apres_ajout-1

def test_sauvegarder_aliment_disponible():
    pass