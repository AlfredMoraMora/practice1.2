from .Carte import Carte
from .Valeurs import Valeurs
from .Couleurs import Couleurs

class Paquet(Carte):
    _NOMBRE_CARTES = 52

    def __init__(self,valeur: Valeurs, couleur: Couleurs, paquet:list[Carte], melange:bool = False):
        super().__init__(valeur, couleur)
        self._paquet = [] if paquet is None else paquet
        self.melange = melange

    @property
    def paquet(self):
        return self._paquet

    @property
    def melange(self):
        return self._melange

    @melange.setter
    def melange(self, value):
        if isinstance(value, bool):
            self._melange = value
        else:
            raise TypeError('Melange doit être un boolean')

    def piger_carte(self):
        pass

    def afficher_cartes(self):
        pass


