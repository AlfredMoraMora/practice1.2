class Poisson:
    """
    Classe représentant un poisson avec son espèce, son poids et s'il est toxique pour un requin

    Le poisson est par défaut une sardine (espèce) de 20 g non toxique
    """

    def __init__(self, espece:str = "sardine", poids:float = 20, toxique:bool = False):
        # espece et toxique sont en lecture seule après initialisation
        self._espece = espece
        self._toxique = toxique
        self.poids = poids

    @property
    def espece(self):
        return self._espece

    @property
    def toxique(self):
        return self._toxique

    @property
    def poids(self):
        """
        Poids en g du poisson
        """
        return self._poids

    @poids.setter
    def poids(self, poids:float):
        if poids <= 0: raise ValueError("Le poids doit être plus grand que 0")
        self._poids = poids

# sape