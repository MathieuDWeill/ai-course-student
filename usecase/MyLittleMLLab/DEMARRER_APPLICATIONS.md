# Préparer les applications ML, NLP et vision

Conception pédagogique : Mathieu Weill.

Le [socle guidé](../../course/CATALOGUE.md) fonctionne sans données externes. Cette page concerne les ateliers `AML_05`, `AML_06`, `NLP_01`, `NLP_02`, `CV_01` et `CV_02` sur données de compétition. Garder le dossier `mllab` au même niveau que `notebooks` et ouvrir le terminal dans `usecase/MyLittleMLLab`.

## Environnement

Réutiliser l’environnement préparé selon le README du laboratoire. NLP_01 et ML_05/06 utilisent les dépendances de base. NLP_02 et les ateliers vision nécessitent les dépendances profondes. Installer celles-ci avant la séance, avec une connexion Internet ; cela peut être plus long que l’installation du socle.

Windows PowerShell :

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-deep.txt
```

macOS/Linux :

```bash
.venv/bin/python -m pip install -r requirements-deep.txt
```

Redémarrer le noyau du notebook après installation. La compatibilité de PyTorch et torchvision dépend du matériel et du Python utilisés ; en cas d’absence de paquet compatible, demander l’environnement alternatif prévu en séance.

## Données officielles

Télécharger personnellement les fichiers depuis les pages Data, après les démarches demandées par la plateforme. Ne pas substituer silencieusement un jeu fabriqué aux données officielles.

- Fraude : `data/competitions/playground-series-s6e11/train.csv`, `test.csv` et `sample_submission.csv`.
- Disaster Tweets : `data/competitions/nlp-getting-started/train.csv`, `test.csv` et `sample_submission.csv`.
- Chiens/chats : `data/competitions/dogs-vs-cats-redux-kernels-edition/train/`, `test/` et `sample_submission.csv`. Extraire aussi les archives imbriquées ; les dossiers doivent contenir les images JPEG.

Les pages des trois compétitions sont référencées dans `mllab/competition.py`. Les règles, conditions d’accès et ressources se vérifient avant participation. L’atelier n’accepte rien et ne soumet rien à votre place.

## Préparer les poids

NLP_02 utilise un encodeur préentraîné ; la vision utilise ResNet18. Le téléchargement ci-dessous est une action explicite à réaliser sur la machine qui exécutera le notebook, après lecture des licences concernées. Un cache sur un ordinateur n’est pas disponible automatiquement sur un autre.

Windows :

```powershell
.\.venv\Scripts\python.exe -m mllab.prepare_assets --text
.\.venv\Scripts\python.exe -m mllab.prepare_assets --vision
```

macOS/Linux :

```bash
.venv/bin/python -m mllab.prepare_assets --text
.venv/bin/python -m mllab.prepare_assets --vision
```

Le script écrit un manifeste dans `runs/asset_preparation`. Ne pas redistribuer les caches, les données ou les identifiants. Lancer seulement la préparation utile à la séance.

## Premier contrôle

Ouvrir le notebook indiqué et exécuter les cellules de préparation avant un entraînement. Vérifier le nom de la compétition, les données trouvées, les formes, le profil de calcul et la métrique. Si une ressource manque, arrêter et corriger le chemin ou le cache ; ne pas laisser un calcul partir avec une autre question.

Les profils courts servent à vérifier le fonctionnement. Un résultat sur peu d’images ou de textes n’est pas un benchmark fiable de compétition. Aucun score public n’est annoncé avant une soumission réellement effectuée.
