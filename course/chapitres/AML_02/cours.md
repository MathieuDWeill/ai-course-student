# AML_02 - Choisir une validation qui répond à la question

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

L’évaluation correspond-elle à la généralisation visée ?

## Ce que nous réutilisons

Une expérience décrite et une référence mesurée.

## Ce que vous devez savoir montrer

Justifier la frontière entre ensembles avant de commenter leurs scores.

## Les mots du chapitre

**Train** : Les observations utilisées pour apprendre.

**Validation** : Les observations utilisées pour choisir et diagnostiquer.

**Test indépendant** : Un ensemble préservé de la boucle de choix.

**Fold** : Une partition utilisée dans une validation croisée.

## Comprendre le raisonnement

Les données d’entraînement servent à apprendre ; la validation sert à choisir et diagnostiquer ; un test réellement indépendant sert à l’évaluation finale. Dès qu’un ensemble guide les choix successifs, il ne joue plus le rôle d’un test final intact. Un contrôle déjà consulté doit être présenté comme tel.

Le split dépend de la généralisation recherchée. Pour de nouvelles observations indépendantes, une séparation aléatoire peut convenir. Pour de nouveaux clients, les clients ne doivent pas traverser la frontière. Pour prédire le futur, la validation doit respecter le temps et la disponibilité réelle des labels. Stratifier maintient approximativement les proportions de classes ; cela n’élimine pas les fuites par groupe ou par temps.

La validation croisée répète des séparations à l’intérieur du développement. Chaque transformation apprise doit être ajustée sur le train du fold. Les scores par fold révèlent une partie de la sensibilité au découpage ; leur dispersion n’est pas automatiquement un intervalle de confiance, car les entraînements se recouvrent.

On compare les candidats sur les mêmes partitions, et on conserve le protocole avant d’observer le résultat. Changer le split jusqu’à obtenir un bon score transforme l’évaluation en optimisation cachée.

## Un calcul à savoir lire

Pour trois folds sur 180 observations réparties également, chaque modèle apprend sur 120 lignes et est évalué sur 60. Une prédiction hors fold est obtenue pour une ligne absente de l’apprentissage du modèle correspondant. Si les lignes dépendent d’une même source, il faut aussi contrôler les groupes.

## AML_02-D1 - Exemple résolu

Les sources A, B et C apparaissent en train ; A, C et D apparaissent en validation. A et C sont partagées. Pour viser de nouvelles sources, une séparation possible est train A/B/C, validation D.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
train={'A','B','C'}; valid={'A','C','D'}
print(sorted(train & valid))
print(sorted(train & {'D'}))
```

Sortie du calcul pédagogique :

```text
['A', 'C']
[]
```

## AML_02-D2 - Démonstration accompagnée

Garder les groupes de part et d’autre de la frontière. Cette démonstration est exécutée dans le notebook du chapitre, au repère **AML_02-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
from sklearn.model_selection import GroupShuffleSplit
X=np.arange(48).reshape(24,2)
y=np.tile([0,1],12)
groups=np.repeat(np.arange(6),4)
tr,va=next(GroupShuffleSplit(n_splits=1,test_size=.33,random_state=17).split(X,y,groups))
shared=set(groups[tr]) & set(groups[va])
print('Groupes partagés :',sorted(shared))
print('Lignes train/validation :',len(tr),len(va))
assert not shared
print('Vérifier aussi les classes et le sens de la généralisation.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Groupes partagés : []
Lignes train/validation : 16 8
Vérifier aussi les classes et le sens de la généralisation.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## AML_02-E1 - Expliquer

Un client possède dix lignes réparties au hasard entre train et validation. Quel risque cela pose-t-il si l’objectif est de prédire pour de nouveaux clients ?

## AML_02-E2 - Transférer

Un contrôle a servi à choisir trois fois le modèle. Peut-on encore le présenter comme un test final intact ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## AML_02-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Penser qu’un split stratifié résout toutes les dépendances ou apprendre le vocabulaire avant les folds.

## La suite du parcours

Le protocole fixé rend possibles les comparaisons de modèles de J3.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
