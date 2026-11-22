# AML_03 - Comprendre arbres, forêts et boosting

Conception pédagogique : Mathieu Weill.

**Comment comparer des familles sans changer la question ?**

## À ouvrir pendant le cours J3

**La présentation détaillée du professeur suit [AML_03_atelier.ipynb](../../usecase/MyLittleMLLab/notebooks/AML_03_atelier.ipynb), qui contient 32 cellules.** Les numéros annoncés en classe comptent aussi les cellules de texte.

1. Suivre les [consignes de préparation J3](../../usecase/MyLittleMLLab/DEMARRER_J3.md).
2. Placer le notebook dans `MyLittleMLLab/notebooks`, avec les données et l’environnement déjà utilisés en J1/J2.
3. Exécuter dans l’ordre, au signal du professeur. Après un redémarrage du noyau, reprendre les cellules précédentes.

Le petit notebook du socle ci-dessous sert à réviser les notions avec des exemples courts. Ses repères D1/D2 ne correspondent pas aux numéros de cellules de l’atelier.

## Le trio du chapitre

- [Guide de séance](../chapitres/AML_03/README.md)
- [PDF étudiant rédigé](../chapitres/AML_03/cours.pdf)
- [PowerPoint étudiant](../chapitres/AML_03/presentation.pptx)
- [Notebook guidé](../chapitres/AML_03/notebook.ipynb)

Les démonstrations D1 et D2, les exercices E1/E2 et le bilan B partagent les mêmes repères. Le PowerPoint contient 24 diapositives. La version étudiante ne contient ni notes de présentation professeur ni réponses réservées aux exercices.

## Application complémentaire

[Ouvrir l’atelier d’application](../../usecase/MyLittleMLLab/notebooks/AML_03_atelier.ipynb). Ce carnet est distinct du socle guidé. Les anciens repères numériques des ateliers et des projections détaillées sont conservés.

[Préparer les données et l’environnement de l’application](../../usecase/MyLittleMLLab/DEMARRER_J3.md).

## Réussite attendue

Examiner les différences par fold et le coût, pas seulement la meilleure moyenne.

## Avant de quitter la séance

Sans relire la correction, savoir :

- Expliquer avec une règle concrète ce que fait un arbre, puis distinguer forêt et boosting.
- Comparer les modèles avec les mêmes folds et la même métrique ; lire aussi les différences entre folds.
- Justifier la représentation retenue et le budget de recherche, puis montrer les fichiers produits dans `runs/J3`.
- Dire pourquoi le contrôle déjà consulté en J2 ne constitue plus un test indépendant.

Si un point bloque, noter la cellule concernée et demander une reprise avec le professeur. Un notebook exécuté ne suffit pas à prouver que ces étapes sont comprises.

## Vérification et limites

Le notebook du chapitre a été exécuté localement dans un noyau neuf. Les résultats des petits exemples ne constituent pas des scores Kaggle. L’atelier local AML_03 a également été exécuté entièrement dans un noyau neuf, sur CPU, avec les données officielles locales et une limite de 15 000 observations. Cette vérification ne couvre pas tous les PC/Mac ni une exécution authentifiée sur Kaggle. [Détail des vérifications](../VERIFICATION.md).

[Catalogue](../CATALOGUE.md) · [Aide](../AIDE.md)

## Rappel avant la séance

[Six diapositives de rappel accompagné](../../slides/ML_Avance_J3_Rappel_Etudiant.pptx) : répondre brièvement avant la correction orale. Ce support étudiant ne contient pas de notes professeur.

Pour les repères numériques de la présentation détaillée de classe, ouvrir **AML_03_atelier.ipynb** dans la rubrique Application complémentaire ci-dessus.
