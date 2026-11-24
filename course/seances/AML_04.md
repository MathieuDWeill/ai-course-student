# AML_04 - Comprendre la boucle d’un réseau

Conception pédagogique : Mathieu Weill.

**Comment les poids changent-ils pendant l’apprentissage ?**

## À ouvrir pendant le cours J4

**La présentation détaillée du professeur suit [AML_04_atelier.ipynb](../../usecase/MyLittleMLLab/notebooks/AML_04_atelier.ipynb), qui contient 38 cellules.** Les numéros annoncés en classe comptent aussi les cellules de texte.

1. Suivre les [consignes de préparation J4](../../usecase/MyLittleMLLab/DEMARRER_J4.md).
2. Placer le notebook dans `MyLittleMLLab/notebooks`, avec les données et l’environnement déjà utilisés en J1/J2.
3. Exécuter dans l’ordre, au signal du professeur. Après un redémarrage du noyau, reprendre les cellules précédentes.

Le petit notebook du socle ci-dessous sert à réviser les notions avec des exemples courts. Ses repères D1/D2 ne correspondent pas aux numéros de cellules de l’atelier.

## Le trio du chapitre

- [Guide de séance](../chapitres/AML_04/README.md)
- [PDF étudiant rédigé](../chapitres/AML_04/cours.pdf)
- [PowerPoint étudiant](../chapitres/AML_04/presentation.pptx)
- [Notebook guidé](../chapitres/AML_04/notebook.ipynb)

Les démonstrations D1 et D2, les exercices E1/E2 et le bilan B partagent les mêmes repères. Le PowerPoint contient 24 diapositives. La version étudiante ne contient ni notes de présentation professeur ni réponses réservées aux exercices.

## Application complémentaire

[Ouvrir l’atelier d’application](../../usecase/MyLittleMLLab/notebooks/AML_04_atelier.ipynb). Ce carnet est distinct du socle guidé. Les anciens repères numériques des ateliers et des projections détaillées sont conservés.

[Préparer les données et l’environnement de l’application](../../usecase/MyLittleMLLab/DEMARRER_J4.md).

## Réussite attendue

Tracer entrée, sortie, perte, gradient et mise à jour dans cet ordre logique.

## Avant de quitter la séance

Sans relire la correction, savoir :

- Décrire dans l’ordre : prédiction, perte, gradient, mise à jour des poids.
- Distinguer le calcul du gradient de la modification des poids et expliquer le rôle du taux d’apprentissage.
- Comparer le réseau à la référence avec le même protocole, même si le réseau gagne moins souvent.
- Montrer les fichiers de `runs/J4` et expliquer pourquoi les poids seuls ne suffisent pas à reproduire une prédiction.

Si un point bloque, noter la cellule concernée et demander une reprise avec le professeur. Un notebook exécuté ne suffit pas à prouver que ces étapes sont comprises.

## Vérification et limites

Le notebook du chapitre a été exécuté localement dans un noyau neuf. Les résultats des petits exemples ne constituent pas des scores Kaggle. L’atelier local AML_04 a également été exécuté entièrement dans un noyau neuf, sur CPU, avec les données officielles locales et une limite de 15 000 observations. Cette vérification ne couvre pas tous les PC/Mac ni une exécution authentifiée sur Kaggle. [Détail des vérifications](../VERIFICATION.md).

[Catalogue](../CATALOGUE.md) · [Aide](../AIDE.md)

## Rappel avant la séance

[Six diapositives de rappel accompagné](../../slides/ML_Avance_J4_Rappel_Etudiant.pptx) : répondre brièvement avant la correction orale. Ce support étudiant ne contient pas de notes professeur.

Pour les repères numériques de la présentation détaillée de classe, ouvrir **AML_04_atelier.ipynb** dans la rubrique Application complémentaire ci-dessus.

## Complément du syllabus

[AML_C1 — CNN : du filtre au classifieur](../complements/AML_C1/README.md) : Expliquer les dimensions d’une convolution et entraîner un petit CNN sur des chiffres intégrés.

## Schémas détaillés de la projection

[Présentation visuelle étudiant — 71 diapositives](../../slides/ML_Avance_J4_Visuel_Etudiant.pptx) · [PDF des schémas](../../usecase/MyLittleMLLab/lectures/AML_04_Schemas.pdf). Reprise guidée Kaggle K1 à K8, puis rappel arbre, forêt et boosting, et calcul du réseau, gradients, boucle et courbes. Les notes professeur restent dans le dépôt enseignant.

[Guide de la reprise Kaggle K1 à K8](../../usecase/MyLittleMLLab/J4_REPRISE_KAGGLE.md). Les anciens repères 1 à 63 restent imprimés après cette introduction.
