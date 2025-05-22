import pytest
from classes.budget_manager import BudgetManager
from classes.transaction import InvalidTransactionError

def test_ajouter_transaction_valide():
    manager = BudgetManager()
    manager.ajouter_transaction("2023-01-01", 50.0, "Nourriture", "Épicerie")
    assert len(manager.get_transactions()) == 1
    assert manager.calculer_total_depense() == 50.0

def test_ajouter_transaction_montant_negatif():
    manager = BudgetManager()
    with pytest.raises(InvalidTransactionError):
        manager.ajouter_transaction("2023-01-01", -10.0, "Nourriture", "Test")

def test_supprimer_transaction():
    manager = BudgetManager()
    manager.ajouter_transaction("2023-01-01", 50.0, "Nourriture", "Épicerie")
    manager.supprimer_transaction(0)
    assert len(manager.get_transactions()) == 0
    assert manager.calculer_total_depense() == 0.0

def test_supprimer_transaction_index_hors_limites():
    manager = BudgetManager()
    with pytest.raises(IndexError):
        manager.supprimer_transaction(0)

