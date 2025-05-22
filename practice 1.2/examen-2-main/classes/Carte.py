from .Valeurs import Valeurs
from .Couleurs import Couleurs

class Carte:
    def __init__(self, valeur:Valeurs, couleur:Couleurs):
        self._valeur = valeur
        self.couleur = couleur

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, value: Valeurs):
        if not isinstance(value, Valeurs):
            raise ValueError("La valuer doit être une instance de Valeurs")
        self._valeur = value

    @property
    def couleurs(self):
        return self._couleur

    @couleurs.setter
    def couleurs(self, value: Couleurs):
        if not isinstance(value, Couleurs):
            raise ValueError("La valeur doit être une instance de Couleurs")
        self._couleur = value

    def obtenir_valeur(self):
        return self._valeur

    def __str__(self):
        return f"{self.couleur} {self.valeur}"

carte1 = Carte(Valeurs.AS, Couleurs.TREFLE)
print(carte1.valeur)  # il y a problème/s.