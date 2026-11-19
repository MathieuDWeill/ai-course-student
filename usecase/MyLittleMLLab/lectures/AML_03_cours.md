# ML avancé — J3

## 1. Le contrat de J3

J1 : produire une première prédiction. J2 : comparer sans changer les règles. J3 : justifier la complexité et le budget.

Notre question reste le classement des paiements selon le risque de fraude. Nous disposons des mêmes observations étiquetées et de trois folds fixés. Nous allons comparer plusieurs familles, puis trois réglages d’un même algorithme. Une bonne expérience conserve les données et la métrique, annonce ce qui change et mesure aussi le temps. Le contrôle local a déjà été consulté : nous ne pouvons plus le présenter comme une évaluation finale indépendante.

### Exemple résolu

Une AUC de 0,93 mesure un classement relatif entre positifs et négatifs. Elle ne signifie ni 93 % de fraudes trouvées ni une probabilité calibrée. Pour agir, il faudrait ensuite choisir un seuil et examiner les erreurs.

### Vérifier sa compréhension

Un modèle gagne 0,01 d’AUC, mais ses lignes de validation ont changé. Peut-on attribuer le gain au modèle ?

**Réponse expliquée :** Non. La difficulté des lignes a aussi changé. Il faut comparer les candidats sur les mêmes folds.

Les modèles, leur encodage et leurs hyperparamètres peuvent changer. Les observations, les folds, la métrique et le budget annoncé restent contrôlés. Un PC plus lent peut donner un autre temps ; il faut donc comparer les durées sur la même machine.

### Passage au notebook

Cellule physique 3. Ouvrir AML_03_atelier.ipynb dans le dossier notebooks existant. Exécuter seulement la cellule 3. Retrouver les 15 000 lignes train, les trois folds et le contrôle local. Expliquer à son voisin ce qui peut changer aujourd’hui et ce qui reste fixé.

## 2. Une règle, une branche, une feuille

Un arbre transforme une succession de questions en une prédiction.

Un nœud pose une question sur une variable. Une branche correspond à une réponse. Une feuille termine le chemin. Pour une classification binaire simple, la probabilité de fraude dans une feuille est la proportion de fraudes parmi les exemples d’apprentissage arrivés dans cette feuille. L’algorithme apprend les seuils à partir du train. Nous imposons d’abord un seuil pour calculer à la main, puis nous laissons le logiciel choisir selon son propre critère.

### Exemple résolu

Montants : 10, 20, 30, 40, 50, 60. Classes : 0, 0, 1, 0, 1, 1. Avec la règle montant ≤ 35, la feuille gauche contient une fraude sur trois : 1/3. La droite contient deux fraudes sur trois : 2/3. Un montant de 25 reçoit donc 1/3 dans cet arbre illustratif.

### Vérifier sa compréhension

Pourquoi le logiciel peut-il choisir 25 ou 45 au lieu du seuil 35 dessiné au tableau ?

**Réponse expliquée :** Il cherche un seuil qui réduit son critère d’impureté. Notre seuil 35 explique le mécanisme ; il n’est pas une consigne optimale.

Le critère de Gini d’une feuille est 1 − somme des proportions au carré. À 35, l’impureté pondérée vaut 4/9. À 25 ou 45, elle vaut 1/4. Un seuil plus bas selon ce critère ne prouve pas une meilleure généralisation.

### Passage au notebook

Cellule physique 5. Dessiner les deux feuilles pour le seuil 35. Calculer les probabilités pour les montants 25 et 55. Exécuter la cellule 5 ensemble, puis lire le seuil réellement appris. Ne pas modifier les données pour forcer le résultat attendu.

## 3. La complexité et le surapprentissage

Une règle précise sur le train peut devenir fragile sur de nouvelles observations.

La profondeur compte les niveaux de décisions successives. Des feuilles nombreuses et petites permettent de reproduire plus finement les réponses du train. Cette souplesse est une capacité du modèle. Elle peut aider si les relations sont réelles, ou mémoriser des accidents de l’échantillon. Un excellent score train ne permet pas de départager ces deux situations. La validation sur des observations séparées est donc indispensable.

### Exemple résolu

Sur les six montants jouets, un arbre profond peut isoler les changements de classe et atteindre une accuracy train de 1. Un arbre peu profond garde des feuilles mélangées. Nous ne disposons ici d’aucun nouvel exemple étiqueté pour affirmer lequel généralise le mieux.

### Vérifier sa compréhension

Profondeur maximale = 2 : paramètre appris ou hyperparamètre ? Et le seuil choisi par le fit ?

**Réponse expliquée :** La profondeur maximale est un hyperparamètre donné avant le fit. Le seuil est un paramètre appris pendant le fit.

Limiter la profondeur ou augmenter le nombre minimal de lignes par feuille peut réduire la variance, mais aussi empêcher d’apprendre une relation utile. Nous ne cherchons pas une règle « plus petit est toujours meilleur ». Nous testons un compromis sur le même protocole.

### Passage au notebook

Cellule physique 7. Avant de lancer la cellule 7, prévoir quel arbre aura le plus de feuilles. Lire ensuite le tableau, entourer un score train et écrire une phrase expliquant pourquoi ce score ne suffit pas. Proposer une comparaison honnête avec de nouvelles lignes.

## 4. Forêt, boosting et catégories

Combiner des arbres peut améliorer la prédiction ; la manière de les combiner compte.

Une forêt entraîne des arbres avec de l’aléa dans les observations et les variables, puis combine leurs probabilités. Le boosting ajoute des étapes successives qui cherchent à réduire une perte. Ce sont deux mécanismes différents. Une catégorie telle que mobile ou desktop n’a pas nécessairement d’ordre numérique. Donner les codes 0, 1 et 2 à des catégories peut introduire des coupures arbitraires si le modèle les traite comme des quantités.

### Exemple résolu

Trois arbres prédisent 0,2 ; 0,5 ; 0,8 : leur moyenne vaut 0,5. Pour les catégories A, B, C codées 0, 1, 2, une coupure à 0,5 sépare A de B et C. Un traitement catégoriel peut chercher d’autres regroupements sans imposer cet ordre.

### Vérifier sa compréhension

Ajouter cent arbres qui reproduisent tous le même défaut le supprime-t-il forcément ?

**Réponse expliquée :** Non. Une combinaison aide notamment lorsque les erreurs diffèrent ; elle ne corrige pas automatiquement un biais partagé.

Le notebook marque explicitement les colonnes catégorielles du HistGradientBoostingClassifier. Les codes de catégories inconnues deviennent des valeurs manquantes pour ce modèle. Ce traitement natif est une expérience justifiée ; il ne garantit pas un gain sur tous les jeux de données.

### Passage au notebook

Cellule physique 9. Exécuter la cellule 9. Identifier le modèle linéaire, la forêt et les deux versions du boosting. Vérifier que les deux boosting gardent 80 étapes et 15 feuilles. Expliquer l’unique différence recherchée dans cette paire : la façon de traiter les catégories.

## 5. Le tournoi et le coût du calcul

Un tableau commun permet de comparer le score, la dispersion et la durée.

Chaque candidat est entraîné sur deux folds et évalué sur le troisième, à trois reprises. Les prétraitements sont ajustés dans chaque fit grâce aux pipelines. Nous calculons la moyenne et l’écart-type des trois AUC. Cet écart-type décrit la dispersion sur ces folds ; ce n’est pas un intervalle de confiance. Le temps inclut l’exécution de cette comparaison sur la machine utilisée. Les scores train aident à repérer un écart avec la CV.

### Exemple résolu

Quatre modèles sur trois folds donnent douze fits. Si un fit dure dix secondes, ces seuls entraînements coûtent environ deux minutes, auxquelles s’ajoutent préparation et prédiction. Utiliser tous les cœurs pour chaque recherche parallèle peut saturer une machine : ici n_jobs = 1.

### Vérifier sa compréhension

Le modèle A gagne 0,0002 d’AUC et prend dix fois plus de temps. Est-il automatiquement le bon choix ?

**Réponse expliquée :** Non. Il faut regarder la stabilité, le budget disponible et l’utilité du gain. Trois folds ne suffisent pas à démontrer qu’un si faible écart est robuste.

La correction s’appuie sur le tableau réellement obtenu. Si le boosting perd, ce résultat reste utile : il indique que cette configuration et cette représentation ne justifient pas encore leur coût. Nous ne modifions ni le split ni la métrique pour faire gagner un modèle préféré.

### Passage au notebook

Cellule physique 11. Prévoir le classement sans calculer, puis lancer la cellule 11 ensemble. Lire d’abord la référence linéaire, ensuite les différences de score, de dispersion et de durée. Chaque binôme défend un candidat avec deux chiffres et une limite.

## 6. Régler avec un budget annoncé

Une recherche choisit des hyperparamètres ; elle consomme des fits et réutilise les scores de validation.

Nous annonçons trois configurations : sept feuilles avec un pas de 0,1 ; quinze feuilles avec 0,1 ; quinze feuilles avec 0,03. La première paire teste la complexité, la seconde teste la force de chaque étape. Le nombre d’étapes reste fixé à 80 : un plus petit learning rate n’est donc pas assuré d’avoir le temps d’apprendre suffisamment. Le meilleur score de recherche a servi au choix et peut être optimiste.

### Exemple résolu

Trois configurations sur trois folds donnent neuf fits. Avec le tournoi précédent, le total de CV est 21 fits. Une configuration de référence est répétée volontairement dans la recherche. Le fit du candidat retenu et le refit d’export s’ajoutent à ce total.

### Vérifier sa compréhension

Peut-on essayer cent configurations, puis annoncer uniquement la meilleure AUC comme une estimation indépendante ?

**Réponse expliquée :** Non. Le choix exploite les scores. Plus les essais sont nombreux, plus on risque de sélectionner une fluctuation favorable.

La cellule 15 choisit selon la CV, puis décrit le contrôle local déjà consulté depuis J2. Elle ne transforme pas ce contrôle en test vierge. Une nouvelle compétition, une nouvelle période ou un test réellement réservé serait nécessaire pour une mesure indépendante supplémentaire.

### Passage au notebook

Cellule physique 13. Avant la cellule 13, annoncer l’effet attendu de sept feuilles au lieu de quinze. Lancer la recherche sans agrandir la grille. Construire ensuite le tableau hypothèse / résultat / décision. Exécuter la cellule 15 après avoir arrêté le choix.

## 7. Interpréter, exporter et décider

Un résultat Kaggle utile associe une prédiction valide à une explication traçable.

La permutation mélange une variable sur les lignes de contrôle et mesure la baisse d’AUC. Une forte baisse suggère que le modèle utilisait cette information dans ce contexte. Ce n’est pas une preuve causale. Des variables corrélées peuvent se remplacer et partager l’importance. Nous exportons ensuite des scores continus pour tout le test officiel, dans l’ordre des identifiants du fichier exemple. Aucun dépôt n’est automatique.

### Exemple résolu

Un CSV valide contient exactement id et is_fraud, une ligne par paiement test et des valeurs finies entre zéro et un. Il ne contient pas les classes seulement 0 ou 1 pour ce classement. Le manifeste conserve les empreintes des données, le modèle retenu et le budget.

### Vérifier sa compréhension

Une variable importante prouve-t-elle qu’en la modifiant on réduirait la fraude ?

**Réponse expliquée :** Non. L’importance mesure un usage prédictif du modèle. Elle peut refléter des relations indirectes ou des variables corrélées.

Le livrable attendu contient tournoi.csv, recherche.csv, importance.csv, submission_J3.csv, manifest.json et journal.json complété. Conserver le modèle simple s’il reste préférable est une conclusion acceptable. J4 ajoutera un réseau comme nouveau challenger sur le même protocole.

### Passage au notebook

Cellule physique 17. Exécuter 17, lire trois variables et une limite. Exécuter ensuite 19 pour le CSV et 21 pour le journal. Compléter réellement le journal : hypothèse, preuve chiffrée, décision et prochaine expérience. Vérifier les règles et la possibilité actuelle de dépôt sur Kaggle.