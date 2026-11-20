# Pauses de pop culture — Prédire et expliquer

Ces scénarios sont fictifs et servent à raisonner sur les notions du laboratoire. Ils ne décrivent pas les algorithmes réels des jeux ou services cités. Les illustrations sont projetées par le professeur.

Chacun écrit une prédiction et une justification avant la correction collective.

## J3 — Among Us · 90 % peut rater tous les imposteurs

Partie fictive : 10 joueurs, 1 imposteur.

Le détecteur répond toujours « innocent ».

Son accuracy ?
Son rappel des imposteurs ?

**Lien avec le laboratoire :** Le notebook de fraude travaille aussi sur une classe rare. Nous gardons la ROC-AUC pour le classement et examinons ensuite le rappel à un seuil.

## J3 — Pokédex maison · Décrire plutôt que mémoriser

Dans un petit historique :
2 créatures ailées portent la classe Air.

Une nouvelle créature a des ailes.

Quelle prédiction ?
Quelle incertitude ?

**Lien avec le laboratoire :** Revenir aux six montants et aux classes connues, puis vérifier le seuil réellement choisi dans la cellule 5.

## J3 — Conseil Jedi · Plusieurs avis, une prédiction

Trois scores hypothétiques :
0,2 ; 0,5 ; 0,8.

Quel score moyen ?

Et si les trois avis copient exactement la même source ?

**Lien avec le laboratoire :** Exécuter ensuite la cellule 9 : elle montre un bootstrap et la moyenne de trois arbres sur deux lignes.

## J3 — Mario Kart · Même piste pour comparer

Kart A gagne sur un circuit court.
Kart B gagne sur un circuit long.

Peut-on déclarer A meilleur ?

Que faudrait-il garder identique pour comparer une seule modification ?

**Lien avec le laboratoire :** Comparer les variantes log1p de la cellule 17, puis lire leurs différences sur chacun des trois folds.

## J4 — Celeste · Un grand pas peut dépasser la cible

On vise la plateforme du milieu.

Dans notre calcul : w = 2 et gradient = 30.

Avec un pas de 0,01 ?
Avec un pas de 1 ?

**Lien avec le laboratoire :** Poursuivre le calcul manuel et vérifier les valeurs dans la cellule 5, puis les rôles de backward et step dans la cellule 7.

## J4 — Iron Man · Ouvrir la boîte noire

Capteurs : les entrées.
Forward : les logits.
Perte : l’écart à une cible.
Backward : les gradients.
Step : la mise à jour.

Quelle étape change les poids ?

**Lien avec le laboratoire :** La cellule 9 affiche le petit batch et ses logits ; les cellules 11 et 13 montrent la perte puis la mise à jour de la matrice de poids.

## J4 — Soirée streaming · Des scores aux probabilités

Choix fictif entre 3 films.
Scores bruts A, B, C :
0 ; 2 ; 1.

Est-ce déjà une probabilité ?
Quel film arrive en tête ?
Que donnera softmax ?

**Lien avec le laboratoire :** Dans la cellule 11, refaire exactement le raisonnement sur les deux logits et les classes du petit batch. Fournir les logits directement à CrossEntropyLoss.

## J4 — Rocket League · Garder le meilleur replay

Le meilleur essai est le troisième.
Les suivants sont moins bons.

Garder le dernier ou le meilleur ?

En ML : selon quel critère, et sur quelles données ?

**Lien avec le laboratoire :** Après l’exercice sur les cinq pertes, la cellule 29 montre l’arrêt et le checkpoint réels de la démonstration, distincte du tournoi à huit epochs fixes.
