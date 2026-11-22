# PY_03 - Explorer et mesurer une association

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Quelle description est soutenue par les données ?

## Ce que nous réutilisons

Une table dont le grain, les types et les jointures sont contrôlés.

## Ce que vous devez savoir montrer

Choisir une visualisation et une mesure cohérentes avec le type des variables.

## Les mots du chapitre

**Moyenne** : La somme divisée par l’effectif ; sensible aux valeurs extrêmes.

**Médiane** : Une valeur centrale selon l’ordre des observations.

**Pearson** : Une mesure de relation linéaire entre variables quantitatives.

**Association** : Une dépendance observée qui n’identifie pas automatiquement une cause.

## Comprendre le raisonnement

L’analyse exploratoire décrit les données et fait émerger des questions. Elle ne prouve pas automatiquement une cause. Une moyenne résume le niveau ; une médiane résiste mieux à certaines valeurs extrêmes ; un écart-type décrit la dispersion autour de la moyenne. Le nombre d’observations accompagne toujours un résumé : une moyenne de trois lignes ne vaut pas une étude sur trois mille lignes.

Une loi normale est une distribution symétrique en cloche caractérisée par sa moyenne et son écart-type. Ce n’est pas la forme obligatoire des données. On regarde l’histogramme et le contexte avant de l’utiliser comme approximation. Une queue asymétrique ou des valeurs extrêmes peuvent demander d’autres résumés.

La mesure d’association dépend des variables. Pearson décrit une relation linéaire entre deux variables quantitatives. Spearman travaille sur les rangs et décrit une relation monotone. Pour deux variables catégorielles, un tableau de contingence puis, si pertinent, un V de Cramér décrivent une association sans lui donner de signe. Numéroter arbitrairement des genres de films ne les transforme pas en quantités. Les catégories multiples demandent d’expliciter l’encodage et l’unité d’analyse.

Un graphique doit avoir un titre informatif, des axes, des unités et une source. Une corrélation peut venir d’une variable commune, d’un effet temporel ou d’un biais de collecte. Elle ne suffit ni à décider d’une action ni à annoncer une causalité.

## Un calcul à savoir lire

Pearson décrit la relation linéaire après centrage et mise à l’échelle des deux variables. Un Pearson nul n’exclut pas une relation en U. Pour deux variables catégorielles, V de Cramér = racine[chi² / (n × min(r−1, c−1))], pour un tableau avec au moins deux lignes et deux colonnes et des marges valides. Cette mesure n’a pas de signe ; examiner effectifs et modalités avant de l’interpréter.

## PY_03-D1 - Exemple résolu

Les valeurs 10, 10 et 100 ont une moyenne de 40 et une médiane de 10. Les deux nombres sont corrects ; ils répondent à deux descriptions différentes du même petit échantillon.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
from statistics import mean, median
x = [10, 10, 100]
print(mean(x), median(x))
```

Sortie du calcul pédagogique :

```text
40 10
```

## PY_03-D2 - Démonstration accompagnée

Une corrélation nulle peut cacher une relation. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_03-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
x = np.array([-2.,-1.,0.,1.,2.])
y = x**2
r = float(np.corrcoef(x,y)[0,1])
print('x :', x.tolist())
print('y = x au carré :', y.tolist())
print('Pearson :', round(r,6))
assert abs(r) < 1e-12
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
x : [-2.0, -1.0, 0.0, 1.0, 2.0]
y = x au carré : [4.0, 1.0, 0.0, 1.0, 4.0]
Pearson : 0.0
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_03-E1 - Expliquer

On observe une association entre ancienneté et salaire. Peut-on conclure que chaque année supplémentaire provoque la même hausse de salaire ?

## PY_03-E2 - Transférer

Deux variables ont une corrélation de zéro. Peut-on affirmer qu’elles n’ont aucune relation ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_03-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Calculer Pearson sur des codes de catégories arbitraires, ou comparer des moyennes sans effectifs.

## La suite du parcours

Les associations servent à proposer des variables et des hypothèses ; la validation vérifiera leur utilité prédictive.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
