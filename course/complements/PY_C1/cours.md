# PY_C1 — Clustering hiérarchique et responsabilité

Conception pédagogique : Mathieu Weill.

## Question et progression

Comment des groupes se construisent-ils, et que peut-on décider avec eux ?

À placer après PY_05. Durée indicative : 45 minutes, à adapter aux acquis.

Preuve attendue : Lire une fusion de groupes et identifier une conséquence possible de leur utilisation.

## La distance précède le groupe

Une distance exprime ce que nous décidons de considérer comme proche. Les unités et les variables choisies influencent donc le résultat.

Nous connaissons k-means. Nous allons regarder une autre manière de regrouper : réunir progressivement les observations ou groupes les plus proches. Avant de choisir un algorithme, nous choisissons une représentation. Dix kilomètres et dix euros ne sont pas des quantités comparables. Standardiser peut rendre les échelles comparables ; cela ne rend pas automatiquement toutes les variables pertinentes.

Question de vérification : Changer l’unité d’une variable peut-il changer les groupes ?

## La classification ascendante hiérarchique

Chaque observation commence seule. À chaque étape, deux groupes fusionnent selon un critère de liaison. La liaison simple utilise la paire la plus proche.

Ascendante signifie que nous partons des éléments pour construire des ensembles. Hiérarchique signifie que les fusions s’emboîtent. La liaison simple peut produire une chaîne : une suite de proches voisins réunit des extrêmes pourtant éloignés. D’autres critères existent. Ward recherche une faible augmentation de l’inertie et s’emploie avec une distance euclidienne. Nous n’allons pas les confondre.

Question de vérification : Une fusion est-elle une preuve que deux personnes se ressemblent en tout ?

## Le dendrogramme et sa coupure

Le dendrogramme représente les fusions. La hauteur indique le critère de fusion, dont le sens dépend de la méthode. Couper l’arbre fixe une partition.

Un dendrogramme n’est pas un arbre de décision supervisé. Nous n’apprenons pas à prédire une cible. La coupure ne révèle pas un nombre universel de vraies catégories. Nous regardons la stabilité et l’utilité des groupes pour la question. Dans notre petit exemple, 0 et 1 se regroupent, puis 7 et 9 fusionnent avant que les deux ensembles se rejoignent.

Question de vérification : Deux groupes obtenus suffisent-ils à justifier deux actions commerciales ?

## Une analyse responsable

Définir l’usage, minimiser les données, rechercher les erreurs par sous-groupe et prévoir un recours humain. Une association ne prouve pas une cause.

Un groupe calculé peut devenir une étiquette imposée. Imaginons un outil d’aide à l’emploi : une distance entre CV ne mesure ni le mérite ni la capacité d’apprendre. Nous devons demander quelles données sont nécessaires, quelles erreurs pénalisent une personne, et comment elle peut contester une décision. Une variable apparemment neutre peut aussi servir d’indice indirect pour une caractéristique sensible. La bonne réponse est une enquête sur l’usage et les erreurs, pas la promesse que supprimer une colonne résout tout.

Question de vérification : Un score global élevé garantit-il des erreurs réparties équitablement ?

## PY_C1-D1 — Lire les distances

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
import numpy as np
x=np.array([0.,1.,7.,9.])
d=np.abs(x[:,None]-x[None,:])
print(d.astype(int))
assert d[0,1]==1 and d[2,3]==2
```

## PY_C1-D2 — Construire la hiérarchie

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
from scipy.cluster.hierarchy import linkage,cut_tree
Z=linkage(x[:,None],method='single',metric='euclidean')
groups=cut_tree(Z,n_clusters=2).ravel()
print('Fusions :',Z.tolist())
print('Groupes :',groups.tolist())
assert groups[0]==groups[1] and groups[2]==groups[3]
assert groups[0]!=groups[2]
```

## Sorties résolues et limites

Les deux premières fusions sont séparées : 0 avec 1, puis 7 avec 9. Les étiquettes 0 et 1 nomment des groupes ; leur valeur n’a pas de sens ordinal. Nous commentons les distances de liaison simple, pas une performance prédictive.

## PY_C1-E — Exercice individuel

Une entreprise veut refuser automatiquement une candidature à partir de son cluster. Proposer deux vérifications et une limite à cette utilisation.

Écrire une réponse justifiée avant la correction collective.

## Bilan

Lire une fusion de groupes et identifier une conséquence possible de leur utilisation.

Une sortie expliquée : …

Une limite : …

Une prochaine vérification : …

## Références

- https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
- https://scikit-learn.org/stable/modules/clustering.html
