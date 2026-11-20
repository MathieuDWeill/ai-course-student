# J3 — Feuille de travail accompagnée

Travail individuel guidé. Le professeur fait un premier exemple, vérifie une réponse intermédiaire puis corrige collectivement. Inscrire les réponses dans un document ou dans des cellules de texte du notebook. Chaque étudiant doit pouvoir expliquer le résultat.

## 1. Auditer trois annonces (15 min)

A : « 99 % sur le train ». B : « Meilleur modèle sur un nouveau split ». C : « Gain de 0,002, dix fois plus lent ». Pour chaque annonce : quelle conclusion est possible, quelle preuve manque, quelle vérification faire ensuite ?

## 2. Arbre et Gini (20 min)

Montants 10, 20, 30, 40, 50, 60. Classes 0, 0, 1, 0, 1, 1. Gini = 1 − p0² − p1².

1. Calculer les feuilles, leurs probabilités et le Gini pondéré au seuil 35.
2. Refaire au seuil 25 et comparer.
3. Prédire pour 25 et 55 avec chacun des arbres.
4. Distinguer seuil appris et profondeur maximale.

Vérification dans les cellules 5 et 7.

## 3. Construire le boosting (25 min)

Entrées 1, 2, 3, 4. Cibles 0, 0, 2, 2. F0=1. Une correction sépare les deux premières entrées des deux dernières. Learning rate 0,5.

|Étape|Prédiction à gauche|Prédiction à droite|Résidus à gauche/droite|MSE|
|---|---|---|---|---|
|0|1|1|−1 / +1|1|
|1|…|…|…|…|
|2|…|…|…|…|
|3|…|…|…|…|

Recalculer les résidus après chaque correction. Que se passe-t-il avec learning rate 1 sur ce jouet ? Quelle limite empêche de généraliser ce résultat à la fraude ? Vérification cellule 11.

## 4. Conclure sur l’ablation (25 min)

Après la cellule 17, relever les AUC moyennes de la référence, du remplacement log1p et de l’ajout log1p. Lire les deltas par fold. Écrire quatre lignes : hypothèse, preuve chiffrée, décision, limite. Un classement seul ne constitue pas une explication.

## 5. Budget de douze fits (20 min)

Douze fits au total, refit final compris. Trois folds. Combien de configurations complètes pouvez-vous comparer ? Proposer un petit espace de recherche et compter les opérations. Quel serait le coût de quatre configurations ? Distinguer fits et arbres d’une forêt.

## 6. Audit d’un sous-groupe (20 min)

Après la cellule 25, choisir un groupe. Relever effectif, nombre de fraudes, AUC et rappel au seuil 0,5. Expliquer une observation, une limite et une vérification future. Restitution de 60 secondes.

## 7. Bilan de deux minutes

Montrer un tableau et un artefact. Expliquer la question, ce qui changeait, les preuves et le modèle retenu. Donner une prochaine expérience avec budget. Compléter le journal dans runs/J3. Critères : question claire, protocole contrôlé, preuve interprétée, limite comprise.

## Pauses illustrées

Répondre individuellement avant la correction collective. [Retrouver les huit scénarios](PAUSES_POP_CULTURE.md). Pour chaque cas : une prédiction, une justification et le lien avec le notebook.
