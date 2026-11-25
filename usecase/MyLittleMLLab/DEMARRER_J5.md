# Démarrer J5 — Choisir une expérience et son budget

Conception pédagogique : Mathieu Weill.

## Installation accompagnée PC et Mac

Télécharger le kit de la séance depuis `kits`, puis l’extraire **dans un nouveau dossier**. Ne pas écraser le laboratoire qui contient vos runs J1 à J4. Le kit comprend `mllab`, `notebooks`, `templates` et les dépendances ; aucun `git pull` n’est nécessaire.

Dans un terminal ouvert dans le dossier `MyLittleMLLab` extrait :

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-j56.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

**macOS / Linux**

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements-j56.txt
./.venv/bin/python -m jupyter lab
```

Choisir le noyau Python de ce nouvel environnement. Les calculs utilisent le CPU, sans PyTorch ni GPU pour ces deux séances. Si vous gardez votre laboratoire existant, ajouter les deux nouveaux modules `mllab/experiments_j56.py`, `mllab/delivery_j56.py`, `api_j6.py`, les notebooks et les dépendances du kit ; la voie recommandée reste le dossier neuf.

## Les données restent les données officielles

Après obtention personnelle et autorisée des CSV de `playground-series-s6e11`, placer :

```text
data/competitions/playground-series-s6e11/train.csv
data/competitions/playground-series-s6e11/test.csv
data/competitions/playground-series-s6e11/sample_submission.csv
```

Vous pouvez recopier ces trois fichiers depuis votre laboratoire J3/J4. Ils ne sont pas redistribués dans le kit. Une erreur de fichiers absents doit être corrigée avant D1 ; ne pas substituer un dataset simulé. Le profil classe utilise au plus 15 000 lignes train et trois folds fixes.

## Comment suivre la projection

Chaque repère **D1 à D12** correspond à une section nommée du notebook. Il ne désigne pas le compteur `In[n]` qui augmente à chaque exécution. Lire l’objectif, prévoir une sortie, exécuter au signal, puis expliquer une valeur avant de continuer. Si le noyau redémarre, les variables disparaissent : reprendre les cellules dans l’ordre.

## Ouvrir et réaliser J5

Ouvrir `notebooks/AML_05_atelier.ipynb`. Les étapes sont : D1 données ; D2 budget ; D3 petit test ; D4 folds ; D5 tournoi ; D6 écarts ; D7 jouet de moyenne ; D8 combinaison réelle ; D9 mesures de temps ; D10 décision ; D11 transfert préparé ; D12 bilan.

D5 réalise 12 fits, plus les deux fits techniques de D3 : **14 fits au total**. Relancer D5 redémarre le tournoi ; lire les sorties déjà obtenues si vous voulez seulement les commenter. Ne pas changer `LIMIT` en cours de notebook. Pour un autre profil, redémarrer et noter le changement avant D1.

### À conserver pour J6

Le dossier complet `runs/J5`, notamment `decision.json`. Il contient aussi `comparaison.csv`, `scores_folds.csv`, `oof.csv`, `latence.csv` et le protocole. Ne pas publier les sorties brutes de lignes de compétition dans un dépôt public.

### Reproduire sur Kaggle

Importer `templates/KAGGLE_AML_05.ipynb` dans un nouveau notebook Kaggle privé. Ajouter les données officielles autorisées, choisir CPU, puis exécuter dans l’ordre. Les deux cellules d’amorçage précèdent les mêmes sections D1 à D12 ; se repérer par leur titre. Attendre un état terminé puis récupérer `MyLittleMLLab/runs/J5`. Comparer les empreintes, les versions et les conditions avant les scores. Aucun token n’est inclus et aucune soumission n’est automatique. Vérifier ouverture et règles au moment de l’usage ; après clôture, ne pas annoncer un classement encore accessible.
