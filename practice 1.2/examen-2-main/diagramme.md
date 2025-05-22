````mermaid
classDiagram

    class Carte {
        -valeur
        -couleur
        +obtenir_valeur()
        }

    class Paquet {
        _NOMBRE_CARTES = 52
        -paquet:list[Carte]
        -melange:bool = False
        +piger_carte()
        +afficher_cartes()
        
        }
    
    class Main_Joueur {
        _NOMBRE_CARTES = 0
        _MAX_CARTES = 5
        _MEILLEURE_MAIN = 0
        -main_joueur:list[Cartes]
        +melanger()
        +ajout_carte()
        +piger_carte()
        +valeur_totale()
    }
    
    Paquet "1" --> "N" Carte: a plusieurs
    Paquet "1" <--> "1" Main_Joueur: a max 5 cartes

````