# Notebooks

Structure aligned with the syllabus and course progression.

```text
01_python_data_science/       Bloc 1 - Python for Data Science
02_big_data_engineering/      Bloc 2 - Big Data & Data Engineering
03_data_product_bi_decision/  Bloc 3 - Data Product, BI & Decision
04_final_product/             Final assembled decision product
05_modern_ai_deep_learning/   Optional Modern AI / Deep Learning bridge
90_kaggle_public/             Public Kaggle notebooks
99_templates/                 Reusable notebook templates
data/                         Local notebook snapshots kept for compatibility
```

Naming convention:

- `B1_S02_...ipynb`: Bloc 1, session 2.
- `B2_S04_...ipynb`: Bloc 2, session 4.
- `B3_S07_...ipynb`: Bloc 3, session 7.
- `FP_01_...ipynb`: final product notebook.
- `DL_S01_...ipynb`: optional deep learning / modern AI bridge.
- `KG_01_...ipynb`: Kaggle publication notebook.
- `TPL_...ipynb`: reusable template, not part of the main run order.

Use `../RUN_ALL_COURSE.md` for the executable order and produced artifacts.

## Complément séance 4

Après `01_python_data_science/B1_S04_supervised_ml_baseline.ipynb`, utiliser
`01_python_data_science/B1_S04b_supervised_ml_diagnostic.ipynb` pour diagnostiquer
un score parfait, reformuler la cible et comparer les modèles dans le temps.
Ce complément écrit dans `outputs/bloc1/s04_diagnostic/`.

Pour une démonstration simple de modèles qui apprennent, ouvrir
`01_python_data_science/B1_S04c_supervised_ml_iris_demo.ipynb` : classification
de fleurs Iris avec arbre, voisins et régression logistique, comparés à une
référence naïve. Autonome, sans téléchargement. Pour une séance accessible,
commencer par Iris ; utiliser S04b pour le diagnostic de l'exemple temporel.

Alternative liée au travail :
`01_python_data_science/B1_S04d_supervised_ml_retards_demo.ipynb`.
QUID : anticiper le retard d'une tâche au démarrage. Données explicitement
simulées, comparaison arbre / régression logistique / forêt et référence naïve.
