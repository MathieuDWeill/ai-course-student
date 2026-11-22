# AML_06 - Livrer et surveiller un système

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Qu’est-ce qu’un modèle réellement livrable ?

## Ce que nous réutilisons

Le pipeline, les artefacts, les budgets et la décision d’expérience.

## Ce que vous devez savoir montrer

Contrôler les entrées, les artefacts et l’alignement des sorties.

## Les mots du chapitre

**Contrat d’entrée** : Les champs, types, unités et refus prévus pour l’inférence.

**Rechargement** : L’utilisation des artefacts sauvegardés dans un état propre.

**Dérive d’entrée** : Un changement des données observées en utilisation.

**Supervision** : Les mesures et actions prévues pour contrôler le système.

## Comprendre le raisonnement

Un contrat d’inférence définit les champs d’entrée, leur type, leurs unités, les valeurs admises et le sens de la sortie. Il décrit aussi les refus : un champ absent ou une catégorie inconnue ne doit pas déclencher silencieusement une prédiction incompréhensible.

Un artefact complet inclut les transformations, le modèle et ce qui permet de les reconstruire : versions, architecture si nécessaire, ordre des variables et métadonnées utiles. Le format de soumission vérifie les identifiants, leur ordre et les colonnes requises. Un fichier créé sans erreur peut encore avoir des lignes inversées.

Le test de rechargement utilise un nouveau processus ou un état propre. On compare les prédictions avant et après sauvegarde, avec une tolérance adaptée aux nombres flottants. Une dépendance absente ou un mauvais prétraitement doit être détecté avant la démonstration.

En exploitation, une dérive d’entrée décrit une modification des données observées. Elle ne prouve pas à elle seule une perte de performance ; mesurer cette perte demande souvent les vrais labels, parfois disponibles tard. On définit quoi surveiller, quand alerter, qui vérifie et comment revenir à une version connue. Une API locale ne constitue pas à elle seule une plateforme de production sécurisée.

## Un calcul à savoir lire

Le contrat vérifie au minimum noms, types, valeurs admises et ordre des variables. Le rechargement compare les sorties sur les mêmes entrées avec une tolérance numérique annoncée. Une égalité sur un petit lot contrôle le retour de l’artefact ; elle ne mesure pas sa généralisation.

## AML_06-D1 - Exemple résolu

Le contrat attend montant et anciennete. Une entrée ne contenant que montant est incomplète : la réponse correcte est un refus explicite ou une règle d’imputation déjà définie, pas une invention silencieuse.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
attendus={'montant','anciennete'}
entree={'montant':20}
print(sorted(attendus-set(entree)))
print('entrée valide' if attendus <= set(entree) else 'entrée refusée')
```

Sortie du calcul pédagogique :

```text
['anciennete']
entrée refusée
```

## AML_06-D2 - Démonstration accompagnée

Refuser une entrée invalide explicitement. Cette démonstration est exécutée dans le notebook du chapitre, au repère **AML_06-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import math
def validate_input(row):
    required={'montant','anciennete'}
    missing=required-set(row)
    if missing: raise ValueError('Champs absents : '+','.join(sorted(missing)))
    for name in required:
        value=row[name]
        if type(value) not in (int,float) or not math.isfinite(value):
            raise ValueError('Valeur numérique finie attendue : '+name)
    return [row['montant'],row['anciennete']]
print('Entrée valide :',validate_input({'montant':20,'anciennete':3}))
try:
    validate_input({'montant':20})
except ValueError as error:
    print('Refus contrôlé :',error)
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Entrée valide : [20, 3]
Refus contrôlé : Champs absents : anciennete
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## AML_06-E1 - Expliquer

Pourquoi une variation de la distribution des entrées ne permet-elle pas toujours de calculer une nouvelle accuracy ?

## AML_06-E2 - Transférer

Un fichier de prédictions possède les bonnes colonnes mais l’ordre des identifiants a changé. Est-il forcément correct ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## AML_06-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Livrer seulement les poids ou annoncer une surveillance de performance sans accès aux cibles.

## La suite du parcours

Les mêmes contrats seront conservés lorsque les entrées deviendront des textes et des images.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
