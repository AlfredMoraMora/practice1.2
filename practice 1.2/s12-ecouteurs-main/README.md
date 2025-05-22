# Modélisation Orientée Objet d'Écouteurs
## Objectif
Concevoir et implémenter un système en Python pour modéliser différents types d'écouteurs 
(casques, intra-auriculaires, etc.) avec leurs fonctionnalités spécifiques, 
en utilisant les principes de la programmation orientée objet, notamment l'héritage.

## Contexte
Le marché des écouteurs est vaste, allant des simples modèles filaires 
aux casques sans fil sophistiqués avec annulation de bruit active (ANC) et microphones intégrés. 
Votre tâche est de créer une structure de classes flexible et extensible pour représenter cette diversité.

# Les points communs et les différences
Tous les écouteurs, quel que soit leur type, partagent des caractéristiques et des actions fondamentales. 
Identifiez ces éléments communs et identifiez des fonctionnalités exclusives selon les types d'écouteurs.

- Contrôle du volume (augmentation, diminution). 
Pensez à définir des limites globales (minimum et maximum) pour le volume.

- Contrôle de la lecture (jouer, arrêter).

- Certains écouteurs ont des fonctionnalités optionnelles comme un microphone ou l'annulation de bruit (ANC). 
Prévoyez un moyen de savoir si un modèle possède ces fonctionnalités et si elles sont actives. 

## Le Monde Filaire
- Modélisez les écouteurs qui se connectent physiquement à un appareil.

- Quelle information spécifique est nécessaire pour un écouteur filaire par rapport à la base ?

- Comment ces écouteurs représentent-ils leur état de "connexion" ?

## L'Univers Sans Fil
Les écouteurs sans fil introduisent de nouvelles considérations.

- Gestion de l'énergie : Ils fonctionnent sur batterie.

- Connectivité : Ils doivent pouvoir se connecter et se déconnecter d'un appareil source.

- Impact des fonctionnalités : Pensez à l'impact de l'utilisation (lecture, ANC active) sur la batterie.

- Spécificités Sans Fil : Bluetooth & Wi-Fi
  - Bluetooth : Quelles informations supplémentaires sont nécessaires ? (Version, codecs audio supportés).
  - Wi-Fi : Ces écouteurs utilisent souvent un dongle USB. Quelles informations sont pertinentes ? (Bande de fréquence, portée).

## Organisation et Bonnes Pratiques
- Utilisez des Énumérations pour représenter les ensembles finis de valeurs.

- Structurez votre code en plusieurs fichiers logiques.

- Appliquez l'héritage de manière judicieuse pour réutiliser le code et modéliser les relations "est un type de".

- Utilisez des méthodes/attributs statiques ou de classe lorsque pertinent.

- Documentez votre code avec des docstrings.

- Utilisez les annotations de type (type hinting).

- Écrivez des tests unitaires avec pytest pour valider le comportement de vos classes 
(initialisation, actions de base, gestion de la batterie, connexion/déconnexion, activation des fonctionnalités, etc.).

## Livrables Attendus
- Les fichiers Python (.py) contenant les définitions des énumérations et des classes.

- Un fichier de tests (test_*.py) contenant les tests unitaires pytest.

- (Optionnel) Un petit script main.py démontrant l'utilisation de vos classes.

## Conseils
- référez-vous au diagramme de cas d'utilisation pour avoir une vue globale de projet.

- Commencez par la classe de base et ajoutez progressivement les spécialisations.

- Réfléchissez bien aux responsabilités de chaque classe.