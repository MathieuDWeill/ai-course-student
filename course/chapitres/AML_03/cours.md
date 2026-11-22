# AML_03 - Comprendre arbres, forêts et boosting

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Comment comparer des familles sans changer la question ?

## Ce que nous réutilisons

Les folds, les transformations et la référence linéaire.

## Ce que vous devez savoir montrer

Examiner les différences par fold et le coût, pas seulement la meilleure moyenne.

## Les mots du chapitre

**Arbre** : Un ensemble de règles successives apprises sur les données.

**Forêt** : Une combinaison d’arbres construits avec de l’aléa.

**Boosting** : Une fonction améliorée par ajouts successifs guidés par une perte.

**Ablation** : Une comparaison qui retire ou modifie un élément pour examiner son effet.

## Comprendre le raisonnement

Un arbre construit des règles successives sur les variables pour séparer les observations. En classification, une feuille résume la proportion des classes qui y arrivent. Une mesure comme Gini quantifie le mélange ; la qualité d’un split combine les impuretés des enfants en tenant compte de leurs effectifs.

Un arbre profond peut mémoriser des particularités. Une forêt combine des arbres construits avec de l’aléa, notamment échantillonnage et sélection de variables ; la moyenne réduit certaines variations sans garantir la disparition des biais. Le boosting construit une fonction par étapes : chaque ajout corrige la fonction actuelle selon une perte. Il ne s’agit pas simplement de voter entre modèles indépendants.

Une transformation de variables peut modifier le résultat autant qu’un changement de famille. Une ablation compare avec et sans un élément en gardant le protocole. On annonce ce que l’on remplace, ce que l’on ajoute et le budget. Une petite amélioration moyenne doit être examinée par fold ; elle ne prouve pas un progrès universel.

La permutation mesure la dégradation de performance quand on brouille une variable pour un modèle donné sur un ensemble donné. Elle n’établit pas une cause et peut être délicate à interpréter avec des variables corrélées.

La régularisation limite certaines solutions pour réduire l’adaptation aux particularités du train. Dans la régression logistique scikit-learn, C est l’inverse de sa force : diminuer C renforce la pénalisation, toutes choses égales. C n’est ni un poids appris ni un learning rate ; sa convention ne s’applique pas à tous les modèles.

## Un calcul à savoir lire

Gini = 1 − somme des proportions de classes au carré. Deux classes à parts égales donnent 1 − 0,25 − 0,25 = 0,5. Une feuille pure donne zéro. Pour comparer un split, on pondère les impuretés des enfants par leurs effectifs ; leur moyenne non pondérée peut changer le choix.

## AML_03-D1 - Exemple résolu

Une feuille contenant deux classes en proportions 1/2 et 1/2 a un Gini de 1 - (1/2)^2 - (1/2)^2 = 0,5. Une feuille pure a un Gini de zéro.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
def gini(ps): return 1-sum(p*p for p in ps)
print(gini([0.5,0.5]),gini([1.0,0.0]))
print(round(sum([0.2,0.5,0.8])/3,2))
```

Sortie du calcul pédagogique :

```text
0.5 0.0
0.5
```

## AML_03-D2 - Démonstration accompagnée

Comparer trois familles sur les mêmes folds. Cette démonstration est exécutée dans le notebook du chapitre, au repère **AML_03-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,HistGradientBoostingClassifier
X,y=make_classification(n_samples=240,n_features=8,n_informative=4,random_state=17)
folds=list(StratifiedKFold(3,shuffle=True,random_state=17).split(X,y))
models={'arbre':DecisionTreeClassifier(max_depth=3,random_state=17),
        'foret':RandomForestClassifier(n_estimators=20,max_depth=4,random_state=17,n_jobs=1),
        'boosting':HistGradientBoostingClassifier(max_iter=20,max_leaf_nodes=7,random_state=17)}
for name,model in models.items():
    scores=cross_val_score(model,X,y,cv=folds,scoring='roc_auc',n_jobs=1)
    print(name,[round(float(v),3) for v in scores])
print('Budget : 3 modèles x 3 folds = 9 fits, hors autres calculs.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
arbre [0.789, 0.819, 0.862]
foret [0.918, 0.963, 0.886]
boosting [0.93, 0.937, 0.926]
Budget : 3 modèles x 3 folds = 9 fits, hors autres calculs.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## AML_03-E1 - Expliquer

Trois configurations sont évaluées sur trois folds. Combien de fits faut-il pour cette recherche, hors refit final ?

## AML_03-E2 - Transférer

Un candidat gagne sur un fold et perd sur deux. Que manque-t-il pour conclure ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## AML_03-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Comparer un modèle avec fuite à un candidat sain uniquement sur leurs scores, ou confondre importance et causalité.

## La suite du parcours

J4 ouvre la boîte de l’entraînement neuronal et le compare à ces références.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
