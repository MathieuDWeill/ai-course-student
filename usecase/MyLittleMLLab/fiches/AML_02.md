# AML_02 — Séparer apprendre, choisir et vérifier

## À retenir

Une évaluation devient trompeuse si la réponse ou une observation apparentée entre dans l’apprentissage.

## Objectif minimal

Expliquer sur son propre jeu ce qui pourrait traverser le split. Vérifier les IDs avant de calculer un score.

## Exemple à travailler ensemble

Dessiner trois boîtes : TRAIN → VALIDATION → TEST FINAL. Écrire sous chaque boîte : apprendre / choisir / vérifier une fois les choix fixés.

Écrire des observations A1, A2, A3, B1, B2, C1, C2, D1. Le groupe A correspond à une même source, pas à trois sources indépendantes.

Proposer TRAIN={A1,A2,B1,C1}, VALIDATION={A3,B2,C2,D1}. Entourer A, B et C de la même couleur de chaque côté. Demander : « Est-ce que nous évaluons vraiment sur de nouvelles sources ? »

Exemple temporel : origine juin, cible connue en août ; validation qui démarre en juillet. Dessiner les deux dates : une origine ancienne ne rend pas son label disponible plus tôt.

## Questions avant Python

1. Quel ensemble sert à apprendre le scaler ?

Réponse : ........................................................................

2. Pourquoi A1 et A3 peuvent-ils contaminer notre évaluation ?

Réponse : ........................................................................

3. Une ligne de juin avec un résultat connu en août peut-elle servir à décider en juillet ?

Réponse : ........................................................................

4. Que signifie une prédiction hors fold ?

Réponse : ........................................................................

## Fiche de sortie

Je sais expliquer : …

Une sortie que je sais interpréter : …

Le point qui reste à reprendre : …

## Repères concrets dans le notebook distribué

| Cellule | Ce que je dois pouvoir expliquer |
|---|---|
| 7 | Pourquoi A1 et A3 ont des IDs différents mais la même source |
| 24 | Pourquoi GroupKFold laisse zéro groupe partagé |
| 26 | Pourquoi Q et R ne sont pas utilisables au 1er juillet |
| 10 | Ce que vérifie l’intersection des IDs et ce qu’elle ne vérifie pas |
| 22 | Pourquoi 20 devient 265 quand on inclut indûment la validation |
| 13 | Quel modèle produit la prévision OOF d’une ligne donnée |
| 16 | Quel seuil respecte une capacité de 100 contrôles parmi les trois seuils testés |
| 28 | Pourquoi on garde les mêmes folds pour comparer C |
| 30 | Pourquoi une AUC de 1 peut provenir d’une évaluation invalide |
| 19 | Où se trouvent les fichiers qui prouvent mon calcul |

## Ma conclusion, avec mes valeurs

Sur le train local de … lignes, nous utilisons … folds. L’AUC moyenne des folds vaut … . La dispersion descriptive vaut … . Ce chiffre décrit … . Il ne prouve pas … .

Au seuil …, nous produisons … alertes, dont … vraies alertes, et nous ratons … fraudes. Le choix de ce seuil dépend de … .

Pour l’usage que nous visons, notre découpage devrait aussi contrôler … . La prochaine vérification serait … .

## Notre livrable Kaggle

- Tableau de comparaison sur les mêmes trois folds (cellule 32).
- Choix enregistré avant contrôle local (34, puis 36).
- Explication d’une erreur et du rôle du seuil (38).
- CSV contrôlé qui respecte sample_submission.csv (40).
- Journal avec le score public réellement reçu, ou None (42).

Avant le dépôt : pourquoi ce modèle ? Quel volume de train ? Quelle AUC CV ? Quels IDs dans le CSV ? Quelle expérience feriez-vous ensuite ?
