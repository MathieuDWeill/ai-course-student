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
