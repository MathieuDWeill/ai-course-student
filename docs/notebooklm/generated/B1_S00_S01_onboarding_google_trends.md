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
