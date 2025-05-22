from .Carte import Carte

class Main_Joueur:
    _NOMBRE_CARTES = 0
    _MAX_CARTES = 5
    _MEILLEURE_MAIN = 0

    def __init__(self, main_joueur:list[Carte] = None):
        self._main_joueur = [] if main_joueur is None else main_joueur

    @property
    def main_joueur(self):
        return self._main_joueur

    def ajout_carte(self, carte:Carte) -> None:
        """
        Permet d'ajouter une carte à la main du joueur.
        :param carte: Carte
        :return: None
        """
        if isinstance(carte, Carte) and Main_Joueur._NOMBRE_CARTES <= Main_Joueur._MAX_CARTES:
            self.main_joueur.append(carte)
            Main_Joueur._NOMBRE_CARTES += 1
        else:
            raise TypeError("Carte n'est pas un carte")


    def piger_carte(self, carte:Carte):
        if carte not in self.main_joueur:
            raise TypeError("Carte n'est pas dans la main du joueur")
        else:
            self.main_joueur.remove(carte)

    def melanger(self):
        pass

    def valuer_totale(self):
        pass

