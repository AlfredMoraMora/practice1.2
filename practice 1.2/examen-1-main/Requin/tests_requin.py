import pytest

from Poisson import Poisson
from Requin import Requin
from Surfeur import Surfeur


# def test_surfeur_survit_attaque_augmente_survie(monkeypatch):
#     # Forcer le surfeur à survivre
#     monkeypatch.setattr('random.random', lambda: 0)
#     surfeur = Surfeur()
#     requin = Requin()
#     chance_avant = surfeur.chance_survie
#     requin.mords(surfeur)
#     assert surfeur.chance_survie == chance_avant + 0.1

# def test_requin_attaque_augmente_dangerosite():
#     surfeur = Surfeur()
#     # Forcer le surfeur à succomber
#     surfeur.chance_survie = 0
#     requin = Requin()
#     danger_avant = requin.dangerosite
#     requin.mords(surfeur)
#     assert requin.dangerosite == danger_avant + 1
#
# def test_creation_requin():
#     requin = Requin()
#     assert str(requin) == "Bob est un requin-tigre de 150g. Son niveau de dangerosité est évalué à 1"
#
# def test_requin_mange_poisson_augmente_poids():
#     poissons = [Poisson(poids=100), Poisson(poids=100)]
#     requin = Requin()
#     poids_avant = requin.poids
#     requin.mange(poissons)
#     assert requin.poids == poids_avant + 160
#
def test_requin_mange_poisson_toxique_poids_inchange():
    poissons = [Poisson(), Poisson(toxique=True)]
    requin = Requin()
    poids_avant = requin.poids
    requin.mange(poissons)
    assert requin.poids == poids_avant