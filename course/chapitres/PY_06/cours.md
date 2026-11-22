# PY_06 - Rendre une analyse reproductible

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Peut-on refaire la même analyse dans un état propre ?

## Ce que nous réutilisons

Le nettoyage, les premiers modèles et l’évaluation séparée.

## Ce que vous devez savoir montrer

Redémarrer, exécuter dans l’ordre et retrouver les sorties annoncées.

## Les mots du chapitre

**Pipeline** : L’enchaînement explicite des étapes de transformation et de modèle.

**Fit** : L’ajustement de paramètres à partir d’exemples.

**Transform** : L’application d’une transformation déjà définie ou apprise.

**Artefact** : Un fichier nécessaire à comprendre, reproduire ou utiliser le résultat.

## Comprendre le raisonnement

Un pipeline définit les étapes entre les données brutes et la prédiction. Certaines étapes apprennent des informations, comme une médiane ou un vocabulaire. Elles sont ajustées sur le train, puis réutilisées telles quelles pour transformer la validation et les futures entrées. En validation croisée, cet apprentissage doit être recommencé à l’intérieur de chaque fold.

Reproduire demande davantage que conserver un notebook. On identifie les données, les dépendances, les paramètres, les partitions et le code. Une seed aide à stabiliser certains tirages ; elle ne garantit pas une identité universelle entre matériels et versions. Une empreinte permet de reconnaître un fichier précis mais ne décrit pas sa signification.

Un notebook exécuté dans un ordre différent peut utiliser des variables cachées en mémoire. Le contrôle élémentaire consiste à redémarrer le noyau et exécuter toutes les cellules dans l’ordre. Les chemins ne doivent pas dépendre d’un nom de compte personnel. Les données brutes sont conservées séparément des résultats ; les erreurs d’entrée doivent provoquer un message explicite.

La livraison contient le prétraitement et le modèle, ou une procédure complète pour les retrouver. On recharge l’ensemble et on compare les prédictions sur un petit lot connu. Une preuve de rechargement est plus utile qu’une capture du seul entraînement réussi.

## Un calcul à savoir lire

Une transformation apprise dépend des lignes utilisées pour son ajustement. Sur le train [0,2], la moyenne vaut (0+2)/2 = 1. Ajouter la validation [100] donne (0+2+100)/3 = 34. La deuxième transformation utilise une information indisponible lors de l’ajustement correct du fold.

## PY_06-D1 - Exemple résolu

Le train contient 0 et 2, la validation contient 100. La moyenne du train vaut 1. La moyenne calculée sur les trois lignes vaut 34 : elle incorpore une information de validation.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
train=[0,2]; valid=[100]
print(sum(train)/len(train))
print(sum(train+valid)/len(train+valid))
```

Sortie du calcul pédagogique :

```text
1.0
34.0
```

## PY_06-D2 - Démonstration accompagnée

Sauvegarder et recharger un pipeline complet. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_06-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import joblib
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
X=np.array([[0,1],[1,0],[2,1],[3,2],[4,1],[5,2]])
y=np.array([0,0,0,1,1,1])
model=make_pipeline(StandardScaler(),LogisticRegression()).fit(X,y)
before=model.predict_proba(X)
with TemporaryDirectory() as d:
    file=Path(d)/'pipeline.joblib'
    joblib.dump(model,file)
    restored=joblib.load(file)
    assert np.allclose(before,restored.predict_proba(X))
print('Prétraitement et modèle rechargés : prédictions identiques.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Prétraitement et modèle rechargés : prédictions identiques.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_06-E1 - Expliquer

Un notebook fonctionne seulement si l’on exécute sa dernière cellule deux fois. Quel premier contrôle effectuer ?

## PY_06-E2 - Transférer

Une imputation utilise la médiane calculée avant le split. Comment refaire le protocole ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_06-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Apprendre une transformation avant la séparation ou assimiler seed fixe et reproductibilité complète.

## La suite du parcours

MyLittleMLLab transforme ce pipeline en expérience traçable entre exécution locale et environnement distant.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
