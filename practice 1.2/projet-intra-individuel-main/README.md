[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KmqJCl-o)
[TOC]

# Projet de session

## Présentation
### Description du projet
Décrire le projet en environ 1 paragraphe. Quel est votre sujet ? Quelles sont les fonctionnalités principales ?

Le projet consiste à créer une interface sur QTdesign pour un programme en python qui faira le suivi d'un budget mensuel. 

### Membres de l'équipe et division des tâches
- **ui_appli_budget.py**: Code UI généré à partir de Qt Designer (PySide6). Responsable: Hernan Moraga.
- **main_with_ui.py**: Logique de base de l'application. Responsable: Hernan Moraga.
- **appli_budget.ui**: Fichier UI Qt Designer. Responsable: Hernan Moraga.

## Conception

### Diagramme de classes

````mermaid
classDiagram
    class MainWindow {
        -ui: Ui_MainWindow
        -budget: BudgetManager
        +add_transaction()
        +supprimer_transaction()
        +save_to_file()
        +load_from_file()
        +clearFields()
        +mettre_a_jour_total()
    }

    class Transaction {
        -date: str
        -montant: float
        -categorie: str
        -description: str
    }

    class BudgetManager {
        -transactions: list[Transaction]
        -total_depenses: float
        +ajouter_transaction(transaction: Transaction)
        +supprimer_transaction(index: int)
        +calculer_total_depense(): float
        +get_transactions(): list[Transaction]
    }

    MainWindow --> Ui_MainWindow : utilise
    MainWindow --> BudgetManager : utilise
    BudgetManager --> Transaction : gère
````

### Diagramme de cas d'utilisation

````mermaid
%% LR : gauche à droite (left-right)
flowchart LR
    %% Acteurs
    UUtilisateur["👤 Utilisateur"]

    %% Liens entre acteur et cas d'utilisation
    UUtilisateur --> CasAjouterTransaction
    UUtilisateur --> CasSupprimerTransaction
    UUtilisateur --> CasSauvegarderTransactions
    UUtilisateur --> CasChargerTransactions
    UUtilisateur --> CasEffacerChamps
    UUtilisateur --> CasMettreAJourTotal

    subgraph Système de gestion de budget
    %% TB : haut en bas (top-bottom)
    direction TB

    %% Cas d'utilisation
    CasAjouterTransaction(["Ajouter une transaction"])
    CasSupprimerTransaction(["Supprimer une transaction"])
    CasSauvegarderTransactions(["Sauvegarder les transactions"])
    CasChargerTransactions(["Charger les transactions"])
    CasEffacerChamps(["Effacer les champs"])
    CasMettreAJourTotal(["Mettre à jour le total"])

    %% Relations entre cas d'utilisation
    CasAjouterTransaction -. << include >> .-> CasMettreAJourTotal
    CasSupprimerTransaction -. << include >> .-> CasMettreAJourTotal
    CasSauvegarderTransactions -. << include >> .-> CasMettreAJourTotal
    CasChargerTransactions -. << include >> .-> CasMettreAJourTotal
    CasEffacerChamps(["Effacer les champs"]) -. << include >> .-> CasMettreAJourTotal
    end
````

## Avancement et vérification des exigences
Vous pouvez ajouter des numéros de billets et ajouter des éléments. L'objectif est de vous aider à faire la gestion de votre projet.

### Documentation et organisation du code
- [ ] Documentation de la personne responsable de chaque fichier
- [ ] Documentation du code
- [ ] Remise des diagrammes dans le projet
- [ ] Organisation du code à l'aide d'au moins 2 _packages_

### Orienté-objet
- [ ] Diagramme de classes
- [ ] Au moins 3 classes qui entrent en relation 
- [ ] Au moins 3 propriétés par classe
- [ ] Utilisation de l’héritage
- [ ] Utilisation des accesseurs et des mutateurs
- [ ] Utilisation d’au moins une exception personnalisée par personne

### Logique applicative
- [ ] Diagramme de cas d'utilisation
- [ ] Créer, modifier et supprimer différents objets
- [ ] Afficher des objets selon leur relation avec d’autres objets 
-	[ ] Manipuler des dates
- [ ] Valider adéquatement les données
- [ ] Enregistrer les données
- [ ] Charger les données au lancement de l’application

### Interface graphique
- [ ] Planification/ébauche
- [ ] La taille relative des éléments est logique
- [ ] Alignement adéquat des éléments graphiques
- [ ] Messages d’erreurs situés près des erreurs
- [ ] Confirmation des actions destructrices

### Contrôle de qualité
- [ ] Tests unitaires
- [ ] Appliquer les recommandations suite à la remise formative du 17 avril
- [ ] Appliquer les recommandations suite à la rétroaction par les pairs

