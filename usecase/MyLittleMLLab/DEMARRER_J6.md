# Démarrer J6 — Livrer un système vérifiable

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

## Reprendre J5 avant J6

Dans le nouveau laboratoire, recopier `runs/J5` issu de votre J5 validé. Les CSV officiels doivent être identiques. Si `decision.json` manque, terminer J5 ; ne pas créer manuellement un gagnant. Ouvrir `notebooks/AML_06_atelier.ipynb` et exécuter D1 à D12 dans l’ordre.

J6 réentraîne uniquement le candidat retenu (un modèle, ou deux pour la moyenne), sauvegarde le pipeline complet et teste le rechargement dans un nouveau processus. Le bundle `runs/J6/release` dépend des versions enregistrées ; s’il vient d’un autre environnement incompatible, reconstruire avec la décision et les données autorisées. Ne charger que des artefacts créés ou approuvés dans un contexte de confiance.

## L’API locale : d’abord D8, ensuite le navigateur

D8 teste les routes avec TestClient, sans ouvrir de port. Les réponses attendues sont 200 pour `/health`, 200 pour un batch valide et 422 pour un batch invalide.

Pour afficher la même application dans le navigateur, ouvrir un **second terminal** à la racine du laboratoire après D3/D4 :

Windows :

```powershell
.\.venv\Scripts\python.exe -m uvicorn api_j6:app --host 127.0.0.1 --port 8006
```

macOS/Linux :

```bash
./.venv/bin/python -m uvicorn api_j6:app --host 127.0.0.1 --port 8006
```

Ouvrir **http://127.0.0.1:8006/docs**. Tester `GET /health`. Pour `POST /predictions`, choisir « Try it out », copier le contenu **complet** de `runs/J6/release/exemple_entree.json` dans le corps de requête, puis exécuter. Le résultat contient trois scores et l’empreinte du modèle. Retirer une clé dans une copie pour constater le refus 422. Arrêter avec Ctrl+C dans le terminal du serveur. Si le port est occupé, choisir 8007 et adapter l’URL ; le test D8 reste disponible.

L’API écoute uniquement sur la machine locale ; elle n’est pas une plateforme de production authentifiée. TestClient ne mesure pas une latence réseau.

## Reproduire sans API

D6 affiche la commande exacte pour recharger le bundle avec le Python du notebook. Le module `mllab.delivery_j56` prend `--bundle`, `--input` et `--output`. Le nouveau processus doit retrouver les scores dans la tolérance indiquée. Pour un autre poste, installer les dépendances, extraire le paquet et conserver l’arborescence avec `mllab` et `release`.

## À remettre et à expliquer

Conserver `runs/J6/livraison_J6.zip`, `submission_J6.csv`, la politique de surveillance et le bilan. Le paquet contient le pipeline, le manifeste, l’exemple, les versions, le code utile et la fiche modèle. Aucun dataset brut ni identifiant secret n’y figure. Le CSV reste local ; ne pas confondre création, contrôle, soumission et performance en entreprise.
