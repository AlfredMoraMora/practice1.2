import sys
import jsonpickle
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QDate
from interface.ui_appli_budget import Ui_MainWindow
from classes.transaction import Transaction, InvalidTransactionError
from classes.budget_manager import BudgetManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ajout pour mettre en évidence les champs.
        self.setStyleSheet("""
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
                border: 2px solid red;
                background-color: lightyellow;
                }
        """)

        # Initialiser BudgetManager
        self.budget = BudgetManager()   # Créer objet qui gère les transactions



        self.mettre_a_jour_total()  # Mettre à 0 le total
        self.ui.dateEdit.setDate(QDate.currentDate())   # Mettre la date courrante par defaut

        # Connecter boutons aux fonctions
        self.ui.ajouterButton.clicked.connect(self.add_transaction)
        self.ui.sauvegarderButton.clicked.connect(self.save_to_file)
        self.ui.chargerButton.clicked.connect(self.load_from_file)
        self.ui.clearButton.clicked.connect(self.clearFields)
        self.ui.supprimerButton.clicked.connect(self.supprimer_transaction)

    def add_transaction(self):
        try:
            date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
            montant_text = float(self.ui.montantEdit.text().strip())
            montant = float(montant_text) if montant_text else 0.0
            categorie = self.ui.comboBox.currentText()
            description = self.ui.descriptionEdit.text()

            # valider que la date
            if self.ui.dateEdit.date() > QDate.currentDate():
                raise InvalidTransactionError("La date ne peut pas être dans le futur.")

            # Caller l'ajout à BudgetManager
            self.budget.ajouter_transaction(date, montant, categorie, description)

            # Ajouter les rangées au tableau
            row_count = self.ui.transactionsTable.rowCount()
            self.ui.transactionsTable.insertRow(row_count)
            self.ui.transactionsTable.setItem(row_count, 0, QTableWidgetItem(date))
            self.ui.transactionsTable.setItem(row_count, 1, QTableWidgetItem(f"{montant:.2f}"))
            self.ui.transactionsTable.setItem(row_count, 2, QTableWidgetItem(categorie))
            self.ui.transactionsTable.setItem(row_count, 3, QTableWidgetItem(description))

            # Clear some input fields
            self.ui.montantEdit.clear()
            self.ui.descriptionEdit.clear()

            # Mettre à jour total
            self.mettre_a_jour_total()

        except ValueError as e:
            QMessageBox.warning(self, "Erreur de saise", str(e) if str(e).startswith("Le") else
            "Veuillez entrer un montant valide.")

    def supprimer_transaction(self):
        """Supprime la transaction sélectionnée."""
        try:
            row = self.ui.transactionsTable.currentRow()
            if row >= 0:
                if QMessageBox.question(self, "Confirmation", "Voulez-vous supprimer cette transaction? ") == QMessageBox.Yes:
                    self.budget.supprimer_transaction(row)
                    self.ui.transactionsTable.removeRow(row)
                    self.mettre_a_jour_total()
            else:
                QMessageBox.warning(self, "Erreur", "Pas de transaction sélectionnée.")
        except IndexError as e:
            QMessageBox.warning(self, "Erreur", str(e))

    def save_to_file(self):
        """Sauvegarde les données entrées dans un fichier JSON"""
        try:
            with open('../documents/transactions.json', 'w', encoding='utf-8') as file:
                json_str = jsonpickle.encode(self.budget.transactions, indent = 4)
                file.write(json_str)
            QMessageBox.information(self, "Succès", "Transactions sauvegardées dans transactions.json")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec de la sauvegarde: {str(e)}" )

    def load_from_file(self):
        """Charge les données dans le fichier JSON"""
        try:
            with open('../documents/transactions.json', 'r', encoding='utf-8') as file:
                json_str = file.read()
                loaded_transactions = jsonpickle.decode(json_str)

            # Mettre à jour la liste des transactions. chatgpt fix. J'avais problème sans ces lignes
            self.budget.transactions = loaded_transactions
            self.budget.total_depenses = sum(t.montant for t in loaded_transactions)

            # Vider les valeurs et remplir le tableau. sugéré par IA
            self.ui.transactionsTable.setRowCount(0)
            for transaction in loaded_transactions:
                row_count = self.ui.transactionsTable.rowCount()
                self.ui.transactionsTable.insertRow(row_count)
                self.ui.transactionsTable.setItem(row_count, 0, QTableWidgetItem(transaction.date))
                self.ui.transactionsTable.setItem(row_count, 1, QTableWidgetItem(f"{transaction.montant:.2f}"))
                self.ui.transactionsTable.setItem(row_count, 2, QTableWidgetItem(transaction.categorie))
                self.ui.transactionsTable.setItem(row_count, 3, QTableWidgetItem(transaction.description))

            self.mettre_a_jour_total()
            QMessageBox.information(self, "Succès", "Transactions chargées depuis le fichier transactions.json")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec du chargement: {str(e)}")

    def clearFields(self):
        """Clears all input fields"""
        if QMessageBox.question(self, "Confirmation", "Voulez-vous tout effacer?") == QMessageBox.Yes:
            self.budget.transactions.clear()
            self.budget.total_depenses = 0.0
            self.ui.dateEdit.setDate(QDate.currentDate())
            self.ui.montantEdit.clear()
            self.ui.comboBox.setCurrentIndex(0)
            self.ui.descriptionEdit.clear()
            self.ui.transactionsTable.setRowCount(0)
            self.mettre_a_jour_total()

    def mettre_a_jour_total(self):
        """Met à jour le label qui affiche le total"""
        total = self.budget.calculer_total_depense()
        self.ui.totalLabel.setText(f"Total dépensé : {total: .2f} $")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())