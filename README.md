# Python pour la Data Science — ESEO Pro

Dépôt public du module **Python pour la Data Science** et du portfolio pédagogique IA associé.

Le fil directeur reste simple :

> Le code qui tourne n'est pas une preuve que le résultat est vrai.

Le cours apprend à poser une question, comprendre le grain des données, vérifier les jointures, produire une analyse, puis transformer le résultat en décision fiable.

## Démarrage étudiant

Option recommandée : cliquez sur **Use this template** ou **Fork** sur GitHub, puis clonez votre propre copie.

Important : ouvrez un **terminal** dans le dossier du projet. Ne double-cliquez pas sur les fichiers `setup`, `check` ou `run`.

### Mac / Linux / Git Bash

```bash
git clone https://github.com/VOTRE-USER/ai-course-student.git
cd ai-course-student
bash setup.sh
bash check.sh
bash run.sh
```

### Windows PowerShell

```powershell
git clone https://github.com/VOTRE-USER/ai-course-student.git
cd ai-course-student
.\setup.bat
.\check.bat
.\run.bat
```

Si vous ne forkerez pas tout de suite, vous pouvez cloner la version de départ :

```bash
git clone https://github.com/MathieuDWeill/ai-course-student.git
cd ai-course-student
```

Si un fichier `.sh` s'ouvre au lieu de s'exécuter sous Windows, utilisez les commandes `.bat` ci-dessus.

Si Git Bash refuse l'exécution directe :

```bash
bash setup.sh
bash check.sh
bash run.sh
```

Puis ouvrir :

```text
notebooks/01_python_data_science/B1_S01_logic_over_code.ipynb
```

## Lundi — S1 : Logic Over Code

La première séance utilise :

- `notebooks/01_python_data_science/B1_S01_logic_over_code.ipynb`
- `datasets/retail_case/`

Objectifs S1 :

- vérifier l'environnement Python ;
- manipuler NumPy sans tunnel de syntaxe ;
- comprendre le grain de quatre tables ;
- distinguer faits, dimensions, clés et cardinalités ;
- construire un fait de vente fiable ;
- détecter une jointure valide techniquement mais fausse analytiquement.

Résultats de référence :

- `fact rows = 8`
- `reference revenue = 634`
- `bad-join revenue = 1268`
- la mauvaise jointure double artificiellement le chiffre d'affaires ;
- `validate=` doit permettre de détecter l'hypothèse de cardinalité incorrecte.

## Check hors ligne

`./check.sh` ne dépend pas de Google Trends ni d'Internet pour le test standard.

Il vérifie :

- environnement Python ;
- NumPy, pandas, matplotlib, scikit-learn, JupyterLab ;
- dataset `retail_case` ;
- notebook S1 ;
- clés et grains minimaux.

Le test Google Trends reste optionnel :

```bash
CHECK_ONLINE=1 ./check.sh
```

## Structure

```text
course/                         supports et cartes pedagogiques
notebooks/01_python_data_science/ seances Python / Data Science
notebooks/02_big_data_engineering/ Big Data et pipeline
notebooks/03_data_product_bi_decision/ BI, decision, produit data
notebooks/04_final_product/      assemblage final
notebooks/05_modern_ai_deep_learning/ bridge Modern AI
notebooks/90_kaggle_public/      notebooks publics Kaggle
datasets/retail_case/            cas e-commerce reproductible S1/S2
datasets/euromillions_historical_data/ dataset hasard/probabilites
projects/                        framework projet
kaggle/                          strategie portfolio Kaggle
data/snapshots/                  snapshots Google Trends versionnes
docs/                            documentation de cours et exports NotebookLM
```

## Parcours pédagogique

Progression :

1. Data Science : explorer, nettoyer, visualiser, modeliser.
2. ML Engineering : entrainer, evaluer, industrialiser, deployer.
3. Applied AI : construire des applications NLP, vision et multimodales.
4. Modern AI bridge : comprendre pourquoi le deep learning a change l'IA moderne.

Voir :

- `SYLLABUS.md`
- `TEACHING_MAP.md`
- `TDSP_TEACHING_LAYER.md`
- `RUN_ALL_COURSE.md`
- `STUDENT_GIT_WORKFLOW.md`

## Règles de travail

- Comprendre ce qu'une ligne représente avant de calculer.
- Écrire les hypothèses importantes et les rendre testables.
- Vérifier les cardinalités avant/après une jointure.
- Contrôler un résultat important par une seconde méthode.
- L'IA peut aider à coder, mais ne remplace pas la vérification.
