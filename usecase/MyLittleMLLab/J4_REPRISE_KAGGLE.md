# Reprise J4 — De la sonde à la vraie expérience ML

Conception pédagogique : Mathieu Weill.

À réaliser avec le professeur avant la suite de J4. Conserver J3_2 pour la sonde ; utiliser ensuite KAGGLE_AML_03.ipynb pour le modèle.

## K1 — De la sonde au vrai modèle

1. Prouver que la sonde a terminé.

2. Importer ensemble le notebook ML dans Kaggle.

3. Récupérer et expliquer ses résultats.

## K2 — Vérifier la fin de la sonde

Dans J3_2 : consulter status, sans relancer push.

Quand le statut indique complete : récupérer output.

Ouvrir rapport.json : calcul doit valoir 4.

## K3 — Télécharger le bon notebook

Ouvrir le dépôt étudiant → usecase → MyLittleMLLab → templates.

Télécharger KAGGLE_AML_03.ipynb.

Garder ce nom et l’extension .ipynb.

[Ouvrir le fichier à télécharger](https://github.com/MathieuDWeill/ai-course-student/blob/main/usecase/MyLittleMLLab/templates/KAGGLE_AML_03.ipynb)

## K4 — Importer dans Kaggle

Se connecter à son compte Kaggle.

Créer un notebook → File → Import Notebook.

Choisir KAGGLE_AML_03.ipynb depuis l’ordinateur.

[Ouvrir Kaggle Code](https://www.kaggle.com/code)

## K5 — Ajouter les données et choisir CPU

Add Input : rechercher playground-series-s6e11.

Ajouter les données de la compétition : train.csv, test.csv, sample_submission.csv.

Vérifier accès privé et accélérateur None / CPU.

[Ouvrir la compétition](https://www.kaggle.com/competitions/playground-series-s6e11)

## K6 — Exécuter avec le protocole conservé

Lire les deux cellules d’amorçage, puis lancer les cellules dans l’ordre.

Conserver seed, folds, limite de lignes et paramètres.

Puis Save Version → Save & Run All pour enregistrer une exécution complète.

## K7 — Récupérer les résultats du vrai atelier

Dans la version terminée : ouvrir les sorties / Output.

Chercher MyLittleMLLab/runs/J3 : comparaison, journal, manifest et submission_J3.csv.

Télécharger les fichiers utiles ; ne rien soumettre au classement pour cette étape.

## K8 — Comparer avant de conclure

Même empreinte des identifiants ? Mêmes folds et limite de données ?

Même métrique et mêmes paramètres ? Quelles versions logicielles ?

Noter : voie graphique ou API, référence/version, résultat et limite.

## Commandes de vérification de la sonde

Après B10 et l’envoi effectué une seule fois dans B11, consulter l’état dans une cellule séparée :

```python
kaggle_cmd('kernels', 'status', REF, execute=True)
```

Attendre le statut `complete`. Puis récupérer et contrôler le rapport :

```python
SORTIES = RUN / 'retour_kaggle'
SORTIES.mkdir(exist_ok=True)
kaggle_cmd('kernels', 'output', REF, '-p', str(SORTIES), execute=True)
rapport = json.loads((SORTIES / 'rapport.json').read_text())
assert rapport['calcul'] == 4
print('Résultat distant vérifié :', rapport)
```

Ne pas relancer `push` pour suivre l’état. Une réussite de l’import graphique du notebook ML ne prouve pas que la boucle API a été complétée.

## À remettre

La référence et la version Kaggle, les sorties récupérées, une comparaison du protocole avec le local et une limite expliquée. Ne pas transmettre de jeton ni de données dont la redistribution n’est pas autorisée.
