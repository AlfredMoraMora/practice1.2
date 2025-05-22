
class Robot:
    """
    Classe représentant un robot avec des attributs de coût, force, vitesse et intelligence.
    """
    def __init__(self, nom: str, cout: int, force: int, vitesse: int, intelligence: int) -> None:
        self.nom = nom
        self.cout = cout
        self.force = force
        self.vitesse = vitesse
        self.intelligence = intelligence

    def __str__(self) -> str:
        return f"{self.nom} (Coût: {self.cout}, For: {self.force}, Vit: {self.vitesse}, Int: {self.intelligence})"