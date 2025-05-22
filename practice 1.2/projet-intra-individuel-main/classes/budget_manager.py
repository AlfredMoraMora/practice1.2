from classes.transaction import Transaction, InvalidTransactionError

class BudgetManager:
    """Classe pour gérer les transactions et effectuer des calculs."""
    def __init__(self):
        self.transactions = []
        self.total_depenses = 0.0
        # self.nom_budget = "Budget Mensuel"

    def ajouter_transaction(self, date, montant, categorie, description):
        """
        Ajoute une transaction
        :param date: Date de la transaction
        :param montant: Montant de la transaction
        :param categorie: Categore de la transaction
        :param description: Description de la transaction
        :return: None
        """
        # Validation des données
        if montant <= 0:
            raise InvalidTransactionError("Le montant doit être positif.")
        if not description:
            raise InvalidTransactionError("Il faut ajouter une description.")
        if not categorie:
            raise InvalidTransactionError("Il faut choisir une categorie.")

        # Créer une nouvelle transaction et l'ajouter
        transaction = Transaction(date, montant, categorie, description)
        self.transactions.append(transaction)
        self.total_depenses += montant

    def supprimer_transaction(self, index):
        """
        Supprime une transaction à l'index donné.
        :param index: Index de la transaction à supprimer.
        """
        if index < 0 or index >= len(self.transactions):
            raise IndexError("Index de transaction hors limites.")

        # enlever du total
        self.total_depenses -= self.transactions[index].montant
        # supprimer la transaction
        self.transactions.pop(index)

    def calculer_total_depense(self):
        """
        Retourne le total des dépenses.
        :return: Total des dépenses (float)
        """
        return self.total_depenses

    def get_transactions(self):
        """
        Retourne la liste des transactions.
        :return: Liste des transactions (list)
        """
        return self.transactions