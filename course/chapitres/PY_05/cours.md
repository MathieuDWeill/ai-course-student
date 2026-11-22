# PY_05 - Explorer sans cible et distinguer la recommandation

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Quel effet la représentation a-t-elle sur les groupes ?

## Ce que nous réutilisons

Les variables, les distances et la différence entre décrire et prédire.

## Ce que vous devez savoir montrer

Comparer des représentations et discuter l’interprétation sans inventer de vérité terrain.

## Les mots du chapitre

**Clustering** : Construire des groupes selon une représentation et une proximité.

**Distance** : Un choix de mesure de dissemblance.

**PCA** : Une projection linéaire résumant une partie de la variance.

**Recommandation** : Classer des éléments pour un utilisateur selon un objectif défini.

## Comprendre le raisonnement

L’apprentissage non supervisé cherche une structure sans cible fournie pour chaque observation. Le clustering regroupe des observations selon une représentation et un critère de proximité. Les groupes ne sont pas des vérités naturelles : ils dépendent des variables, de leur échelle, de la distance et du nombre de groupes demandé.

La PCA construit de nouveaux axes qui résument une partie de la variance. C’est une transformation linéaire, pas une découverte automatique des bonnes classes. Si une variable est mesurée en milliers et une autre entre zéro et un, l’échelle peut dominer le résultat. On choisit et documente les transformations ; on ne les applique pas mécaniquement.

Un système de recommandation classe des éléments pour un utilisateur à partir de son profil, de ses interactions ou des caractéristiques des éléments. Il peut utiliser des similarités, du filtrage collaboratif, une factorisation ou un modèle supervisé de classement. Le clustering peut contribuer au système, mais recommander n’est pas synonyme de clusteriser.

L’évaluation doit correspondre à l’usage. Pour recommander un prochain élément, on peut réserver des interactions futures et vérifier la qualité du classement. Faire apparaître en entraînement l’interaction que l’on prétend prédire donne une impression trompeuse de réussite.

## Un calcul à savoir lire

Similarité cosinus = produit scalaire / (norme du premier vecteur × norme du second), pour deux vecteurs non nuls. Avec [1,0] et [1,1], le produit scalaire vaut 1 et les normes valent 1 et racine(2). La similarité vaut donc 1/racine(2), environ 0,707.

## PY_05-D1 - Exemple résolu

Deux vecteurs [1,0] et [1,1] ont une similarité cosinus de 1/racine(2), environ 0,707. Le calcul mesure leur direction commune ; il ne dit pas à lui seul qu’un utilisateur aimera un contenu.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
from math import sqrt
a=[1,0]; b=[1,1]
sim=sum(x*y for x,y in zip(a,b))/(sqrt(sum(x*x for x in a))*sqrt(sum(y*y for y in b)))
print(round(sim,3))
```

Sortie du calcul pédagogique :

```text
0.707
```

## PY_05-D2 - Démonstration accompagnée

Projeter une représentation avant de l’interpréter. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_05-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
X,_ = make_blobs(n_samples=90,centers=3,n_features=4,random_state=17)
Z = StandardScaler().fit_transform(X)
pca = PCA(n_components=2).fit(Z)
coords = pca.transform(Z)
labels = KMeans(n_clusters=3,n_init=10,random_state=17).fit_predict(Z)
print('Forme projetée :', coords.shape)
print('Groupes demandés et obtenus :', len(set(labels)))
print('Part de variance des deux axes :', round(pca.explained_variance_ratio_.sum(),3))
assert coords.shape == (90,2)
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Forme projetée : (90, 2)
Groupes demandés et obtenus : 3
Part de variance des deux axes : 0.969
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_05-E1 - Expliquer

Pourquoi deux clusters de clients peuvent-ils changer si l’on remplace le revenu en euros par le revenu en milliers d’euros sans standardiser ?

## PY_05-E2 - Transférer

Un algorithme produit trois groupes. A-t-il prouvé qu’il existe exactement trois profils réels ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_05-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Appeler les clusters des labels vrais ou choisir clustering seulement parce que le projet recommande des contenus.

## La suite du parcours

Les représentations apprises en NLP et vision prolongeront cette question de proximité et de géométrie.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
