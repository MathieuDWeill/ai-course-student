# J2 — Une validation qui mérite notre confiance

**[Notebook J2 : AML_02_atelier.ipynb](notebooks/AML_02_atelier.ipynb)** · **[Kit complet J2 (ZIP)](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/kits/MyLittleMLLab_J2.zip)**

## Si J1 fonctionne déjà

Vous gardez le même environnement Python et les mêmes données de fraude. Aucun nouveau compte, GPU, paquet Python ou téléchargement Kaggle n’est nécessaire.

1. Récupérez [le notebook J2](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/usecase/MyLittleMLLab/notebooks/AML_02_atelier.ipynb) avec **Enregistrer le lien sous**, ou le bouton de téléchargement de la page GitHub.
2. Enregistrez-le dans `MyLittleMLLab/notebooks/`, à côté de `AML_01_atelier.ipynb`. Conservez l’extension `.ipynb`, pas `.txt` ou `.html`.
3. Dans votre dossier MyLittleMLLab, lancez JupyterLab avec le Python de l’environnement J1. Ouvrez **AML_02_atelier.ipynb**, puis choisissez ce même noyau Python.
4. Gardez à disposition la [fiche de séance](fiches/AML_02.md) et le [cours rédigé](lectures/AML_02_cours.md). Vous pouvez les lire sur GitHub.

Windows PowerShell, depuis MyLittleMLLab :

```powershell
.\.venv\Scripts\python.exe -m jupyter lab notebooks/AML_02_atelier.ipynb
```

macOS / Linux, depuis MyLittleMLLab :

```bash
.venv/bin/python -m jupyter lab notebooks/AML_02_atelier.ipynb
```

## Si vous partez du kit complet J2

Extrayez entièrement le ZIP. Il contient les fichiers de J1 et de J2, le code `mllab`, les fiches et les dépendances. Il ne contient pas les données Kaggle ni un environnement Python déjà installé. Suivez le [guide d’installation](README.md). Si vous avez déjà les trois CSV, copiez-les dans `data/competitions/playground-series-s6e11/` de ce laboratoire plutôt que de les télécharger de nouveau.

**Ne remplacez pas votre travail de J1** : conservez votre ancien dossier et vos résultats `runs/`.

## Déroulé accompagné

Les numéros comptent toutes les cellules du fichier, textes compris. Ils ne désignent pas les compteurs `In [n]`. Le professeur annonce la cellule avant chaque démonstration. Certaines cellules de fin sont utilisées plus tôt dans le cours : c’est indiqué dans le PowerPoint.

| Cellule | Travail | Dépend de |
|---|---|---|
| 5 | Préparer les fichiers et les outils | Installation J1 et données |
| 7 | Repérer des groupes partagés | 5 |
| 24 | Vérifier GroupKFold sur le mini-tableau | 7 |
| 26 | Vérifier quand une cible est connue | 5 |
| 10 | Auditer le vrai train local et créer le dossier de preuves | 5 |
| 22 | Montrer la fuite dans une moyenne | 5 |
| 13 | Calculer les scores des folds et les prédictions OOF | 10 |
| 16 | Comparer des seuils avec les mêmes scores OOF | 13 |
| 28 | Comparer deux valeurs de C sur les mêmes folds | 13 et 10 |
| 30 | Montrer pourquoi copier la réponse invalide le score | 13 |
| 19 | Enregistrer et expliquer les preuves du socle | 13 et 16 |

La validation croisée porte sur le train local `tr`. La validation locale `va` reste en dehors de ces entraînements et prédictions OOF. Le test officiel Kaggle ne sert pas à calculer nos métriques locales. Après le choix du modèle, la cellule 40 produit ses prédictions pour préparer une soumission.

## Votre dossier de preuves

La cellule 10 crée un dossier unique `runs/j2_…`. La cellule 19 y conserve :

- `oof_predictions.csv` : une ligne par observation du train local, son fold exclu, sa cible et son score OOF ;
- `fold_scores.csv` : tailles et ROC-AUC par fold ;
- `thresholds.csv` : alertes, erreurs, précision et rappel selon le seuil ;
- `manifest.json` : protocole, versions et empreintes des fichiers.

La cellule 28 ajoute `regularisation_cv.csv`. Si le manifeste existe déjà, son empreinte y est ajoutée. Votre conclusion écrite cite vos valeurs, le protocole et une limite. Un nom de fichier n’est pas une preuve de validité : expliquez ce qu’il contient et comment il a été produit.

## Si un calcul ou une installation bloque

Ne modifiez pas dix lignes au hasard. Montrez le message au professeur. Les captures du cours permettent de poursuivre le raisonnement. Les tailles et scores peuvent différer entre profils ou versions : comparez vos propres méthodes avec le même protocole. Un résultat OOF est une évaluation de développement, pas une garantie sur de nouvelles périodes ou de nouvelles personnes.

## Atelier de compétition Kaggle

Récupérez la version enrichie du notebook : elle contient **42 cellules**, textes compris. L’environnement de J1 suffit. Après le socle et la cellule 19, nous avançons ensemble :

| Cellule | Travail | Dépend de |
|---|---|---|
| 32 | Comparer dummy, logistique C=0,1 et boosting sur les mêmes folds | 10, 13 |
| 34 | Choisir et enregistrer la configuration sur la CV | 32 |
| 36 | Contrôler le choix sur la validation locale va | 34 |
| 38 | Examiner les erreurs au seuil 0,5 | 36 |
| 40 | Réapprendre et fabriquer submission.csv avec contrôles | 36 |
| 42 | Tenir le journal et renseigner le score public réel après dépôt | 40 |

La cellule 32 effectue neuf apprentissages. La cellule 40 réapprend sur un échantillon stratifié du train officiel limité à LIMIT, puis prédit toutes les lignes du test officiel. Ce réapprentissage peut inclure des lignes de l’ancienne validation locale : elle ne mesure donc plus indépendamment le modèle réappris.

Les fichiers restent sur votre ordinateur. Le dépôt sur [Kaggle](https://www.kaggle.com/competitions/playground-series-s6e11) est manuel, après lecture des règles, des modalités d’équipe et de la page Evaluation. Cette compétition utilise des scores continus de fraude. Le journal conserve `None` tant qu’aucun score public réel n’a été reçu.

Le dossier `runs/j2_…` conserve aussi comparaison_modeles.csv, selection.json, controle_validation.json, audit_validation.csv et journal_kaggle.csv. Le CSV de soumission et release.json se trouvent dans le dossier `runs/submission_fraud_…` affiché par la cellule 40.
