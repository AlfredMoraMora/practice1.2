import random

class Surfeur:
    """
    Classe qui représente un surfeur avec son nom et sa chance de survie

    - À sa création, le surfeur a une chance de survie de 0,5
    - Lorsqu'un surfeur se fait attaquer, la méthode survit_attaque retourne si le surfeur survit, selon la probabilité de survie
    - Si le surfeur survit à l'attaque, sa chance de survie augmente de 0,1

    """

    def __init__(self, nom: str = "Bob"):
        self._nom = nom
        self.chance_survie = 0.5

    @property
    def nom(self):
        return self._nom

    @property
    def chance_survie(self):
        return self._chance_survie

    @chance_survie.setter
    def chance_survie(self, valeur):
        if valeur < 0 or  valeur > 1:
            raise ValueError("La chance de survie est un nombre entre 0 et 1")
        self._chance_survie = valeur

    def survit_attaque(self):
        """
        Retourne si le surfeur survit, selon la probabilité de survie.
        Si le surfeur survit à l'attaque, sa chance de survie augmente de 0,1

        :return: True si le surfeur survit, False sinon
        """
        # TODO : compléter/corriger le code fourni (env 10 min)
        if random.random() < self.chance_survie:
            print("Le surfeur/se survit!")
            self._chance_survie += 0.1
            return True
        else:
            print("Le surfeur/se est mort/e! Womp womp...")
            return False

    def __str__(self):
        return f"Nom du surfeur/se {self._nom}"

