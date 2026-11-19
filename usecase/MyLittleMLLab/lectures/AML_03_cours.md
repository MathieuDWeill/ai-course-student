# ML avancé — J3

Question du laboratoire : classer les paiements selon leur risque de fraude.

Ce cours accompagne AML_03_atelier et la feuille EXERCICES_J3. Les résultats de calcul sont locaux. Le contrôle déjà consulté en J2 reste un contrôle de développement.

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
|1|Le contrat et les acquis|45|
|2|Arbre et forêt au tableau|70|
|3|Le boosting étape par étape|60|
|4|L’enquête sur les variables|75|
|5|Recherche et décision|60|
|6|Interprétation et audit|55|
|7|Boucle Kaggle et bilan|55|

## Le même laboratoire, la bonne version

Ajouter le notebook du jour dans notebooks et conserver mllab, data et l’environnement.

Ouvrir la version renforcée et redémarrer le noyau. Les numéros de cellules ont changé.

J3 : aucune nouvelle bibliothèque.

## Un arbre pose des questions

Nœud : une question sur une variable.
Branche : une réponse.
Feuille : un groupe d’exemples et une prédiction.

## Exercice résolu · Les six montants

Règle imposée : montant ≤ 35 à gauche.
Un montant de 25 reçoit 1/3 dans cet arbre.

|Montants|Classes|Fréquence de fraude|
|---|---|---|
|10, 20, 30|0, 0, 1|1/3|
|40, 50, 60|0, 1, 1|2/3|

## Gini · Mesurer le mélange des classes

Gini = 1 − p₀² − p₁²

Une feuille pure donne 0. Deux classes à parts égales donnent 0,5.

Le critère d’une coupure est la moyenne des Gini, pondérée par les effectifs.

## La forêt · De l’aléa à une moyenne

Le bootstrap tire des lignes avec remise.
Chaque arbre peut aussi examiner un sous-ensemble de variables.
Les probabilités des arbres sont ensuite moyennées.

## Le boosting · Une fonction corrigée par étapes

Fₘ(x) = Fₘ₋₁(x) + η hₘ(x)

F : prédiction actuelle.
h : correction apprise.
η : force donnée à cette correction.

## Exemple · Commencer par une constante

Quatre entrées : 1, 2, 3, 4.
Cibles : 0, 0, 2, 2.

F₀ = moyenne des cibles = 1.
Résidus : −1, −1, +1, +1.
MSE initiale = 1.

## De la régression à la classification

Pour la perte quadratique, les résidus donnent la direction de correction.

Plus généralement, le boosting utilise le gradient négatif de la perte.

En classification, il construit des scores que la perte relie aux probabilités.

## Diagnostic · Un pas plus petit, un budget identique

80 étapes à 0,03 et 80 étapes à 0,1 ne donnent pas le même chemin d’apprentissage.

Un pas plus petit peut stabiliser, mais aussi apprendre trop peu si les étapes restent limitées.

## Catégories · Un code peut introduire un ordre

Mobile = 0, desktop = 1, tablette = 2.

Une coupure numérique traite ces codes comme ordonnés. Le traitement catégoriel cherche des regroupements de modalités.

Comparer avec le même boosting permet d’isoler cette représentation.

## Une hypothèse sur les variables positives

Montant, délai, distance et solde peuvent couvrir des échelles très étalées.

log1p(x) = log(1 + x) compresse les grandes valeurs et accepte x = 0.

Nous testons deux variantes : remplacer ou ajouter quatre colonnes.

## L’ablation · Une modification à la fois

Même C = 0,1. Mêmes trois folds.

Référence : variables originales.
Essai A : quatre variables remplacées par log1p.
Essai B : quatre colonnes log1p ajoutées.

Deux nouveaux candidats coûtent six fits.

## Le gagnant de recherche est un choix

Les scores de CV ont servi à choisir.

Plus on multiplie les essais, plus on peut sélectionner une fluctuation favorable.

Une validation déjà consultée ne redevient pas vierge après un changement de nom.

## Permutation · Ce que le modèle utilise

Mélanger une variable casse son association avec les lignes.
Mesurer la baisse d’AUC indique son utilité dans ce modèle et ce contexte.

Des variables corrélées peuvent partager leur information.

## L’audit des sous-groupes

Un score global peut masquer des comportements différents selon les paiements.

Toujours lire : effectif, nombre de fraudes, métrique et erreurs au seuil choisi.

Un petit groupe peut donner un score très instable.

## Le CSV officiel · Un contrat précis

Deux colonnes : id et is_fraud.
Une ligne par paiement test, dans le bon ordre.
Des scores finis entre zéro et un.

Les réponses du test officiel restent inconnues.

## Local et Kaggle · La même expérience

La variante Kaggle adapte les chemins et embarque le code du laboratoire.

Conserver données, folds, configuration et métrique.
Comparer les scores avant de comparer les temps.

Les variantes ont deux cellules d’amorçage supplémentaires.

## Exemple résolu : trois corrections de boosting

Pour les cibles 0, 0, 2, 2, la constante initiale vaut 1. Les résidus initiaux valent −1, −1, +1, +1. Un arbre sépare les deux premières entrées des deux dernières. Avec learning rate 0,5, la première correction donne 0,5 à gauche et 1,5 à droite. La MSE devient 0,25. Les nouveaux résidus valent −0,5 et +0,5. L’étape suivante donne 0,25 et 1,75, avec MSE 0,0625. La troisième donne 0,125 et 1,875, avec MSE 0,015625. La classification utilise un gradient de perte approprié : cet exemple de régression explique le mécanisme séquentiel, pas tout l’algorithme du classifieur.

## Exemple résolu : une comparaison appariée

Dans l’exécution de référence, remplacer quatre variables par log1p fait passer l’AUC moyenne de 0,926346 à 0,927203. Les trois deltas sont positifs, mais petits et d’amplitudes différentes : environ 0,000157, 0,000627 et 0,001787. Ajouter les colonnes donne ici 0,925001. La transformation n’est donc pas un bouton universel d’amélioration. La règle annoncée sélectionne le remplacement, mais la conclusion doit rester limitée à ce protocole. Ces chiffres ne sont pas un score public Kaggle.

## Repères exacts du notebook local

- Cellule 3 : Le contrat et le budget.
- Cellule 5 : Lire une règle et calculer Gini.
- Cellule 7 : Profondeur et mémorisation.
- Cellule 9 : Bootstrap et moyenne de forêt.
- Cellule 11 : Construire trois étapes de boosting.
- Cellule 13 : Les familles et les catégories.
- Cellule 15 : Le tournoi initial.
- Cellule 17 : Une expérience de représentation.
- Cellule 19 : Une recherche bornée.
- Cellule 21 : La décision arrêtée avant le contrôle.
- Cellule 23 : L’importance par permutation.
- Cellule 25 : L’audit des sous-groupes.
- Cellule 27 : Le candidat et le CSV Kaggle.
- Cellule 29 : Le journal et la décision.
- Cellule 31 : La vérification finale.

## Références techniques

[Scikit-learn : ensembles](https://scikit-learn.org/stable/modules/ensemble.html) et [PyTorch : optimisation](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html).
