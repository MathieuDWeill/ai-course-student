# PY_01 - Comprendre la question et les tableaux

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Une table numérique peut-elle répondre à la question posée ?

## Ce que nous réutilisons

Aucun modèle n’est nécessaire pour commencer : il faut savoir lire une consigne et identifier une observation.

## Ce que vous devez savoir montrer

Lire les formes avant et après une opération ; justifier l’axe choisi.

## Les mots du chapitre

**Grain** : Ce que représente une ligne dans son contexte.

**Variable** : Une information décrivant une observation.

**Type** : La nature informatique de la valeur, par exemple nombre ou texte.

**Axe** : Une dimension selon laquelle un tableau est parcouru.

## Comprendre le raisonnement

Une question utile précise ce que l’on veut savoir et à quel moment. « Analyser les ventes » est trop large. « Quel est le chiffre d’affaires des lignes de vente de cette période ? » annonce une quantité mesurable. Avant de programmer, on définit le grain : une ligne correspond-elle à une commande, à un article ou à une ligne de commande ? Additionner les mauvaises lignes donne un nombre exact pour une mauvaise question.

Python manipule des objets. Une liste contient des éléments ; une variable désigne un objet ; une fonction regroupe une opération que l’on peut réutiliser. NumPy représente efficacement des tableaux numériques. La forme, ou shape, donne la taille selon chaque axe : trois observations décrites par deux variables forment un tableau de forme (3, 2). Un calcul peut agir sur tout le tableau, sur chaque ligne ou sur chaque colonne. On annonce l’axe et l’unité avant de commenter le résultat.

Les grandes familles de bases de données répondent à des besoins distincts. Une base relationnelle organise des tables liées par des clés. Une base documentaire stocke des documents structurés, par exemple JSON. Une base clé-valeur retrouve une valeur à partir d’une clé. Une base graphe représente des entités et leurs relations. Aucun de ces formats ne dispense de définir ce que représente un enregistrement.

## Un calcul à savoir lire

Le chiffre d’affaires est une somme de produits : montant = quantité × prix unitaire. Ici : 2×10 + 1×25 + 3×4 = 57. Pour le tableau de forme (3, 2), axis=0 parcourt les trois observations et donne deux moyennes de colonnes ; axis=1 donne une moyenne par ligne.

## PY_01-D1 - Exemple résolu

Trois lignes de vente : quantités 2, 1 et 3 ; prix unitaires 10, 25 et 4. Les montants sont 20, 25 et 12. Le chiffre d’affaires vaut 57, dans l’unité monétaire du prix.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
quantites = [2, 1, 3]
prix = [10, 25, 4]
montants = [q*p for q,p in zip(quantites, prix)]
print(montants)
print(sum(montants))
```

Sortie du calcul pédagogique :

```text
[20, 25, 12]
57
```

## PY_01-D2 - Démonstration accompagnée

Lire les axes d’un tableau. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_01-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
x = np.array([[2,10],[1,25],[3,4]])
print('Forme :', x.shape)
print('Moyennes par colonne :', x.mean(axis=0).round(2).tolist())
print('Montants :', (x[:,0]*x[:,1]).tolist())
assert x.shape == (3,2)
assert int((x[:,0]*x[:,1]).sum()) == 57
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Forme : (3, 2)
Moyennes par colonne : [2.0, 13.0]
Montants : [20, 25, 12]
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_01-E1 - Expliquer

Un fichier contient cinq lignes mais seulement deux identifiants de commande distincts. Peut-on affirmer qu’il contient cinq commandes ? Justifier.

## PY_01-E2 - Transférer

Le tableau contient trois observations et deux mesures. Quelle est sa forme ? Quelle opération donnerait une moyenne par mesure ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_01-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Confondre nombre de lignes et nombre d’entités ; additionner des prix unitaires pour obtenir un chiffre d’affaires.

## La suite du parcours

Le grain servira ensuite à choisir les jointures, les splits et le sens d’une prédiction.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
