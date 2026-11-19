# ML avancé — J4

## 1. Le réseau comme nouveau challenger

J3 a comparé des règles et des ensembles. J4 rend visible le mécanisme d’apprentissage d’un réseau.

Un réseau contient des poids appris à partir des données. Une architecture définit les opérations et le nombre de neurones ; une fonction de perte indique ce que l’apprentissage cherche à réduire ; un optimiseur modifie les poids. Nous gardons la compétition de fraude afin de ne pas confondre changement de modèle et changement de problème. Le réseau devra être comparé à une référence linéaire et, si disponible, au tableau J3.

### Exemple résolu

Notre architecture sera entrées → 32 neurones avec ReLU → deux logits. Le travail se fait sur CPU. Le nombre de couches ne suffit pas à prédire la qualité : sur des tableaux, les arbres peuvent rester meilleurs avec moins de réglages.

### Vérifier sa compréhension

Un réseau est-il automatiquement meilleur parce qu’il contient plus de paramètres ?

**Réponse expliquée :** Non. La capacité supplémentaire peut aider, surapprendre ou coûter davantage sans améliorer la CV.

Le notebook J4 ne dépend pas des variables en mémoire de J3 : il peut démarrer après redémarrage du noyau. Si PyTorch manque, corriger l’installation avant de poursuivre ; les captures permettent au professeur de continuer sa démonstration pendant ce dépannage.

### Passage au notebook

Cellule physique 3. Installer PyTorch avant la séance dans le noyau du notebook avec %pip install "torch>=2.4,<3", puis redémarrer le noyau. Ajouter AML_04_atelier.ipynb au dossier notebooks existant. Exécuter la cellule 3 et vérifier CPU, données et trois folds.

## 2. Un calcul d’apprentissage à la main

Avant un réseau complet, un seul poids permet de comprendre la mise à jour.

Nous prenons une entrée x = 3, une cible égale à 1 et un poids w = 2. Le modèle scalaire donne une prédiction wx. La perte quadratique mesure le carré de l’écart. Cette perte sert uniquement à rendre le calcul manuel simple ; le classifieur utilisera ensuite une cross-entropy. Le gradient décrit la variation locale de la perte quand le poids change. Il dépend du point actuel, pas seulement de la formule du modèle.

### Exemple résolu

Prédiction : 3 × 2 = 6. Perte : (6 − 1)² = 25. Dérivée par rapport à w : 2(3w − 1) × 3. Au point w = 2, le gradient vaut 30. Avec un pas de 0,01, le nouveau poids vaut 1,7 et la nouvelle perte 16,81.

### Vérifier sa compréhension

Avec le même gradient de 30 et un learning rate égal à 1, quel poids et quelle perte obtient-on ?

**Réponse expliquée :** Le poids devient −28 et la perte vaut (−84 − 1)² = 7 225. Un pas plus grand peut aggraver fortement le résultat.

La descente utilise w_nouveau = w − learning_rate × gradient dans cet exemple SGD simple. Un gradient positif nous conduit à diminuer le poids localement. La garantie est locale : un déplacement trop grand peut dépasser la région où cette direction est utile.

### Passage au notebook

Cellule physique 5. Faire le calcul sur papier avant de lancer la cellule 5. Une personne donne la prédiction, une autre la perte, une troisième le gradient et une quatrième la mise à jour. Comparer ensuite les deux learning rates, sans changer le point de départ.

## 3. Les cinq lignes de la boucle

Chaque fonction a un rôle précis ; les confondre rend le débogage difficile.

zero_grad remet les gradients à zéro. Le forward produit la sortie à partir des poids actuels. La perte compare la sortie et la cible. backward calcule les gradients par rétropropagation. step utilise ces gradients pour modifier les paramètres. Dans PyTorch, les gradients s’accumulent si nous ne les remettons pas à zéro. Une accumulation volontaire existe, mais elle doit correspondre à une méthode explicite.

### Exemple résolu

Le notebook affiche le poids avant et après step. backward laisse le poids à 2 et calcule un gradient de 30. step avec SGD et un pas de 0,01 le passe à environ 1,7. Deux backward sur deux calculs identiques, sans remise à zéro, donnent un gradient accumulé de 60.

### Vérifier sa compréhension

Quelle ligne modifie les poids : backward ou step ? Que se passe-t-il sans zero_grad ?

**Réponse expliquée :** step modifie les poids dans cette boucle. Sans remise à zéro, les gradients des backward successifs s’additionnent.

La rétropropagation calcule des dérivées à travers les opérations du réseau. Elle ne corrige ni une cible inversée, ni une fuite de données, ni une mauvaise métrique. Une boucle techniquement correcte peut donc résoudre le mauvais problème si le contrat de données est faux.

### Passage au notebook

Cellule physique 7. Lire les cinq lignes à voix haute avec leur rôle, puis exécuter la cellule 7. Écrire à côté de chaque variable si elle représente un poids, une prédiction, une perte ou un gradient. Montrer l’accumulation observée à 60.

## 4. Des variables aux logits

Le réseau reçoit des nombres ; sa sortie doit respecter le contrat de la fonction de perte.

Les variables numériques sont imputées et mises à l’échelle. Les catégories sont transformées en indicateurs. Ces transformations sont apprises sur le train de chaque fit et seulement appliquées aux lignes de validation. Une couche linéaire calcule une combinaison avec poids et biais. ReLU garde les valeurs positives et remplace les négatives par zéro. Cette non-linéarité permet des fonctions plus riches qu’une succession de couches linéaires seules.

### Exemple résolu

Deux logits 0 et 2 deviennent, après softmax, environ 0,119 et 0,881. Ces nombres somment à un. CrossEntropyLoss reçoit pourtant directement les logits et des indices de classe entiers : elle réalise les opérations numériques utiles en interne. La probabilité de fraude est celle de la classe 1.

### Vérifier sa compréhension

Faut-il appliquer softmax avant CrossEntropyLoss ? Le logit 2 signifie-t-il une probabilité de 200 % ?

**Réponse expliquée :** Non dans les deux cas. Le logit est un score brut ; la perte attend ce score. Softmax sert ici à lire les probabilités après calcul.

Pour d entrées, l’architecture retenue contient d × 32 + 32 paramètres dans la première couche, puis 32 × 2 + 2 dans la seconde, soit 32d + 98. Ce comptage décrit la taille ; il ne démontre ni l’utilité de chaque poids ni une meilleure qualité.

### Passage au notebook

Cellule physique 9. Exécuter la cellule 9. Vérifier la somme des deux probabilités. Dessiner ensuite entrées → 32 neurones ReLU → 2 logits. Compter les paramètres d’une couche à trois entrées et deux sorties : six poids plus deux biais.

## 5. Batch, epoch et courbes

Une boucle courte et visible vaut mieux qu’un entraînement long difficile à interpréter.

Un batch regroupe des observations pour une mise à jour. Une epoch parcourt l’ensemble d’apprentissage. Avec 10 000 lignes et un batch de 256, une epoch demande 40 mises à jour, la dernière portant sur 16 lignes. Le nombre d’epochs, le batch et le learning rate sont des hyperparamètres. Notre budget fixe est huit epochs et le premier fold fournit une courbe de démonstration. Le contrôle externe reste à l’écart du choix.

### Exemple résolu

La cellule 11 entraîne entrées → 32 ReLU → 2 logits, avec AdamW et weight_decay fixé à 0,01. Elle affiche une perte train et une perte validation, mesurées après chaque epoch en mode eval. Ce protocole de mesure évite de confondre pertes de batch pendant apprentissage et pertes finales.

### Vérifier sa compréhension

Une baisse de la perte train accompagnée d’une hausse de la perte validation suggère quoi ? Faut-il ajouter automatiquement des epochs ?

**Réponse expliquée :** Elle peut signaler du surapprentissage. Ajouter des epochs peut aggraver la situation ; vérifier protocole, courbes et régularisation.

eval change le comportement de modules comme dropout ; no_grad désactive la construction du graphe de gradients. Ils ont des rôles distincts. Ici le réseau n’a pas de dropout. L’early stopping est expliqué comme extension ; la boucle actuelle reste à huit epochs fixes et ne choisit aucun checkpoint sur le contrôle externe.

### Passage au notebook

Cellule physique 11. Lire la fonction train_net avant de lancer la cellule 11. Repérer zero_grad, forward, loss, backward et step. Exécuter une seule fois, puis décrire le début, la fin et l’écart des deux courbes. Identifier les huit lignes correspondant aux huit epochs.

## 6. Le learning rate et la comparaison

Nous réglons une seule chose, puis nous confrontons le réseau à une référence.

Nous comparons deux learning rates, 0,001 et 0,01, sur les mêmes trois folds, avec huit epochs et la même architecture. Cela produit six entraînements neuronaux. La courbe de démonstration précédente s’ajoute à ce budget. Nous recalculons ensuite la référence logistique sur les mêmes folds. Les résultats peuvent changer selon versions et matériel ; les durées se comparent sur la même machine.

### Exemple résolu

Le tableau contient moyenne AUC, dispersion et durée pour chaque learning rate et pour la référence. La perte utilisée pour apprendre est la cross-entropy, tandis que la métrique du tournoi est la ROC-AUC. Réduire la perte ne garantit pas une amélioration identique du classement, ni une probabilité bien calibrée.

### Vérifier sa compréhension

Le réseau a une meilleure perte mais une moins bonne AUC. Quelle mesure répond au classement demandé par la compétition ?

**Réponse expliquée :** La ROC-AUC répond au classement. La cross-entropy sert à l’apprentissage et décrit aussi la qualité probabiliste selon sa définition, mais ce n’est pas le classement officiel.

Le choix du learning rate utilise la CV. Le contrôle J2 déjà vu reste un diagnostic de développement. Si le tableau J3 existe, le notebook l’affiche ; une comparaison n’est légitime que si données, sous-échantillon et folds correspondent. Un gain minuscule demande confirmation, pas une déclaration de victoire.

### Passage au notebook

Cellule physique 13. Avant de lancer la cellule 13, prévoir l’effet des deux tailles de pas. Lire le tableau sans chercher à faire gagner le réseau. Choisir le meilleur learning rate selon la CV, puis exécuter la cellule 15 pour décrire le contrôle local.

## 7. Exporter et poursuivre la boucle Kaggle

Une expérience complète termine par une décision, un artefact et une prochaine hypothèse.

Après le choix, nous refaisons l’apprentissage du réseau avec le learning rate retenu sur un échantillon stratifié du train officiel. Le test officiel sert seulement à produire les scores d’export. La prédiction se fait par blocs de 4 096 lignes pour limiter la mémoire. Nous sauvegardons le CSV, les poids et un manifeste. Le fichier de poids seul ne contient pas le prétraitement ajusté : il n’est donc pas un paquet autonome de déploiement.

### Exemple résolu

Le CSV doit conserver les identifiants et leur ordre, des probabilités finies entre zéro et un et autant de lignes que le test officiel. Un dépôt Kaggle éventuel reste manuel, après vérification des règles et de l’ouverture. Le journal conserve le score public à null tant qu’aucun résultat réel n’a été obtenu.

### Vérifier sa compréhension

Après un score décevant, faut-il augmenter en même temps les neurones, les epochs, le learning rate et le volume de données ?

**Réponse expliquée :** Pour une expérience interprétable, choisir un changement justifié et un budget. Plusieurs changements simultanés empêchent d’attribuer leur effet.

Le livrable contient comparaison.csv, courbe_demo.csv, submission_J4.csv, poids_reseau.pt, manifest.json et journal.json complété. Chaque membre explique forward, backward et step, puis justifie le modèle qu’il garderait. La suite du laboratoire pourra combiner les prédictions et vérifier si les erreurs sont complémentaires.

### Passage au notebook

Cellule physique 17. Exécuter la cellule 17 pour l’export puis 19 pour le journal. Compléter une preuve chiffrée et une décision : réseau retenu ou référence conservée. Proposer une seule expérience suivante, par exemple 16 neurones au lieu de 32 sur les mêmes folds.