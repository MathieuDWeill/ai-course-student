# PY_02 - Fiabiliser les données avec pandas

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

La table nettoyée décrit-elle encore les mêmes événements ?

## Ce que nous réutilisons

Le grain, les tableaux et les unités de PY_01.

## Ce que vous devez savoir montrer

Contrôler unicité, lignes sans correspondance et agrégats avant/après.

## Les mots du chapitre

**Clé** : Une ou plusieurs colonnes identifiant une entité au grain annoncé.

**Cardinalité** : Le nombre de correspondances attendues entre deux tables.

**Valeur manquante** : Une absence de valeur dont la signification doit être examinée.

**Contrat** : Des règles explicites que les données doivent respecter.

## Comprendre le raisonnement

Un DataFrame pandas est une table dont les colonnes ont des noms et des types. Charger un CSV ne garantit ni la bonne lecture des dates, ni la validité des nombres, ni l’unicité d’une clé. On examine les types, les valeurs manquantes, les doublons et quelques lignes avant les agrégations.

Une clé identifie une entité dans le contexte annoncé. Une table de transactions contient des événements ; une table de produits décrit les produits. Une jointure relie leurs lignes. Si la table produits contient deux descriptions pour la même clé, une transaction peut être dupliquée pendant la jointure. Le programme réussit, mais la somme augmente artificiellement. La validation de cardinalité, par exemple many_to_one, transforme cette hypothèse en contrôle.

Une valeur manquante peut correspondre à une absence réelle, une donnée non collectée ou une erreur de lecture. La remplacer par zéro modifie son sens. On documente une règle justifiée, puis on vérifie les effectifs et agrégats avant et après transformation. En apprentissage, une médiane d’imputation est apprise sur le train seulement ; c’est une étape du pipeline, pas une préparation libre sur tout le fichier.

## Un calcul à savoir lire

Une ligne de gauche liée à k lignes de droite apparaît k fois après une jointure interne sur cette clé. Pour k=2, le montant 20 est répété deux fois et la somme devient 40. Le contrôle many_to_one exige au plus une correspondance à droite pour chaque clé.

## PY_02-D1 - Exemple résolu

Une vente de montant 20 est reliée à deux lignes produits portant la même clé. La jointure produit deux lignes et un total de 40. Ce doublement révèle une cardinalité non respectée, pas une hausse réelle des ventes.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
ventes = [{'produit': 'A', 'montant': 20}]
produits = [{'produit': 'A'}, {'produit': 'A'}]
jointure = [v for v in ventes for p in produits if v['produit'] == p['produit']]
print(len(jointure), sum(v['montant'] for v in jointure))
```

Sortie du calcul pédagogique :

```text
2 40
```

## PY_02-D2 - Démonstration accompagnée

Faire refuser une jointure invalide. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_02-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import pandas as pd
ventes = pd.DataFrame({'produit':['A','B'],'montant':[20,25]})
produits = pd.DataFrame({'produit':['A','A','B'],'famille':['X','Y','Z']})
try:
    ventes.merge(produits, on='produit', validate='many_to_one')
except pd.errors.MergeError:
    print('Cardinalité invalide détectée : examiner la table produits.')
else:
    raise AssertionError('La jointure invalide devait être refusée')
assert ventes.montant.sum() == 45
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Cardinalité invalide détectée : examiner la table produits.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_02-E1 - Expliquer

Une jointure fait passer le nombre de lignes de 100 à 130. Quelles vérifications demander avant de calculer une moyenne ?

## PY_02-E2 - Transférer

Une clé produit apparaît deux fois à droite d’une jointure many_to_one. Faut-il accepter le résultat parce qu’aucune valeur ne manque ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_02-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Supprimer tous les doublons sans définir la clé ou considérer toute absence comme zéro.

## La suite du parcours

La qualité des données conditionne l’exploration et évite qu’un modèle apprenne sur une table déjà fausse.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
