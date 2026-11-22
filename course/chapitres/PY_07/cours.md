# PY_07 - Défendre un résultat et une décision

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Quelle décision les résultats permettent-ils de défendre ?

## Ce que nous réutilisons

Les six étapes précédentes : de la question à l’analyse reproductible.

## Ce que vous devez savoir montrer

Distinguer qualité de prédiction, règle d’action et conséquences.

## Les mots du chapitre

**Prédiction** : La sortie d’un modèle pour une entrée.

**Seuil** : Une règle transformant un score en classe ou en action.

**Coût** : Une conséquence chiffrée selon des hypothèses d’usage.

**Limite** : Une condition au-delà de laquelle la conclusion n’est plus justifiée.

## Comprendre le raisonnement

Une restitution explique le problème, les données, l’expérience et ce que le résultat permet de décider. Le score arrive après le protocole. Le lecteur doit comprendre la référence, les observations évaluées, les limites et le coût des erreurs. Une application agréable ne corrige pas une cible mal définie.

Prédire et agir sont deux étapes distinctes. Un score de risque sert à ordonner ou estimer, puis une règle transforme ce score en action. Le seuil dépend de la capacité d’intervention, du coût des fausses alertes et du coût des événements ratés. Une bonne métrique de classement ne définit pas automatiquement la meilleure règle d’action.

Les coûts utilisés dans un exercice sont des hypothèses pédagogiques, pas des lois universelles. On les écrit et on montre comment la décision change si elles changent. Dans une simulation économique, il faut également préciser frais, horizon, montant engagé et scénario ; une prévision raisonnable peut conduire à une stratégie perdante.

Une contribution individuelle se voit dans une hypothèse expliquée, une modification comprise et une erreur commentée. Un assistant de code peut accélérer l’exécution, mais ne remplace pas cette compréhension. La conclusion peut être « nous n’avons pas battu la référence » si cette affirmation repose sur une comparaison honnête.

## Un calcul à savoir lire

Coût = nombre de fausses alertes × coût d’une fausse alerte + nombre d’événements ratés × coût d’un raté. Avec les hypothèses 2 et 20 : une fausse alerte et un raté coûtent 22 ; trois fausses alertes et aucun raté coûtent 6. Ces coûts sont des hypothèses d’usage.

## PY_07-D1 - Exemple résolu

Une fausse alerte coûte 2 et un événement raté coûte 20. Une stratégie avec une fausse alerte et un raté coûte 22. Une autre avec trois fausses alertes et aucun raté coûte 6, sous ces hypothèses.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
cout_fausse_alerte=2; cout_rate=20
print(1*cout_fausse_alerte+1*cout_rate)
print(3*cout_fausse_alerte+0*cout_rate)
```

Sortie du calcul pédagogique :

```text
22
6
```

## PY_07-D2 - Démonstration accompagnée

Le seuil change le coût, pas les scores. Cette démonstration est exécutée dans le notebook du chapitre, au repère **PY_07-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
y=[0,1,0,1,0,0]
scores=[.1,.8,.4,.6,.2,.3]
for seuil in [.3,.5,.7]:
    pred=[int(p>=seuil) for p in scores]
    fp=sum(a==0 and b==1 for a,b in zip(y,pred))
    fn=sum(a==1 and b==0 for a,b in zip(y,pred))
    print('Seuil',seuil,'fausses alertes',fp,'ratés',fn,'coût',2*fp+20*fn)
print('Coûts pédagogiques : fausse alerte=2, événement raté=20.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Seuil 0.3 fausses alertes 2 ratés 0 coût 4
Seuil 0.5 fausses alertes 0 ratés 0 coût 0
Seuil 0.7 fausses alertes 0 ratés 1 coût 20
Coûts pédagogiques : fausse alerte=2, événement raté=20.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## PY_07-E1 - Expliquer

Un modèle A obtient un meilleur score global mais deux fois plus d’erreurs graves pour l’usage prévu. Peut-on le choisir automatiquement ?

## PY_07-E2 - Transférer

Les coûts de fausse alerte et d’événement raté s’inversent. La stratégie retenue doit-elle forcément rester la même ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## PY_07-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Présenter le classement ou la réussite d’une simulation comme une preuve d’efficacité dans tous les contextes.

## La suite du parcours

Le ML avancé conserve la question et la décision ; il rend les comparaisons et les livraisons plus rigoureuses.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
