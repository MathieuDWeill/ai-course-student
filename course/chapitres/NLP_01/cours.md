# NLP_01 - Représenter le texte avec une référence simple

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Comment transformer un texte sans changer sa cible ?

## Ce que nous réutilisons

pandas, la logistique, les splits et les pipelines.

## Ce que vous devez savoir montrer

Vérifier la cible, le split et les erreurs de sens avant de complexifier le modèle.

## Les mots du chapitre

**Tokenisation** : Le découpage du texte en unités.

**Vocabulaire** : La correspondance apprise entre unités et variables.

**TF-IDF** : Une représentation combinant fréquence locale et fréquence dans le corpus.

**Bigramme** : Une paire d’unités consécutives dans la tokenisation retenue.

## Comprendre le raisonnement

Un texte brut n’est pas un vecteur directement utilisable par un modèle linéaire. La tokenisation le découpe en unités. Un vocabulaire associe des unités à des colonnes. Une représentation par comptes ou TF-IDF transforme chaque document en vecteur ; le vocabulaire et les pondérations sont appris sur le train, puis appliqués à la validation.

TF-IDF combine une fréquence dans le document et une pondération liée à la fréquence dans le corpus. Les formules exactes dépendent de l’implémentation et de sa normalisation. Le but est de réduire le poids de termes présents partout, sans prétendre que chaque terme rare soit utile. Les unigrammes perdent l’ordre ; les bigrammes représentent certaines paires, sans résoudre automatiquement ironie, ambiguïté ou changement de domaine.

Dans Disaster Tweets, la cible concerne une catastrophe réelle, pas le sentiment exprimé. Les messages peuvent contenir un vocabulaire figuré. Les textes identiques normalisés doivent rester dans la même partition ; quasi-doublons et événements communs demandent aussi un audit.

Le F1 positif combine précision et rappel de la classe positive. Le seuil se choisit à l’intérieur du développement, jamais grâce aux labels cachés du test. Une amélioration du seuil peut changer le F1 sans changer le modèle ni son classement des scores.

## Un calcul à savoir lire

Avec le lissage de scikit-learn, IDF(t) = ln[(1+n)/(1+df(t))] + 1, où n est le nombre de documents train et df le nombre de documents contenant le terme. Dans D2, « fire » apparaît dans deux des quatre textes : son IDF avant normalisation du vecteur vaut ln(5/3)+1, environ 1,511.

## NLP_01-D1 - Exemple résolu

Les textes « pas de feu » et « feu » partagent le mot feu, mais la négation change l’interprétation. Le bigramme « de feu » garde une information locale supplémentaire, sans comprendre à lui seul toute la phrase.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
texte='pas de feu'
tokens=texte.split()
bigrammes=[' '.join(tokens[i:i+2]) for i in range(len(tokens)-1)]
print(tokens)
print(bigrammes)
```

Sortie du calcul pédagogique :

```text
['pas', 'de', 'feu']
['pas de', 'de feu']
```

## NLP_01-D2 - Démonstration accompagnée

Apprendre un vocabulaire sans lire la validation. Cette démonstration est exécutée dans le notebook du chapitre, au repère **NLP_01-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
train=['smoke near the forest','fire destroys a house',
       'this song is on fire','a calm evening at home']
valid=['an unknown volcano is erupting']
vectorizer=TfidfVectorizer(ngram_range=(1,2)).fit(train)
Xtr=vectorizer.transform(train)
Xv=vectorizer.transform(valid)
print('Formes train et validation :',Xtr.shape,Xv.shape)
print('volcano dans le vocabulaire :','volcano' in vectorizer.vocabulary_)
assert 'volcano' not in vectorizer.vocabulary_
print('Corpus fabriqué pour comprendre la représentation, sans score de compétition.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Formes train et validation : (4, 27) (1, 27)
volcano dans le vocabulaire : False
Corpus fabriqué pour comprendre la représentation, sans score de compétition.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## NLP_01-E1 - Expliquer

Un vocabulaire TF-IDF a été appris sur tous les textes avant le split. Pourquoi refaire le pipeline ?

## NLP_01-E2 - Transférer

Un message « cette chanson est une bombe » contient un mot de catastrophe. Cela suffit-il à lui donner la cible catastrophe réelle ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## NLP_01-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Appeler le cas Disaster Tweets une analyse de sentiment ou confondre rappel positif et F1 macro.

## La suite du parcours

La deuxième journée texte compare cette référence à des représentations préentraînées.

## Références techniques

- https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
