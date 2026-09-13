# Bloc 1 - Python Data Science

# B1_S00 — Can You Beat Randomness?

Source notebook: `notebooks/01_python_data_science/B1_S00_Can_You_Beat_Randomness.ipynb`

## Decision Problem

Not explicitly stated.

## Key Concepts

- data quality
- exploratory analysis
- model validation
- business decision

## Course Notes

# B1_S00 — Can You Beat Randomness?

## Opening hook

**Can you beat randomness?**

EuroMillions looks simple: 5 main numbers, 2 Lucky Stars, one draw, one dream.

But before learning pandas, visualization, or machine learning, students need a more important lesson:

> Humans are pattern-making machines. Randomness is where that instinct becomes dangerous.

Questions for the room:

- Do some numbers come out more often?
- Are there hot numbers?
- Are there cursed numbers?
- Can we detect a real pattern?
- Or are we just seeing shapes in noise?

This notebook is **not** about predicting lottery numbers. It is about learning why Data Science often starts by proving that a pattern is fake.

## Decision problem

When we see historical data, how do we know whether a visible pattern is meaningful or just randomness doing what randomness does?

Dataset: **EuroMillions Historical Data** by Duarte Pereira da Cruz on Kaggle. It contains historical EuroMillions draws from 2004 to present, including draw dates, five main numbers, two Lucky Stars, and jackpot/rollover context when available.

## Load the Kaggle dataset

On Kaggle, add the dataset **EuroMillions Historical Data** to the notebook input. Locally, place the CSV anywhere under `data/`, `datasets/`, `kaggle/`, or the repo root.

The notebook intentionally fails with a clear message if the dataset is missing. We do not generate fake lottery history.

## Prepare draw columns

Kaggle datasets can evolve. Instead of hard-coding one schema too aggressively, we detect likely main-number and Lucky Star columns from names and values.

# 1. Frequency analysis

The first temptation is simple: count which numbers came out most often.

This is where intuition starts whispering: “that number wins more.”

The statistical question is sharper:

> Is the difference surprising, or is it normal variation?

## Does one number really “win more”?

A number can be above average without being special.

In random systems, someone is always first. Someone is always last. That does not mean the leader has a hidden force.

# 2. Hot numbers vs cold numbers

Hot/cold lists are seductive because they turn noise into a story.

But a story is not evidence.

## Gambler’s fallacy

The gambler’s fallacy says: “This number has not appeared for a while, so it is due.”

But in a fair draw, the machine does not remember.

An overdue number is not a promise. It is a feeling.

# 3. Human bias

Even if randomness is fair, humans can still play badly.

Why?

- **Birthdays effect:** many people choose 1–31, ignoring 32–50.
- **Favorite numbers:** people cluster around memorable numbers.
- **Pattern preference:** sequences, diagonals, symmetry, and “nice looking” tickets feel meaningful.
- **Narrative bias:** we invent explanations after seeing results.

This does not change the draw probability. It changes how many people may share a prize if common numbers win.

Reflection question:

Even if every combination has the same probability, why might a human-selected ticket be strategically worse than a random ticket?

# 4. Monte Carlo simulation

Now we compare intuition with pure randomness.

If the real draw is fair, simulated random draws should also produce “hot” numbers, “cold” numbers, and overdue numbers.

That is the point: randomness naturally creates patterns that look suspicious.

# 5. Statistical interpretation

Key ideas:

**Law of large numbers**  
As the number of draws grows, frequencies tend to move closer to expected proportions. But “closer” does not mean “perfectly equal.”

**Variance**  
Random systems fluctuate. Variation is not automatically signal.

**Randomness illusion**  
Humans expect randomness to look balanced. Real randomness often looks streaky, clustered, and unfair.

**False signal detection**  
A core Data Science skill is not finding patterns. It is testing whether the pattern deserves belief.

# Final lesson

Data Science is often not about finding patterns.

It is about proving that some patterns are fake.

Students should leave remembering:

> **Randomness is not intuitive. Data Science starts when intuition fails.**

## Practical Activities

### Code activity 1

create charts

### Code activity 2

load course data

### Code activity 3

run a practical notebook step

### Code activity 4

save reusable artifacts

### Code activity 5

create charts

### Code activity 6

save reusable artifacts

### Code activity 7

save reusable artifacts

### Code activity 8

save reusable artifacts

### Code activity 9

save reusable artifacts

### Code activity 10

create charts

### Code activity 11

save reusable artifacts

## Expected Outputs

- No saved output artifact detected.

## Reflection Questions

- # B1_S00 — Can You Beat Randomness?
- Do some numbers come out more often?
- Are there hot numbers?
- Are there cursed numbers?
- Can we detect a real pattern?


---

# Bloc 1 — Python pour la Data Science (B2)

Source notebook: `notebooks/01_python_data_science/B1_S00_S01_onboarding_google_trends.ipynb`

## Decision Problem

how can a public signal become evidence for a product or business decision without overclaiming?

## Key Concepts

- data quality
- model validation
- business decision

## Course Notes

# Bloc 1 — Python pour la Data Science (B2)
## Séance 0 + Séance 1 — Installation + premières illusions sur des données Google Trends

**Decision problem:** how can a public signal become evidence for a product or business decision without overclaiming?

Ce notebook contient **deux parties** :
- **Séance 0 (onboarding)** : installation + vérifications + “ça tourne”
- **Séance 1 (3h30)** : introduction Data Science + NumPy + premières explorations **sur Google Trends récupéré automatiquement**

> ⚠️ Google Trends n’a pas d’API officielle. On utilise **pytrends** (non-officiel).  
> Si Google limite temporairement les requêtes (429 / captcha), réessayez plus tard ou changez de réseau.

# Séance 0 — Installation & prise en main (objectif : zéro friction en séance 1)

## Objectif
À la fin de cette séance, vous devez pouvoir :
- exécuter un notebook
- installer/charger les bibliothèques
- afficher un graphique
- récupérer des données Google Trends via `pytrends`

## Où exécuter ce notebook ?
### Option A (recommandée) — Anaconda / Jupyter
1. Installer Anaconda
2. Lancer **JupyterLab** (ou Jupyter Notebook)
3. Ouvrir ce notebook
4. Exécuter les cellules **dans l’ordre** (Shift+Enter)

### Option B — VS Code
1. Installer Python 3.10+
2. Installer VS Code + extensions Python & Jupyter
3. Ouvrir ce notebook
4. Exécuter les cellules **dans l’ordre**

### Option C — Google Colab (si votre machine pose problème)
1. Ouvrir Colab
2. Importer ce notebook
3. Exécuter les cellules (l’installation sera refaite à chaque session)

## 0.1 — Vérifier Python

## 0.2 — Installer les bibliothèques (si nécessaire)

- Si vous êtes sur **Anaconda**, vous avez souvent déjà `numpy/pandas/matplotlib/seaborn/sklearn`.
- Sinon, exécutez la cellule ci-dessous.
- On installe aussi **pytrends** pour récupérer Google Trends.

## 0.3 — Tester les imports

## 0.4 — Test rapide : calcul + graphique

## 0.5 — Test Google Trends (connexion + première requête)

On récupère une série d’intérêt dans le temps pour un mot-clé.
- `geo="FR"` : France
- `timeframe="today 12-m"` : 12 derniers mois

“Les warnings des bibliothèques externes peuvent être ignorés si le résultat est correct.”

✅ Si vous voyez une courbe, vous êtes prêt pour la Séance 1.

---

# Séance 1 — Introduction à la Data Science avec Python (3h30)
**Syllabus :**
- Panorama Data Science et applications
- Environnement Python DS (déjà fait en séance 0)
- Manipulation de données avec **NumPy**

## 1.1 — Qu’est-ce qu’un “problème Data Science” ? (version courte)
On part d’une question, puis on vérifie ce que **les données permettent** (ou non) de conclure.

Fil rouge du semestre :
> **Détecter des signaux faibles** à partir de données Google Trends.

## 1.2 — NumPy : mesurer variation, vitesse, accélération (sur un mini-signal)
Ce sont des briques simples, mais très puissantes pour les séries temporelles.

## 1.3 — Récupérer des données Google Trends (automatique)

On récupère **plusieurs mots-clés** et on observe les premières illusions :
- un score est **relatif** (0–100) sur une fenêtre
- comparer deux courbes “brutes” est souvent trompeur

## 1.4 — Première illusion : le score (0–100) n’est pas absolu

On vient de tracer **le même mot-clé** sur deux fenêtres temporelles différentes (12 mois vs 5 ans).

Questions (à discuter) :
- Que vaut un **100** sur Google Trends ?
- Est-ce qu’un **70** aujourd’hui est comparable à un **70** il y a 3 ans ?
- Que change le choix de la **fenêtre temporelle** sur l’interprétation ?

👉 Conclusion : le score est **relatif** à la fenêtre et au maximum observé.

## 1.5 — Un premier indicateur simple : lissage (moyenne glissante)
Même un lissage **change** ce qu’on croit voir.

## 1.6 — Mini-exercice (pendant la séance)

1) Choisissez 3 mots-clés (au choix : sport, musique, tech, finance…).  
2) Récupérez 5 ans de données en France.  
3) Tracez le brut et le lissé.  
4) Notez **3 problèmes** qui empêchent une conclusion solide (comparabilité, fenêtre, bruit, etc.).

> C’est volontaire : en séance 2, on rendra ces données **comparables**.

## 1.7 — Conclusion (séance 1)
- Nous avons manipulé des données numériques avec NumPy
- Nous avons récupéré des données réelles (Google Trends) automatiquement
- Nous avons constaté que les données brutes sont **trompeuses** et **non directement comparables**

➡️ Séance 2 : Pandas + nettoyage + alignement + rendre comparables plusieurs requêtes.

## Practical Activities

### Code activity 1

run a practical notebook step

### Code activity 2

create charts

### Code activity 3

create charts; train or evaluate a model

### Code activity 4

create charts

### Code activity 5

run a practical notebook step

### Code activity 6

create charts

### Code activity 7

run a practical notebook step

### Code activity 8

run a practical notebook step

### Code activity 9

run a practical notebook step

### Code activity 10

create charts

### Code activity 11

run a practical notebook step

### Code activity 12

run a practical notebook step

### Code activity 13

load course data; save reusable artifacts

### Code activity 14

load course data; save reusable artifacts

### Code activity 15

load course data; save reusable artifacts

### Code activity 16

run a practical notebook step

### Code activity 17

load course data; create charts

### Code activity 18

create charts

## Expected Outputs

- No saved output artifact detected.

## Reflection Questions

- **Decision problem:** how can a public signal become evidence for a product or business decision without overclaiming?
- ## Où exécuter ce notebook ?
- Que vaut un **100** sur Google Trends ?
- Est-ce qu’un **70** aujourd’hui est comparable à un **70** il y a 3 ans ?
- Que change le choix de la **fenêtre temporelle** sur l’interprétation ?


---

# Séance 2 — Pandas : manipulation & nettoyage

Source notebook: `notebooks/01_python_data_science/B1_S02_pandas_cleaning_alignment.ipynb`

## Decision Problem

how do bad dates, missing values, duplicates, and inconsistent categories create bad decisions?

## Key Concepts

- data quality
- model validation
- reproducibility
- business decision

## Course Notes

# Séance 2 — Pandas : manipulation & nettoyage

**Decision problem:** how do bad dates, missing values, duplicates, and inconsistent categories create bad decisions?

Official topic preserved: pandas manipulation and cleaning. The output is a clean analytical table used by the rest of the course.

## Practical exercise

Add one new validation rule that would prevent a bad management dashboard.

## Conclusion

The pipeline now has a trusted input table for analysis, modeling, and BI.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data

### Code activity 3

save reusable artifacts; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc1/data_quality_report.csv`

## Reflection Questions

- **Decision problem:** how do bad dates, missing values, duplicates, and inconsistent categories create bad decisions?


---

# Séance 3 — Analyse exploratoire & visualisation

Source notebook: `notebooks/01_python_data_science/B1_S03_eda_visualization_storytelling.ipynb`

## Decision Problem

what pattern is strong enough to change what we do next?

## Key Concepts

- data quality
- exploratory analysis
- model validation
- data engineering
- business decision

## Course Notes

# Séance 3 — Analyse exploratoire & visualisation

**Decision problem:** what pattern is strong enough to change what we do next?

Official topic preserved: EDA and visualization. The output is a reusable analysis summary and chart.

## Practical exercise

Write one decision that the chart supports and one decision it does not support.

## Conclusion

EDA converts clean data into evidence, but only if it ends with interpretation and limits.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data; aggregate and summarize evidence

### Code activity 3

save reusable artifacts; create charts; aggregate and summarize evidence; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/eda_decision_note.md`
- `outputs/bloc1/eda_signal_summary.csv`
- `outputs/bloc1/eda_weak_signals.png`

## Reflection Questions

- **Decision problem:** what pattern is strong enough to change what we do next?


---

# Séance 4 — ML supervisé (régression & classification)

Source notebook: `notebooks/01_python_data_science/B1_S04_supervised_ml_baseline.ipynb`

## Decision Problem

when does prediction improve a decision, and when does it only create false confidence?

## Key Concepts

- data quality
- model validation
- reproducibility
- business decision

## Course Notes

# Séance 4 — ML supervisé (régression & classification)

**Decision problem:** when does prediction improve a decision, and when does it only create false confidence?

Official topic preserved: supervised learning. The output is a feature table and model metrics.

## Practical exercise

Identify which error type would be most costly for a product team.

## Conclusion

A model is only useful if it improves a decision against a baseline and exposes its limits.

## Practical Activities

### Code activity 1

load course data; create charts; train or evaluate a model

### Code activity 2

load course data; save reusable artifacts

### Code activity 3

save reusable artifacts; train or evaluate a model

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`
- `outputs/bloc1/feature_table.csv`
- `outputs/bloc1/model_metrics.csv`

## Reflection Questions

- **Decision problem:** when does prediction improve a decision, and when does it only create false confidence?


---

# Séance 5 — ML non supervisé (clustering, PCA)

Source notebook: `notebooks/01_python_data_science/B1_S05_unsupervised_patterns.ipynb`

## Decision Problem

how do we detect useful patterns when labels do not exist?

## Key Concepts

- data quality
- model validation
- business decision

## Course Notes

# Séance 5 — ML non supervisé (clustering, PCA)

**Decision problem:** how do we detect useful patterns when labels do not exist?

Official topic preserved: clustering and PCA. The output is a segment table for interpretation.

## Practical exercise

Rename each regime with a business interpretation.

## Conclusion

Unsupervised learning creates hypotheses for action; it does not prove segments are real.

## Practical Activities

### Code activity 1

load course data; create charts; train or evaluate a model

### Code activity 2

load course data; save reusable artifacts; aggregate and summarize evidence; train or evaluate a model

## Expected Outputs

- `outputs/bloc1/attention_regime_profiles.csv`
- `outputs/bloc1/attention_regimes.csv`
- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/clean_trends_wide.csv`

## Reflection Questions

- **Decision problem:** how do we detect useful patterns when labels do not exist?


---

# Séance 6 — Pipeline Data Science

Source notebook: `notebooks/01_python_data_science/B1_S06_reproducible_data_science_pipeline.ipynb`

## Decision Problem

can this analysis be rerun reliably when the decision comes back next month?

## Key Concepts

- data quality
- exploratory analysis
- model validation
- reproducibility
- business decision

## Course Notes

# Séance 6 — Pipeline Data Science

**Decision problem:** can this analysis be rerun reliably when the decision comes back next month?

Official topic preserved: data science pipeline. The output is a validation report and artifact manifest.

## Practical exercise

Add one artifact that would make the pipeline easier to audit.

## Conclusion

A repeatable pipeline turns classroom analysis into an operational decision process.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

save reusable artifacts; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/artifact_manifest.json`
- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/pipeline_validation_report.csv`

## Reflection Questions

- **Decision problem:** can this analysis be rerun reliably when the decision comes back next month?


---

# Séances 7–8 — Projet tutoré

Source notebook: `notebooks/01_python_data_science/B1_S07_S08_guided_project_restitution.ipynb`

## Decision Problem

what recommendation can we defend with evidence, limits, and a reproducible workflow?

## Key Concepts

- data quality
- exploratory analysis
- model validation
- reproducibility
- data engineering
- business decision

## Course Notes

# Séances 7–8 — Projet tutoré

**Decision problem:** what recommendation can we defend with evidence, limits, and a reproducible workflow?

Official topic preserved: guided project and restitution. The output is a Bloc 1 project brief.

## Practical exercise

Turn this brief into a 3-minute stakeholder presentation.

## Conclusion

The Bloc 1 project is now an evidence package feeding the rest of the data product.

## Practical Activities

### Code activity 1

load course data; create charts

### Code activity 2

load course data; save reusable artifacts; validate pipeline quality

## Expected Outputs

- `outputs/bloc1/clean_trends_long.csv`
- `outputs/bloc1/eda_signal_summary.csv`
- `outputs/bloc1/model_metrics.csv`
- `outputs/bloc1/project_brief.md`

## Reflection Questions

- **Decision problem:** what recommendation can we defend with evidence, limits, and a reproducible workflow?


---
