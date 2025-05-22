class BaseTransaction:
    """Clase de base pour les transactions."""
    def __init__(self, date):
        self.date = date

class Transaction(BaseTransaction):
    """Classe qui hérite de BaseTransaction."""
    def __init__(self, date, montant, categorie, description):
        """Initialise une transaction."""
        super().__init__(date)
        self.montant = montant
        self.categorie = categorie
        self.description = description

    @property
    def montant(self):
        return self._montant

    @montant.setter
    def montant(self, value):
        if value <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = value

class InvalidTransactionError(Exception):
    """Exception levée pour une transaction invalide."""
    pass
