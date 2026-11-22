# AML_04 - Comprendre la boucle d’un réseau

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Comment les poids changent-ils pendant l’apprentissage ?

## Ce que nous réutilisons

Les tableaux numériques, les pertes et les comparaisons de modèles.

## Ce que vous devez savoir montrer

Tracer entrée, sortie, perte, gradient et mise à jour dans cet ordre logique.

## Les mots du chapitre

**Logit** : Une sortie numérique avant la normalisation en probabilité.

**Perte** : Une quantité que l’apprentissage cherche à réduire.

**Gradient** : La variation locale de la perte par rapport à un paramètre.

**Learning rate** : La taille du pas utilisée par l’optimiseur.

## Comprendre le raisonnement

Un neurone calcule une combinaison pondérée de ses entrées, éventuellement suivie d’une non-linéarité. Les poids et biais sont des paramètres appris. Le learning rate, la taille du batch et le nombre d’epochs sont des choix d’entraînement, donc des hyperparamètres.

Le forward calcule les sorties ; la perte compare ces sorties aux cibles ; backward calcule les gradients ; l’optimiseur réalise la mise à jour avec step. Dans une boucle standard sans accumulation intentionnelle, on remet les gradients à zéro avant le prochain backward. Le gradient indique une variation locale de la perte, pas un nouveau poids.

Pour une classification à deux logits et CrossEntropyLoss, on donne les logits à la perte ; on n’ajoute pas softmax juste avant. Une autre formulation binaire peut utiliser un seul logit et une perte adaptée. Les contrats de formes et de cibles doivent rester cohérents.

Le mode train/eval modifie le comportement de certaines couches. no_grad désactive l’enregistrement du calcul pour les gradients ; ce n’est pas le remplacement de eval. L’early stopping sauvegarde selon une règle de validation définie ; le meilleur checkpoint peut différer du dernier. On distingue toujours perte d’apprentissage et métrique d’évaluation.

La régularisation et l’arrêt ne jouent pas le même rôle. Une pénalité L2 décourage des poids trop grands ; le weight decay modifie les mises à jour selon l’optimiseur et n’est pas toujours équivalent à ajouter L2 à la perte. Le dropout désactive aléatoirement des activations en mode train et cesse de le faire en mode eval. L’early stopping choisit un checkpoint selon une règle de validation. Ces outils ne sont pas tous activés dans chaque réseau.

## Un calcul à savoir lire

Pour la perte L(w) = (wx−y)², le gradient vaut 2(wx−y)x. Avec w=2, x=3 et y=1, il vaut 30. La mise à jour w suivant = w − learning rate × gradient donne 1,7 pour un pas de 0,01. La nouvelle perte vaut (1,7×3−1)² = 16,81.

## AML_04-D1 - Exemple résolu

Pour x=3, cible 1 et poids w=2, la prédiction est 6, la perte quadratique 25 et son gradient en w vaut 30. Un pas de 0,01 donne w=1,7 et une nouvelle perte de 16,81.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
x=3; y=1; w=2
loss=(w*x-y)**2; grad=2*(w*x-y)*x
w=w-0.01*grad
print(loss,grad,round(w,2),round((w*x-y)**2,2))
```

Sortie du calcul pédagogique :

```text
25 30 1.7 16.81
```

## AML_04-D2 - Démonstration accompagnée

Vérifier un gradient avec une différence finie. Cette démonstration est exécutée dans le notebook du chapitre, au repère **AML_04-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
w=2.; x=3.; y=1.; eps=1e-6
loss=lambda weight:(weight*x-y)**2
analytic=2*(w*x-y)*x
numeric=(loss(w+eps)-loss(w-eps))/(2*eps)
print('Gradient analytique :',round(analytic,5))
print('Différence finie :',round(numeric,5))
for lr in [.01,1.]:
    new_w=w-lr*analytic
    print('Pas :',lr,'nouveau poids :',round(new_w,3),'perte :',round(loss(new_w),3))
assert abs(analytic-numeric)<1e-6
print('Vérification scalaire ; la boucle PyTorch est dans l’atelier d’application.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Gradient analytique : 30.0
Différence finie : 30.0
Pas : 0.01 nouveau poids : 1.7 perte : 16.81
Pas : 1.0 nouveau poids : -28.0 perte : 7225.0
Vérification scalaire ; la boucle PyTorch est dans l’atelier d’application.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## AML_04-E1 - Expliquer

Après backward, les poids sont-ils forcément modifiés ? Pourquoi un grand learning rate peut-il faire augmenter la perte ?

## AML_04-E2 - Transférer

eval et no_grad font-ils exactement la même chose ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## AML_04-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Assimiler gradient et poids, oublier zero_grad ou croire qu’un réseau doit battre la logistique.

## La suite du parcours

Les représentations préentraînées en NLP et vision utiliseront la même boucle et les mêmes contrôles.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
