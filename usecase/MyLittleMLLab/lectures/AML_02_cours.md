# ML avancé 2 — Évaluer sans utiliser la réponse à l’avance

## Objectif

Expliquer les rôles des ensembles et repérer une fuite d’information.

## 1. Pourquoi réserver des observations ?

Imaginez un examen dont vous connaissez déjà les questions et leurs réponses. Une bonne note prouverait surtout que vous les avez retenues. L’évaluation d’un modèle pose un problème comparable. Si l’on mesure ses performances sur les exemples qui ont servi à le construire, on ne sait pas s’il saura traiter de nouvelles observations. Un programme peut mémoriser sans apprendre une règle utile.

Nous séparons donc plusieurs rôles. Le train sert à apprendre. La validation sert à comparer les méthodes et à choisir leurs réglages. Le test final sert à évaluer une solution dont les choix sont déjà fixés. Les noms des fichiers ne suffisent pas : si l’on utilise un fichier appelé test pour choisir ses réglages à répétition, il joue en pratique le rôle d’une validation.

Le découpage doit représenter la question réelle. Prédire de nouveaux paiements demain n’est pas exactement la même tâche que compléter au hasard des lignes d’un tableau ancien. Reconnaître une personne déjà vue et reconnaître une nouvelle personne sont également deux usages différents. Un split est une hypothèse sur le monde dans lequel on utilisera le modèle.

## 2. Ce qui peut traverser une frontière

La fuite la plus évidente consiste à utiliser la cible comme entrée. Mais une fuite peut aussi venir d’un doublon, d’un même individu présent des deux côtés ou d’une information connue seulement plus tard. Un score peut alors devenir excellent sans que le modèle réponde à la question annoncée. Le programme ne signale pas forcément d’erreur : c’est notre protocole qui est faux.

Prenons trois photographies d’un même objet. Si deux servent à apprendre et la troisième à valider, le modèle peut reconnaître le fond, l’éclairage ou des détails propres à cet objet. Si l’objectif est de reconnaître de nouveaux objets, il faut séparer les objets, pas seulement les fichiers. On parle alors de split par groupe.

Pour les tweets, garder les textes identiques dans le même ensemble évite une forme de contamination. Cela ne règle pas tout : des textes presque identiques, un événement commun ou un auteur commun peuvent encore faciliter l’évaluation. Le protocole doit donc être présenté avec ce qu’il contrôle et ce qu’il ne contrôle pas.

## 3. Respecter le temps et la disponibilité

Pour une tâche temporelle, on apprend généralement sur le passé et on évalue sur une période suivante. Mais trier les dates d’origine ne suffit pas toujours. Une observation de juin peut contenir une cible qui ne sera connue qu’en août. Au début de juillet, cette cible reste dans le futur, même si la ligne porte une date ancienne.

Dans le cas Zillow, une variation à six mois demande de connaître la valeur de sortie six mois plus tard. Pour construire les exemples d’apprentissage disponibles avant une date de validation, il faut vérifier la fin de chaque cible. Les exemples dont la cible se termine trop tard doivent être retirés du train : c’est l’idée d’une purge temporelle.

La disponibilité d’une variable compte également. Une information collectée aujourd’hui mais publiée le mois prochain n’est pas utilisable pour une décision prise aujourd’hui. On ne peut pas corriger ce problème simplement en déplaçant la ligne dans un autre fichier. Il faut documenter le moment où l’information est réellement accessible.

## 4. Préparer les données sans contaminer l’évaluation

Certaines transformations apprennent une information du jeu de données. Remplacer les valeurs manquantes par une médiane demande de calculer cette médiane. Standardiser une variable demande d’apprendre sa moyenne et son écart-type. Construire un vocabulaire de texte apprend quels mots sont présents. Ces opérations font partie de l’apprentissage, même si elles précèdent le modèle.

Si l’on calcule ces informations sur tout le tableau avant le split, la validation influence déjà la préparation. Il faut au contraire ajuster la transformation sur le train et l’appliquer ensuite aux autres ensembles. Par exemple, avec des valeurs train 10, manquante et 20, la médiane disponible vaut 15. Ajouter une valeur de validation 1 000 avant le calcul changerait la médiane à 20 : le train aurait reçu une information extérieure.

Un pipeline regroupe les transformations et le modèle pour respecter cet ordre. Il ne rend pas automatiquement le protocole correct : un mauvais split reste mauvais. Son intérêt est de rendre reproductible la chaîne « apprendre la préparation sur train, transformer les autres lignes, apprendre puis prédire ».

## 5. Comprendre la validation croisée

Un unique split peut donner une impression trop favorable ou défavorable. La validation croisée répartit les données de développement en plusieurs parties, appelées folds. Chaque partie est évaluée par un modèle entraîné sur les autres. On obtient plusieurs scores et des prédictions hors fold, souvent appelées OOF.

Chaque prédiction OOF provient donc d’un modèle qui n’a pas appris sur la ligne correspondante. Les transformations apprises doivent, elles aussi, être réajustées à chaque entraînement. Une stratification aide à répartir les classes ; un découpage par groupe protège les groupes ; un découpage temporel traite l’ordre. Ces choix ne sont pas interchangeables.

La dispersion des scores renseigne sur la sensibilité au découpage. Elle ne constitue pas automatiquement un intervalle de confiance : les entraînements et les ensembles se recoupent. Enfin, si l’on essaie énormément de variantes sur les mêmes OOF, on peut finir par s’adapter à leurs particularités. La validation n’est pas une ressource infinie que l’on peut interroger sans conséquence.

## Exemple résolu

Les lettres désignent une source commune ; les nombres désignent plusieurs observations de cette source.

|Train proposé|Validation proposée|Problème|
|---|---|---|
|A1, A2|A3|La source A traverse la frontière|
|B1|B2|La source B traverse la frontière|
|C1|C2|La source C traverse la frontière|
|-|D1|D est une source nouvelle|

Si l’usage visé porte sur de nouvelles sources, ce split évalue mal la question. Une séparation possible garde A, B et C dans le train et D dans la validation. Cet exemple montre le principe ; une vraie évaluation doit aussi disposer d’assez de groupes et de classes pour permettre une mesure utile.

## À retenir

Une évaluation crédible reproduit les informations disponibles dans la situation où l’on veut prédire.

## Confusion à éviter

Un pipeline protège l’ordre de préparation ; il ne répare pas un split inadapté.

## Questions de compréhension

1. Quelle différence y a-t-il entre validation et test final ?

2. Pourquoi la médiane doit-elle être apprise sur le train ?

3. Peut-on utiliser en juillet un label de juin qui n’est connu qu’en août ?

4. Une bonne OOF prouve-t-elle que le modèle réussira sur n’importe quel futur jeu ?

## Passage au notebook

Retrouver une entrée, un calcul et une sortie de ce chapitre dans le notebook AML correspondant. Exécuter une cellule, expliquer le résultat, puis seulement passer à la variation demandée.


# Atelier Kaggle : de la validation à une soumission

## La question de compétition

Nous participons à Predicting Credit Card Fraud, sur les données officielles déjà utilisées en J1. Le train officiel contient is_fraud. Le test officiel contient les paiements à scorer, sans cette cible. Le sample_submission décrit le contrat du fichier final. Nous cherchons une configuration qui classe les fraudes au-dessus des paiements normaux. Les règles et la page Evaluation de la compétition restent la référence pour le dépôt.

## Comprendre la ROC-AUC avec quatre paiements

Deux fraudes et deux paiements normaux forment quatre paires de classes différentes. Avec les cibles [1,1,0,0] et les scores [0.9,0.6,0.4,0.1], toutes les paires sont bien ordonnées : AUC 1. Avec [0.9,0.2,0.8,0.1], trois paires sur quatre sont bien ordonnées : AUC 0.75. En cas d’égalité, la paire reçoit un demi-crédit. Un score constant vaut 0.5 quand les deux classes sont présentes. Cette mesure décrit un classement. Elle ne donne pas le pourcentage de classes prédites correctement ni une garantie de calibration des probabilités.

## Comparer les configurations (cellule 32)

Nous annonçons trois candidats : dummy, logistique avec C=0.1 et boosting avec 80 itérations et 15 feuilles maximales. Le dummy prédit un score constant. La logistique apprend des coefficients. Le boosting ajoute successivement des petits arbres pour améliorer la fonction apprise. Notre pipeline de boosting traite les codes ordinaux des catégories comme des nombres, ce qui constitue une limite de cette configuration.

Les données, les trois folds stratifiés et la métrique restent identiques. Les transformations sont réapprises dans chaque fold. Trois candidats et trois folds nécessitent neuf apprentissages. Les secondes mesurées dépendent de l’ordinateur. Une victoire locale concerne ces configurations, ces données et ce protocole. Elle ne classe pas universellement les familles de modèles.

## Choisir puis contrôler (34 et 36)

Nous enregistrons le gagnant de la moyenne CV dans selection.json avant de consulter va. Nous réapprenons ensuite sur tout tr et mesurons sur va. Si nous utilisons ce contrôle pour changer les paramètres, il participe à nos choix. Il ne peut plus être présenté comme une évaluation finale indépendante.

## Décrire les erreurs (38)

Le seuil 0.5 illustre les erreurs du modèle retenu sur va. Une fraude sous le seuil est manquée et un paiement normal au-dessus produit une fausse alerte. Un bon classement AUC peut coexister avec un faible rappel à ce seuil. Les chiffres de cette cellule ne se comparent pas directement à ceux des anciens OOF : la configuration et les observations évaluées diffèrent.

## Produire le fichier de compétition (40)

Le modèle choisi réapprend sur un échantillon stratifié du train officiel, limité à LIMIT pour cette version CPU. Il prédit ensuite tout le test officiel. Cette étape peut réutiliser des lignes auparavant dans va, après le choix fixé. Va ne mesure donc pas indépendamment ce modèle réappris. Aucun label du test officiel n’entre dans le calcul.

Nous gardons les scores continus pour la ROC-AUC. Un seuil écrase leur ordre en deux classes. Les assertions contrôlent colonnes, taille, ordre des IDs, unicité et nombres finis compris entre zéro et un. Le fichier possède autant de lignes que le test officiel. Ces contrôles vérifient le format, pas la qualité du modèle. La cellule ne transmet rien à Kaggle.

## Déposer et apprendre du retour (42)

Après lecture des règles et des modalités affichées, le dépôt manuel utilise le fichier submission.csv du dossier annoncé. Sa description indique modèle, paramètres, taille du train et protocole. Le score public reste None jusqu’au retour effectif de Kaggle. Le journal relie ensuite ce score à l’expérience. Le résultat local ne permet pas de déduire le score public.

Les ensembles évalués, le réapprentissage et la sélection répétée peuvent contribuer à des écarts entre validation locale et classement. Nous examinons d’abord le bon fichier et le protocole. Nous évitons de transformer les dépôts successifs en recherche aveugle sur le score public. Chaque expérience suivante formule une hypothèse et modifie une chose identifiable.

## Budget de calcul

Quatre réglages sur cinq folds demandent vingt apprentissages. À trente secondes par apprentissage, cela représente dix minutes séquentielles avant les frais supplémentaires. Un GPU n’accélère pas automatiquement le code scikit-learn. Nous réduisons d’abord le nombre d’essais ou le volume pour explorer, puis vérifions la configuration retenue sur un protocole adapté au volume supérieur.

Sources : [compétition](https://www.kaggle.com/competitions/playground-series-s6e11), [ROC-AUC](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html), [validation croisée](https://scikit-learn.org/stable/modules/cross_validation.html), [boosting](https://scikit-learn.org/stable/modules/ensemble.html).
