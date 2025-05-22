import pytest
from Tache import Tache
from Jeu import Jeu
from Robot import Robot


def test_acheter_robot_argent_suffisant():
    jeu = Jeu(argent_depart=300)
    robot = Robot("TestBot", 100, 5, 5, 5)
    jeu.acheter_robot(robot)
    assert robot in jeu.equipe
    assert jeu.argent == 200

def test_acheter_robot_argent_insuffisant():
    jeu = Jeu(argent_depart=50)
    robot = Robot("TestBot", 100, 5, 5, 5)
    jeu.acheter_robot(robot)
    assert robot not in jeu.equipe
    assert jeu.argent == 50

def test_tenter_tache_succes():
    jeu = Jeu(argent_depart=300)
    robot1 = Robot("TestBot1", 100, 5, 5, 5)
    robot2 = Robot("TestBot2", 100, 5, 5, 5)
    jeu.equipe = [robot1, robot2]
    tache = Tache("TestTache", 10, 10, 10, 100)
    assert jeu.tenter_tache(tache) == True


@pytest.mark.parametrize("equipe", [
    ( # Échec toutes les compétences
        [Robot("TestBot1", 100, 3, 3, 3),
        Robot("TestBot2", 100, 3, 3, 3)]
    ),
    ( # Échec intelligence
        [Robot("TestBot1", 100, 13, 13, 3),
        Robot("TestBot2", 100, 3, 3, 3)]
    ),
    ( # Échec vitesse
        [Robot("TestBot1", 100, 13, 3, 13),
        Robot("TestBot2", 100, 3, 3, 3)]
    ),
    ( # Échec force
        [Robot("TestBot1", 100, 3, 13, 13),
        Robot("TestBot2", 100, 3, 3, 3)]
    )
])
def test_tenter_tache_echec(equipe):
    jeu = Jeu(argent_depart=300)
    jeu.equipe = equipe
    tache = Tache("TestTache", 10, 10, 10, 100)
    assert jeu.tenter_tache(tache) == False
