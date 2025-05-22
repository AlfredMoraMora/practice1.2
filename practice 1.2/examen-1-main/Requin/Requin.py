from Poisson import Poisson
from Surfeur import Surfeur

class Requin:
    """
    Classe représentant un requin avec un nom, une espèce, un poids et un niveau de dangerosité

    - Lors de sa naissance (création), le requin a une dangerosité de 1 et un poids de 150g. Ces propriétés ne sont pas modifiables à la création.
    - Si l'espèce du requin n'est pas spécifiée lors de sa naissance (création), l'espèce sera requin-tigre.

    Manger

    - Lorsque le requin mange un poisson, son poids augmente de 80% du poids du poisson (ex. si un requin mange un poisson
      de 100g, son poids augmentera de 80g)

    - Lorsqu'un requin mange un poisson toxique, tous les poissons avalés en même temps sont recrachés et le requin
      n'augmente pas de poids

    Mordre

    - Lorsqu'un requin mord un surfeur ou une surfeuse, cette personne tente de survivre. Si elle ne survit pas, le
      requin augmente de dangerosité (+1)

    """

    def __init__(self, nom: str = "Bob", espece:str = "requin-tigre") -> None:
        # TODO : compléter le constructeur selon l'énoncé (env. 5 min)
        self.nom = nom
        self.poids = 150
        self.dangerosite = 1
        self.espece = espece

    @property
    def poids(self):
        """
        Poids en g du requin.
        """
        return self._poids

    @poids.setter
    def poids(self, poids:float):
        self._poids = poids

    def mange(self, poissons: list[Poisson]) -> None:
        # TODO : compléter/corriger selon l'énoncé (env. 30 min)
        poids_initiale = self.poids
        poids_totale = poids_initiale
        poids_mange = 0
        for poisson in poissons: # J'ai un erreur de loguique et j'ai pris trop de temps à ne pas le corriger. Je passe au prochain.
            poids_mange += poisson.poids
            if poisson._toxique:
                print("Le requin a mangé un poisson toxique. Il crache le tout! ")
                break
            else:
                print(f"Le requin mange le poisson. Il augmente son poids à {poids_totale}. ")
                self.poids += poisson.poids * 0.8

    def mords(self, surfer) -> None:
        # TODO : compléter selon l'énoncé (env. 25 min)
        if surfer.survit_attaque():
            print("Le surfer a survit.")
        else:
            print("Le surfer est mort.")
            self.dangerosite += 1


    def __str__(self):
        # TODO : corriger/compléter (env. 10 min)
        return f"{self.nom} est un {self.espece} de {self.poids}g. Son niveau de dangerosité est évalué à {self.dangerosite}"


requin1 = Requin()
poissons = [Poisson(poids=100), Poisson(), Poisson()]
requin1.mange(poissons)