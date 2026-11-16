# AML_01 — Comprendre une prédiction avant de lancer un modèle

## À retenir

Une cible est la réponse observée ; une probabilité est une prévision ; un seuil transforme la prévision en décision.

## Objectif minimal

Identifier X, y et une prédiction sur une ligne, puis retrouver le fichier produit. Pas de changement d’hyperparamètre exigé avant cette vérification.

## Exemple à travailler ensemble

| Transaction | Vraie classe | Probabilité de fraude |
|---|---:|---:|
| A | 0 | 0,10 |
| B | 1 | 0,70 |
| C | 0 | 0,20 |
| D | 1 | 0,40 |
| E | 0 | 0,60 |
| F | 0 | 0,05 |

Convention : alerte si probabilité ≥ 0,50. Faire la ligne A en entier : 0,10 < 0,50, donc pas d’alerte ; la cible vaut 0, c’est une bonne décision. Faire B ensemble. Laisser chacun compléter C à F avant toute discussion.

## Questions avant Python

1. Quelle différence entre la colonne cible et la colonne probabilité ?

Réponse : ........................................................................

2. Quelles transactions déclenchent une alerte ?

Réponse : ........................................................................

3. Combien de fraudes sont ratées ? Combien de fausses alertes ?

Réponse : ........................................................................

4. Pourquoi devons-nous soumettre des probabilités pour la compétition fraude ?

Réponse : ........................................................................

## Fiche de sortie

Je sais expliquer : …

Une sortie que je sais interpréter : …

Le point qui reste à reprendre : …
