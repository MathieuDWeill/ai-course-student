# ML avancé — J4

Question du laboratoire : classer les paiements selon leur risque de fraude.

Ce cours accompagne AML_04_atelier et la feuille EXERCICES_J4. Les résultats de calcul sont locaux. Le contrôle déjà consulté en J2 reste un contrôle de développement.

## J1 et J2 · Ce que nous savons déjà faire

J1 : données, référence constante, logistique, premier score et run sauvegardé.

J2 : contrôle des fuites, mêmes folds, seuils, erreurs et CSV officiel.

Le contrôle local déjà consulté reste un diagnostic de développement.

## L’évolution de notre méthode

Nous conservons la question et nous renforçons la méthode.

|Étape|Question principale|Preuve attendue|
|---|---|---|
|J1|La boucle fonctionne-t-elle ?|Référence, score local, run|
|J2|La comparaison est-elle fiable ?|Folds fixes, contrôle des fuites|
|J3|Quelle complexité est utile ?|Ablation, AUC, coût, budget|
|J4|Comment le réseau apprend-il ?|Gradients, courbes, même CV|

## Les sept étapes de la journée

Les durées comprennent explications, démonstrations et corrections. Les pauses s’ajoutent au temps pédagogique.

|Bloc|Travail|Minutes|
|---|---|---|
|1|Du poids à la mise à jour|55|
|2|Un batch entièrement visible|65|
|3|Non-linéarité et entrées réelles|65|
|4|La boucle et ses courbes|65|
|5|Réglage et arrêt|65|
|6|Contrôle et transfert|60|
|7|Explication et bilan|45|

## Le même laboratoire, la bonne version

Ajouter le notebook du jour dans notebooks et conserver mllab, data et l’environnement.

Ouvrir la version renforcée et redémarrer le noyau. Les numéros de cellules ont changé.

J4 : PyTorch installé avant la séance, ou variante Kaggle sur CPU.

## J3 · La leçon à conserver

La représentation peut changer un modèle autant que son nom.

Nous avons comparé quatre candidats, deux variantes de log1p et trois réglages : 27 fits CV.

Un petit gain moyen mérite une conclusion prudente.

## Un poids · Le calcul complet

x = 3, cible = 1, poids w = 2.
Prédiction = 3w = 6.
Perte L = (3w − 1)² = 25.
Gradient dL/dw = 2(3w − 1) × 3 = 30.

## Le batch miniature · Toutes les valeurs visibles

Trois observations, deux variables, deux classes.

X a la forme (3, 2).
W a la forme (2, 2).
Z = XWᵀ + b a la forme (3, 2).

## Calcul de la première observation

x = [1, 0], biais = [0, 0].
Poids classe 0 : [0,2 ; −0,1].
Poids classe 1 : [−0,3 ; 0,4].

Logit 0 = 0,2. Logit 1 = −0,3.

## Softmax et cross-entropy

Softmax transforme les logits en probabilités qui somment à 1.

Pour une observation : perte = −log(probabilité de la vraie classe).

CrossEntropyLoss reçoit directement les logits et les indices de classe.

## La limite d’une frontière linéaire

XOR : [0,0] et [1,1] appartiennent à la classe 0.
[0,1] et [1,0] appartiennent à la classe 1.

Une droite ne peut pas séparer ces deux paires alternées.

## Des neurones et une non-linéarité

Couche linéaire : une combinaison avec poids et biais.
ReLU : max(0, z).
Seconde couche : combinaison des représentations intermédiaires.

Deux couches linéaires sans non-linéarité restent une transformation affine.

## La boucle réelle · Les mêmes cinq opérations

Le petit batch a montré chaque calcul.
La boucle complète le répète sur tous les batches.

Architecture fixe : d entrées, 32 ReLU, 2 logits.
Budget de comparaison : huit epochs, batch 256.

## Lecture du code · Le cœur d’un batch

Une seule mise à jour se trouve dans ces lignes.

## Batch et epoch · Le compte des opérations

10 000 lignes, batch 256 : 40 mises à jour par epoch.
Huit epochs : 320 mises à jour pour un entraînement.

Deux learning rates et trois folds : six réseaux, soit 1 920 mises à jour pour ce budget.

## Early stopping · Une règle explicite

Critère : perte de validation interne.
Maximum : 40 epochs.
Patience : trois epochs sans amélioration suffisante.

Conserver et recharger le meilleur checkpoint.

## Dropout, weight decay et arrêt

Dropout modifie certaines activations pendant l’apprentissage.
Weight decay agit sur les poids selon l’optimiseur.
Early stopping choisit une durée et un checkpoint selon un critère.

Ces mécanismes ne sont pas interchangeables.

## Un artefact complet demande plus que des poids

Conserver l’architecture et le nombre d’entrées.
Sauvegarder les poids.
Sauvegarder le prétraitement ajusté.
Conserver les versions et la configuration.

## Le bilan individuel · Six réponses précises

Forward produit quoi ?
Backward calcule quoi ?
Step change quoi ?
Pourquoi zero_grad ?
Pourquoi la CV ?
Pourquoi garder le prétraitement ?

## Ce que nous pouvons désormais expliquer

Une expérience complète relie question, données et protocole.

Nous savons suivre une mise à jour et examiner une courbe.
Nous savons confronter un réseau à une référence.
Nous savons sauvegarder et vérifier ses prédictions.

## Exemple résolu : un pas sur un poids

Pour L=(3w−1)², le gradient vaut 2(3w−1)×3. À w=2, la prédiction vaut 6, la perte 25 et le gradient 30. Avec learning rate 0,01, le nouveau poids vaut 1,7 et la perte 16,81. Le gradient recalculé vaut 24,6. Le deuxième pas donne w=1,454 et une perte de 11,303044. Avec learning rate 1 depuis le point initial, w devient −28 et la perte 7 225. Un grand pas peut donc dépasser une région où la direction locale était utile.

## Exemple résolu : la perte du petit batch

Les logits sont [0,2 ; −0,3], [−0,1 ; 0,4] et [0,1 ; 0,1]. Les classes sont 0, 1 et 1. Les probabilités correctes des deux premières lignes valent environ 0,622459, et celle de la troisième 0,5. Les pertes sont environ 0,474077, 0,474077 et 0,693147, soit une moyenne 0,547100. CrossEntropyLoss calcule ce contrat à partir des logits directement. La mise à jour du petit exemple au pas 0,1 abaisse ensuite la perte du batch à environ 0,524911. Cette baisse décrit l’apprentissage de ces trois lignes, pas la généralisation.

## Exemple résolu : arrêt et checkpoint

Pour les pertes 0,50 ; 0,35 ; 0,36 ; 0,37 ; 0,38, une patience de trois arrête après l’epoch 5 et conserve les poids de l’epoch 2. Arrêter sans recharger les meilleurs poids garderait les dernières valeurs, donc un autre modèle. Une sélection sur la perte n’est pas automatiquement une sélection sur l’AUC. La démonstration du notebook est séparée de la comparaison des réseaux à huit epochs fixes.

## Repères exacts du notebook local

- Cellule 3 : Le contrat et les ressources.
- Cellule 5 : Un poids et deux tailles de pas.
- Cellule 7 : Les rôles de backward et step.
- Cellule 9 : Un batch visible, une couche visible.
- Cellule 11 : Logits, softmax et cross-entropy.
- Cellule 13 : Les gradients de chaque poids.
- Cellule 15 : Pourquoi ajouter une non-linéarité.
- Cellule 17 : Les transformations numériques.
- Cellule 19 : Les dimensions et la référence constante.
- Cellule 21 : La boucle tabulaire complète.
- Cellule 23 : Les courbes sur un fold.
- Cellule 25 : train, eval et no_grad.
- Cellule 27 : Deux learning rates, trois folds.
- Cellule 29 : Un early stopping explicite.
- Cellule 31 : Le contrôle après le choix.
- Cellule 33 : Exporter un candidat complet.
- Cellule 35 : Vérifier le retour des artefacts.
- Cellule 37 : Le journal et la décision.

## Références techniques

[Scikit-learn : ensembles](https://scikit-learn.org/stable/modules/ensemble.html) et [PyTorch : optimisation](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html).
