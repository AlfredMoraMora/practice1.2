class Tache:
    """
    Classe représentant une tâche avec des exigences de force, vitesse, intelligence et une récompense.
    """
    def __init__(self, nom: str, force_requise: int, vitesse_requise: int, intelligence_requise: int, recompense: int) -> None:
        self.nom = nom
        self.force_requise = force_requise
        self.vitesse_requise = vitesse_requise
        self.intelligence_requise = intelligence_requise
        self.recompense = recompense

    def __str__(self) -> str:
        return f"{self.nom} (Req: For {self.force_requise}, Vit {self.vitesse_requise}, Int {self.intelligence_requise}, Récompense: {self.recompense})"