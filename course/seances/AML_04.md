# AML_04 - Comprendre la boucle d’un réseau

Conception pédagogique : Mathieu Weill.

## Objectif

Distinguer forward, perte, gradients et mise à jour ; vérifier le rechargement.

## Avant de commencer

Les tableaux numériques, les pertes et les comparaisons de modèles. Reformuler cet acquis avec un exemple ; si un mot bloque, le signaler avant le premier calcul.

## Les supports à utiliser

- [Notebook](../../usecase/MyLittleMLLab/notebooks/AML_04_atelier.ipynb).
- [Guide de démarrage](../../usecase/MyLittleMLLab/DEMARRER_J4.md).
- [Cours rédigé](../../usecase/MyLittleMLLab/lectures/AML_04_cours.md).
- PowerPoint étudiant dédié : pas encore publié pour cette fiche.
- PDF de cours étudiant dédié : pas encore publié pour cette fiche.

Les compléments thématiques ne sont pas présentés comme synchronisés cellule par cellule. Le PDF de projection J1 est un support de slides, distinct d’un chapitre rédigé.

## Le parcours accompagné

1. Lire la question et annoncer ce que représente une ligne, une entrée ou un tenseur.
2. Suivre la première démonstration du professeur et prévoir une sortie avant exécution.
3. Exécuter les cellules dans l’ordre, avec un arrêt au point indiqué en séance.
4. Écrire une observation précise et son interprétation ; traiter une difficulté à la fois.
5. Conserver le livrable et rédiger une limite avant de passer à l’extension.

## Vérifier que l’étape est comprise

Après backward, les poids sont-ils forcément modifiés ? Pourquoi un grand learning rate peut-il faire augmenter la perte ?

Cette question sert au diagnostic ; sa correction est donnée par le professeur. Les exemples résolus du cours restent distincts des exercices à rendre.

## Ce que je conserve

Une réponse personnelle, la sortie qui l’appuie et une limite. Pour un entraînement, ajouter protocole, configuration et durée. Les fichiers à rendre et leur format sont ceux annoncés en séance ; ne pas inventer une soumission Kaggle ou un score attendu.

## Si je bloque

Consulter le [guide de dépannage](../AIDE.md). Noter la cellule, le message exact et le résultat attendu. Ne pas supprimer l’erreur en changeant plusieurs paramètres au hasard.

## La suite

Les représentations préentraînées en NLP et vision utiliseront la même boucle et les mêmes contrôles.

[Retour au catalogue](../CATALOGUE.md)
