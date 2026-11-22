# AML_01 - Décrire une expérience de bout en bout

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Que mesure exactement le résultat d’une expérience ?

## Ce que nous réutilisons

Les tables, la référence et le pipeline reproductible du premier module.

## Ce que vous devez savoir montrer

Conserver le protocole et relier chaque score à son sens.

## Les mots du chapitre

**Précision positive** : La proportion de vrais positifs parmi les alertes.

**Rappel positif** : La proportion de positifs effectivement repérés.

**AUC ROC** : Un classement relatif des scores entre positifs et négatifs.

**Traçabilité** : Les informations reliant une question, un protocole et des sorties.

## Comprendre le raisonnement

Une expérience est une question mise à l’épreuve par un protocole. Elle indique la cible, les données, la séparation, la métrique et le changement étudié. Le nom de l’algorithme ne suffit pas. Un identifiant d’expérience relie configuration, sorties et conclusion.

Dans une classification déséquilibrée, l’accuracy peut masquer l’échec sur les positifs. La matrice de confusion distingue vrais positifs, faux positifs, vrais négatifs et faux négatifs. Le rappel mesure la proportion de positifs repérés ; la précision mesure la proportion de vrais positifs parmi les alertes. Leur sens dépend de la classe considérée et du seuil.

L’AUC ROC évalue un classement des scores entre positifs et négatifs ; elle ne fixe pas le seuil d’action. Un prédicteur constant a une AUC de 0,5 si les deux classes sont présentes. Une AUC élevée ne garantit ni probabilités calibrées ni utilité économique.

Le cycle local vers Kaggle transporte une expérience, pas seulement un fichier de prédictions. Il faut retrouver le code, les identifiants et la configuration. Un aller-retour local réussi vérifie le contrat d’échange ; il ne démontre pas une exécution sur la plateforme distante.

## Un calcul à savoir lire

Précision = TP/(TP+FP) ; rappel = TP/(TP+FN) ; F1 = 2TP/(2TP+FP+FN). Dans D2 au seuil 0,3 : TP=2, FP=2 et FN=0, donc précision=0,5, rappel=1 et F1=2/3. L’AUC reste celle du classement des scores, pas celle de cette seule décision au seuil.

## AML_01-D1 - Exemple résolu

Un positif a un score 0,8 et deux négatifs ont 0,2 et 0,9. Il dépasse un négatif sur deux : l’AUC vaut 0,5 sur cet exemple sans égalité.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
positifs=[0.8]; negatifs=[0.2,0.9]
paires=[float(p>n)+0.5*float(p==n) for p in positifs for n in negatifs]
print(sum(paires)/len(paires))
```

Sortie du calcul pédagogique :

```text
0.5
```

## AML_01-D2 - Démonstration accompagnée

Une matrice de confusion et deux seuils. Cette démonstration est exécutée dans le notebook du chapitre, au repère **AML_01-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
from sklearn.metrics import confusion_matrix,precision_score,recall_score,roc_auc_score
y=[0,1,0,1,0,0]
scores=[.1,.8,.4,.6,.2,.3]
print('AUC sur ces six exemples :',round(roc_auc_score(y,scores),3))
for seuil in [.3,.7]:
    pred=[int(p>=seuil) for p in scores]
    print('Seuil :',seuil,'matrice :',confusion_matrix(y,pred).tolist())
    print('Précision :',round(precision_score(y,pred),3),
          'rappel :',round(recall_score(y,pred),3))
print('Le jouet explique les métriques ; il ne mesure pas la fraude réelle.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
AUC sur ces six exemples : 1.0
Seuil : 0.3 matrice : [[2, 2], [0, 2]]
Précision : 0.5 rappel : 1.0
Seuil : 0.7 matrice : [[4, 0], [1, 1]]
Précision : 1.0 rappel : 0.5
Le jouet explique les métriques ; il ne mesure pas la fraude réelle.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## AML_01-E1 - Expliquer

Un modèle a une AUC de 0,90. Peut-on annoncer qu’il reconnaît correctement 90 % des lignes ?

## AML_01-E2 - Transférer

Deux seuils appliqués aux mêmes scores peuvent-ils donner la même AUC mais des rappels différents ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## AML_01-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Confondre probabilité, classe prédite et métrique de classement.

## La suite du parcours

La séance suivante vérifie que cette expérience évalue bien la situation visée.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
