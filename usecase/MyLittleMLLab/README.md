# ML avancé — MyLittleMLLab

**J2 : [guide de démarrage](DEMARRER_J2.md) · [notebook AML_02](notebooks/AML_02_atelier.ipynb).**

**[Support J1 étudiant (PDF)](../../slides/ML_Avance_J1_Etudiant.pdf)**

**Notebook J1 à ouvrir : [notebooks/AML_01_atelier.ipynb](notebooks/AML_01_atelier.ipynb).**

**[Télécharger le kit complet J1 (ZIP)](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/kits/MyLittleMLLab_J1.zip)** · [Fiche de séance](fiches/AML_01.md) · [Cours rédigé](lectures/AML_01_cours.md)

Le ZIP contient le notebook, le code `mllab`, les dépendances et les documents de J1. **Ne téléchargez pas seulement le `.ipynb`** : il utilise les autres fichiers du kit. La prévisualisation GitHub permet de lire le notebook. Pour exécuter ses cellules, ouvrez la copie locale dans JupyterLab.

## 1. Récupérer le laboratoire

Téléchargez le ZIP ci-dessus. Faites **Extraire tout** sous Windows, ou décompressez-le sous macOS. Vous obtenez un dossier `MyLittleMLLab` contenant `README.md`, `requirements.txt`, `mllab/` et `notebooks/`. Placez ce dossier à un emplacement que vous retrouverez facilement.

Si vous utilisez déjà Git, une autre possibilité est de cloner le dépôt puis de travailler dans `usecase/MyLittleMLLab`. Pour un ancien clone, récupérez la nouvelle version avec votre méthode Git habituelle en conservant vos modifications locales.

## 2. Installer les dépendances de J1

Python **3.12 recommandé**. Ce laboratoire utilise un environnement séparé de celui du premier module. Ouvrez un terminal **dans le dossier MyLittleMLLab extrait**, celui où se trouve `requirements.txt`. Exécutez les commandes adaptées à votre système. Ne lancez pas les commandes depuis l’intérieur du ZIP.

### Windows — PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Si `py -3.12` est introuvable, installez Python 3.12 depuis [python.org](https://www.python.org/downloads/) puis rouvrez le terminal. Si vous disposez déjà d’un Python 3.11 ou 3.13, vous pouvez remplacer `py -3.12` par `py -3.11` ou `py -3.13`.

### macOS / Linux

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Si `python3.12` est introuvable, installez Python 3.12 depuis [python.org](https://www.python.org/downloads/). Si vous disposez déjà de Python 3.11 ou 3.13, utilisez l’interpréteur correspondant à la première ligne.

L’installation nécessite Internet. **J1 fonctionne sur CPU**, sans GPU, PyTorch, compte Copilot ni clé API. Il n’est pas nécessaire d’activer le venv : les commandes appellent directement son Python.

## 3. Récupérer les données de fraude

Ouvrez la **[page Data de la compétition](https://www.kaggle.com/competitions/playground-series-s6e11/data)**. Connectez-vous avec votre compte Kaggle, lisez les règles et effectuez vous-même les démarches demandées, puis téléchargez `playground-series-s6e11.zip`.

Les données de compétition ne sont pas redistribuées dans le kit. Le script suivant lit votre ZIP téléchargé et place uniquement les trois CSV attendus dans le laboratoire. Adaptez le chemin au nom de votre compte et à l’emplacement du ZIP.

Windows :

```powershell
.\.venv\Scripts\python.exe preparer_donnees.py "$HOME\Downloads\playground-series-s6e11.zip"
```

macOS :

```bash
.venv/bin/python preparer_donnees.py "$HOME/Downloads/playground-series-s6e11.zip"
```

Vous pouvez aussi extraire manuellement les trois fichiers pour obtenir exactement :

```text
MyLittleMLLab/
  data/competitions/playground-series-s6e11/
    train.csv
    test.csv
    sample_submission.csv
```

`train.csv` contient la cible `is_fraud`. `test.csv` ne la contient pas. Le script ne télécharge rien et ne demande aucun identifiant. Gardez vos fichiers Kaggle et vos éventuels tokens hors de Git.

## 4. Vérifier puis ouvrir JupyterLab

Windows :

```powershell
.\.venv\Scripts\python.exe verifier_j1.py
.\.venv\Scripts\python.exe -m jupyter lab notebooks/AML_01_atelier.ipynb
```

macOS / Linux :

```bash
.venv/bin/python verifier_j1.py
.venv/bin/python -m jupyter lab notebooks/AML_01_atelier.ipynb
```

La vérification doit annoncer **PRÊT POUR J1**. Gardez le terminal ouvert pendant l’utilisation de JupyterLab. Suivez les points d’arrêt du cours, sans tout lancer avant le signal de l’enseignant.

## 5. Ce que vous devez retrouver

- Cellule 5 : données trouvées et compétition sélectionnée.
- Cellule 7 : les six paiements, leur matrice de confusion et une AUC de 0,875.
- Cellule 10 : la cible, les dimensions et la fréquence des fraudes.
- Cellule 13 : la comparaison `dummy` / `linear` sur la même validation.
- Cellule 16 : le paquet exporté et le résultat importé localement.
- Cellule 19 : votre hypothèse et votre conclusion, avec une preuve et une limite.

Les numéros comptent toutes les cellules, textes compris. Les sorties vont dans `runs/`. Le notebook ne fait aucune soumission automatique à Kaggle. Le score local dépend du protocole et des versions utilisées.

## Si Kaggle est momentanément inaccessible

Vous pouvez lire le cours et faire les calculs des six paiements sur la fiche, sans données Kaggle. L’[annexe CPU](annexes_cpu/AML_01_atelier.ipynb) permet aussi de vérifier l’installation et la boucle d’export/import avec les chiffres manuscrits 8×8 déjà inclus. Ouvrez ce fichier dans JupyterLab uniquement sur indication du professeur. **Elle traite un autre problème** : ses classes, sa log-loss et ses scores ne se comparent pas à ceux de la fraude.

[Provenance des données](data/manifest.json) · [Distribution des données et poids](DATA_RIGHTS.md)
