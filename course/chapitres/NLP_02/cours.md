# NLP_02 - Comprendre embeddings, attention et adaptation

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Qu’apprend-on en adaptant une représentation préentraînée ?

## Ce que nous réutilisons

La baseline texte et les gradients de ML avancé.

## Ce que vous devez savoir montrer

Identifier ce qui est gelé, entraîné et mis en cache.

## Les mots du chapitre

**Embedding** : Une représentation vectorielle dont le sens dépend de l’entraînement.

**Attention** : Une combinaison de valeurs pondérées par des compatibilités.

**Masque** : Une règle empêchant certaines positions de contribuer au calcul.

**Fine-tuning** : L’adaptation de paramètres d’un modèle préentraîné à une tâche.

## Comprendre le raisonnement

Un embedding représente une unité dans un espace vectoriel. Un encodeur contextuel produit une représentation qui dépend aussi des autres unités du texte. La proximité numérique peut être utile, mais son sens dépend de l’entraînement et de la tâche.

L’attention calcule des compatibilités entre requêtes et clés, puis combine des valeurs avec des poids normalisés. Dans l’attention par produit scalaire, les scores sont mis à l’échelle avant softmax. Le masquage empêche d’attribuer du poids à certaines positions, par exemple au padding. Une démonstration avec Q, K et V fixés explique le calcul ; dans le modèle, les projections correspondantes peuvent être apprises.

Geler l’encodeur conserve ses paramètres et permet d’entraîner une tête sur ses sorties. Le fine-tuning adapte certains ou tous ses paramètres ; il demande davantage de mémoire et peut suradapter un petit corpus. On note la révision du modèle, la tokenisation, la longueur maximale et le pooling utilisé.

Un cache d’embeddings est valide seulement si le texte et les transformations qui les produisent restent identiques. Un changement d’encodeur ou de pooling invalide les anciennes représentations. On compare TF-IDF, encodeur gelé et adaptation sur les mêmes partitions, avec des budgets déclarés ; un modèle plus grand n’a aucune obligation de gagner.

## Un calcul à savoir lire

L’attention par produit scalaire utilise softmax(QKᵀ/racine(dk))V. Le masque interdit certaines positions avant la normalisation. Dans D2, les scores retenus sont 0 et 2 ; la troisième position est masquée. Les poids sont environ 0,1192, 0,8808 et 0 : la grande valeur masquée ne contribue pas au contexte. Q représente les requêtes, K les clés et V les valeurs ; dk est la dimension des clés. Dans un transformer, des projections apprises produisent ces matrices. Dans le petit exemple, elles servent uniquement à expliquer le calcul.

## NLP_02-D1 - Exemple résolu

Des scores 0, 2 et 1 deviennent après softmax environ 0,090, 0,665 et 0,245. L’ordre est conservé et la somme vaut 1 ; ce n’est pas une garantie de calibration.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
from math import exp
scores=[0,2,1]; m=max(scores)
e=[exp(x-m) for x in scores]
p=[x/sum(e) for x in e]
print([round(x,3) for x in p])
print(round(sum(p),3))
```

Sortie du calcul pédagogique :

```text
[0.09, 0.665, 0.245]
1.0
```

## NLP_02-D2 - Démonstration accompagnée

Masquer une position dans l’attention. Cette démonstration est exécutée dans le notebook du chapitre, au repère **NLP_02-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
scores=np.array([0.,2.,1.])
mask=np.array([True,True,False])
masked=np.where(mask,scores,-np.inf)
weights=np.exp(masked-np.max(masked))
weights=weights/weights.sum()
values=np.array([[1.,0.],[0.,1.],[100.,100.]])
context=weights@values
print('Poids :',weights.round(4).tolist())
print('Contexte :',context.round(4).tolist())
assert weights[2]==0 and np.isclose(weights.sum(),1)
print('Scores et valeurs fixés pour le calcul ; aucun transformer entraîné ici.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Poids : [0.1192, 0.8808, 0.0]
Contexte : [0.1192, 0.8808]
Scores et valeurs fixés pour le calcul ; aucun transformer entraîné ici.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## NLP_02-E1 - Expliquer

On change le pooling moyen en pooling du premier token. Peut-on réutiliser sans contrôle le cache précédent ?

## NLP_02-E2 - Transférer

Les textes sont inchangés mais la révision de l’encodeur change. Faut-il considérer le cache comme encore valide ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## NLP_02-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Interpréter les poids d’attention comme une explication causale garantie ou confondre encodeur gelé et tête gelée.

## La suite du parcours

En vision, le transfert réutilise lui aussi des représentations préentraînées et adapte une tête ou une partie du réseau.

## Références techniques

- https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
