# Énoncé
1. Lire le contexte ci-dessous
2. Exécuter les tests fournis pour détecter les problèmes dans le code fourni
3. Compléter et corriger le code fourni (lire la documentation)
4. Exécuter les tests fournis pour vérifier l'implémentation. Vous pouvez ajouter des tests, mais ce n'est pas obligatoire.

## Contexte

````mermaid
classDiagram
    class Requin {
        - nom: string
        - espece: string
        - poids: float
        - dangerosité: int
        + mange(poissons: list[Poisson])
        + mords(surfeur: Surfeur)
    }
    class Poisson {
        - espece : string
        - poids: float
        - toxique: bool
    }
    class Surfeur {
        - nom: string
        - chance_survie: float
        + survit_attaque(): bool
    }
    Requin "1" --> "N" Poisson: mange
    Requin "1" --> "N" Surfeur: tente de manger (mords)
````

### Requin

- Lorsque le requin mange un poisson, son poids augmente de 80% du poids du poisson (ex. si un requin mange un poisson
  de 100g, son poids augmentera de 80g)
- Lorsqu'un requin mange un poisson toxique, tous les poissons avalés en même temps sont recrachés et le requin
  n'augmente pas de poids
- Lorsqu'un requin mord un surfeur ou une surfeuse, cette personne tente de survivre. Si elle ne survit pas, le
  requin augmente de dangerosité (+1)
- Lors de sa naissance (création), le requin a une dangerosité de 1 et un poids de 150g. Ces propriétés ne sont pas modifiables à la création.
- Si l'espèce du requin n'est pas spécifiée lors de sa naissance (création), l'espèce sera requin-tigre.

### Poisson
- Le poisson est par défaut une sardine (espèce) de 20 g non toxique

### Surfeur
- À sa création, le surfeur a une chance de survie de 0,5
- Lorsqu'un surfeur se fait attaquer, la méthode survit_attaque retourne si le surfeur survit, selon la probabilité de survie
- Si le surfeur survit à l'attaque, sa chance de survie augmente de 0,1

## Grille de correction
