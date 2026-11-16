# ML avancé 1 — Comprendre ce que prédit un modèle

## Objectif

Distinguer une observation, ses caractéristiques, sa cible, une prévision et une décision.

## 1. Partir d’une question que l’on comprend

Un programme peut exécuter des milliers de calculs sans répondre à une question utile. Notre premier travail consiste donc à formuler ce que nous cherchons. Dans le fil rouge du cours, nous voulons classer des paiements selon leur risque de fraude. Nous n’essayons pas encore de décider automatiquement qui doit être bloqué. Cette différence est importante : classer des risques et prendre une décision sont deux tâches liées, mais distinctes.

Nous retrouvons QUID. La question décrit le problème. L’unité indique ce que représente une observation : ici, un paiement. L’indicateur permet d’évaluer le résultat. La décision précise ce que l’on fera de l’information. Si l’on oublie cette dernière étape, on peut construire un bon classement sans savoir comment l’utiliser. Si l’on mélange plusieurs unités, par exemple une ligne par client et une ligne par paiement, les calculs peuvent devenir difficiles à interpréter.

Les données du Playground fraude sont synthétiques. Elles servent à pratiquer une tâche de compétition ; elles ne prouvent pas que notre modèle fonctionnerait tel quel sur les transactions d’une banque. Les exemples minuscules de ce chapitre sont également pédagogiques. Leur intérêt est de permettre de vérifier chaque opération avant de la retrouver dans le notebook.

## 2. Lire une ligne du tableau

Une ligne contient des caractéristiques de l’observation : un montant, un nombre de paiements récents ou une catégorie de commerçant. Ces caractéristiques sont les entrées du modèle. On les note souvent X. Dans un historique étiqueté, la ligne contient aussi une réponse connue, appelée cible et souvent notée y. Ici, y vaut 1 pour une fraude et 0 pour une absence de fraude.

La cible sert à apprendre et à vérifier. Elle ne doit pas être fournie au modèle parmi les caractéristiques au moment où il prédit. Sinon, le programme pourrait utiliser directement la réponse. Une information calculée après la découverte de la fraude peut créer le même problème, même si sa colonne ne s’appelle pas « cible ». Pour chaque variable, demandons-nous donc : aurions-nous réellement cette information au moment de traiter le paiement ?

Un identifiant permet de retrouver une ligne et d’aligner des fichiers. Il ne constitue pas automatiquement une caractéristique pertinente. Dans notre pipeline de départ, la colonne id est conservée pour les échanges, mais retirée des entrées apprises. Il faut pouvoir expliquer ce choix, plutôt que supprimer ou conserver une colonne seulement parce qu’elle est numérique.

## 3. Une probabilité n’est pas une étiquette

Un modèle peut produire un nombre compris entre 0 et 1. Par exemple, 0,70 indique un score interprété comme une probabilité de fraude. Ce nombre n’est ni la cible réelle, ni une certitude. Un modèle qui annonce 0,70 peut se tromper sur ce paiement. Et tous les modèles ne produisent pas des probabilités bien calibrées : annoncer 0,70 ne garantit pas que exactement sept cas sur dix seront frauduleux dans tous les contextes.

Pour transformer une probabilité en alerte, on peut fixer un seuil. Si le seuil vaut 0,50, on déclenche une alerte lorsque le score est supérieur ou égal à 0,50. Le signe « égal » fait partie de la règle : un score de 0,50 déclenche alors une alerte. Abaisser le seuil déclenche davantage d’alertes sur les mêmes scores. Cela peut permettre de rater moins de fraudes, mais aussi provoquer davantage de fausses alertes.

Changer le seuil ne réentraîne pas le modèle. Les scores restent identiques ; seule la règle d’action change. À l’inverse, modifier les données d’apprentissage ou les paramètres du modèle peut changer les scores eux-mêmes. Dans un compte rendu, il faut dire précisément ce qui a changé.

## 4. Décrire les erreurs avec des mots précis

Une vraie fraude qui déclenche une alerte est un vrai positif. Un paiement normal qui déclenche une alerte est un faux positif, ou fausse alerte. Une fraude sans alerte est un faux négatif, ou fraude ratée. Un paiement normal sans alerte est un vrai négatif. On rassemble ces quatre nombres dans une matrice de confusion.

L’accuracy est la proportion de décisions correctes. La précision répond à la question : parmi mes alertes, quelle part correspond à une fraude ? Le rappel demande : parmi les fraudes réelles, quelle part ai-je détectée ? Le F1 combine précision et rappel. Ces mesures ne sont pas interchangeables. Dans un ensemble de 1 000 paiements contenant seulement 10 fraudes, toujours répondre « pas de fraude » donne 99 % d’accuracy, mais un rappel nul.

La compétition fraude utilise la ROC-AUC. Pour en comprendre l’idée, prenons une fraude et un paiement normal : le modèle place-t-il la fraude au-dessus du paiement normal ? Sur toutes ces paires, on mesure la qualité du classement, avec un demi-point pour une égalité. Une AUC de 1 correspond à un classement parfait sur les observations évaluées. Une AUC de 0,5 correspond à un classement sans pouvoir discriminant dans ce sens. Cela ne signifie pas « la moitié des fraudes détectées ».

## 5. Retrouver ces idées dans Python

Avant d’exécuter une cellule, on doit pouvoir dire quelles données elle lit et quelle sortie elle produit. Une cellule peut charger un tableau, apprendre un modèle ou calculer une mesure : ce ne sont pas les mêmes actions. Les fonctions du laboratoire regroupent plusieurs opérations pour rendre le notebook lisible. Nous commencerons par comprendre leur contrat d’entrée et de sortie, puis nous ouvrirons leurs détails progressivement.

La baseline, ou référence simple, donne un premier résultat facile à reproduire. Pour une classification binaire, on peut prévoir la même probabilité pour toutes les lignes, calculée sur le train. Cette référence ne classe pas les paiements entre eux : son AUC vaut 0,5 lorsque les deux classes sont présentes. Un modèle plus complexe doit montrer ce qu’il apporte face à cette référence, sur les mêmes observations.

Le premier objectif n’est donc pas de modifier dix paramètres. Il est de lire une ligne, distinguer cible et prévision, comprendre la mesure utilisée et retrouver le fichier produit. Une fois ces gestes acquis, nous pourrons chercher une amélioration sans perdre le sens du calcul.

## Exemple résolu

Nous fixons le seuil d’alerte à 0,50. Lisons la première ligne ensemble, puis complétons les autres.

|Paiement|Cible réelle|Score|Alerte au seuil 0,50|
|---|---|---|---|
|A|0|0,10|Non|
|B|1|0,70|Oui|
|C|0|0,20|Non|
|D|1|0,40|Non|
|E|0|0,60|Oui|
|F|0|0,05|Non|

B est une fraude détectée. E est une fausse alerte. D est une fraude ratée. A, C et F sont des paiements normaux correctement laissés sans alerte. On compte donc TP=1, FP=1, FN=1 et TN=3. L’accuracy vaut 4/6 ; la précision, le rappel et le F1 valent 0,50. Pour l’AUC, le positif B gagne ses quatre comparaisons avec les négatifs ; le positif D en gagne trois sur quatre. Le total donne 7/8, soit 0,875.

## À retenir

La cible est la réponse connue ; le score est une prévision ; le seuil définit une règle d’action.

## Confusion à éviter

Ne pas confondre « le modèle classe bien les risques » avec « notre politique d’alerte est adaptée ».

## Questions de compréhension

1. Dans l’exemple, quelle différence y a-t-il entre la cible 1 de D et son score 0,40 ?

2. Si le seuil devient 0,30, quels paiements déclenchent une alerte ?

3. Un modèle qui a une bonne AUC a-t-il forcément une bonne règle d’alerte au seuil 0,50 ?

4. Pourquoi calculer une baseline avant d’essayer un modèle plus compliqué ?

## Passage au notebook

Retrouver une entrée, un calcul et une sortie de ce chapitre dans le notebook AML correspondant. Exécuter une cellule, expliquer le résultat, puis seulement passer à la variation demandée.
