# PY_04 - Construire une référence supervisée

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Le modèle apporte-t-il quelque chose à une référence simple ?

## Ce que nous réutilisons

Une question précise, une exploration et des variables disponibles au bon moment.

## Ce que vous devez savoir montrer

Écrire cible, unités, variables disponibles et métrique avant le modèle.

## Les mots du chapitre

**Cible** : La réponse à apprendre à partir des exemples.

**Régression** : Prédire une quantité numérique.

**Classification** : Prédire une classe ou un score associé à une classe.

**Référence** : Une méthode simple mesurée avec le même protocole.

## Comprendre le raisonnement

L’apprentissage supervisé utilise des exemples dont la réponse, appelée cible, est connue pendant l’entraînement. En régression, on prédit une quantité, comme une durée. En classification, on prédit une classe ou un score associé, comme le risque de retard. Les variables d’entrée doivent exister au moment où la décision sera prise : une date réelle de fin ne peut pas aider à détecter un retard au démarrage.

Une référence simple permet de savoir si le modèle apporte quelque chose. Pour une régression, prédire toujours la moyenne ou la médiane du train constitue une référence possible ; leur pertinence dépend de la métrique. Pour une classification, prédire la classe majoritaire peut obtenir une accuracy élevée tout en ignorant une classe rare. On choisit la référence avant de célébrer le score.

L’erreur est l’écart entre prédiction et observation. La MAE moyenne les écarts absolus. La RMSE est la racine de la moyenne des carrés des écarts : elle donne davantage de poids aux grandes erreurs. Ces deux métriques gardent l’unité de la cible. Une MAE de 2 pour une cible en points de pourcentage signifie deux points de pourcentage d’écart absolu en moyenne. Elle n’annonce pas que chaque prédiction sera à deux points.

Un bon résultat sur un monde simulé démontre un apprentissage dans ce monde. Il ne valide pas encore une utilisation dans une autre population ou une entreprise réelle.

## Un calcul à savoir lire

MAE = moyenne de |prédiction − observation|. RMSE = racine de la moyenne de (prédiction − observation)². Pour les erreurs 2, 0 et −2 : MAE = 4/3 ≈ 1,333 et RMSE = racine(8/3) ≈ 1,633. Les deux gardent l’unité de la cible.

## PY_04-D1 - Exemple résolu

Les valeurs observées sont 10, 12 et 14 ; les prédictions sont 12, 12 et 12. Les écarts absolus sont 2, 0 et 2. La MAE vaut 4/3 ; la RMSE vaut la racine de 8/3, soit environ 1,633.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
from math import sqrt
y = [10,12,14]; pred = [12,12,12]
mae = sum(abs(a-b) for a,b in zip(y,pred))/len(y)
rmse = sqrt(sum((a-b)**2 for a,b in zip(y,pred))/len(y))
print(round(mae,3), round(rmse,3))
```

Sortie du calcul pédagogique :

```text
1.333 1.633
```

## PY_04-D2 - Démonstration accompagnée

Comparer une référence et un modèle sur Iris. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_04-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
X,y = load_iris(return_X_y=True)
Xtr,Xv,ytr,yv = train_test_split(X,y,test_size=.25,stratify=y,random_state=17)
models = {'reference':DummyClassifier(strategy='most_frequent'),
          'logistique':make_pipeline(StandardScaler(),LogisticRegression(max_iter=500))}
for nom,model in models.items():
    model.fit(Xtr,ytr)
    print(nom, 'accuracy :', round(accuracy_score(yv,model.predict(Xv)),3))
print('Une seule séparation pédagogique : pas une garantie universelle.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
reference accuracy : 0.316
logistique accuracy : 0.921
Une seule séparation pédagogique : pas une garantie universelle.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_04-E1 - Expliquer

Une classification compte 95 négatifs et 5 positifs. Un modèle annonce toujours négatif. Donner son accuracy et son rappel de la classe positive.

## PY_04-E2 - Transférer

Pour prédire une durée au démarrage, on utilise la date réelle de fin. Quel problème cela pose-t-il ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_04-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Comparer seulement au hasard, ignorer la référence majoritaire ou confondre points de pourcentage et variation relative.

## La suite du parcours

Le ML avancé demandera si un gain résiste à un protocole crédible et à un budget annoncé.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
