# Séance 1 — Can You Beat Randomness?

Objectif enseignant : faire comprendre que la Data Science ne commence pas avec Python, mais avec le doute méthodique.

Notebook principal : `notebooks/01_python_data_science/B1_S00_Can_You_Beat_Randomness.ipynb`

Plan B sans dataset Kaggle : `notebooks/01_python_data_science/B1_S00_S01_onboarding_google_trends.ipynb`

Durée cible : 3h30

## Message d'ouverture

"Le cours s'appelle Python for Data Science. Mais je ne vais pas vous demander de mémoriser pandas comme une table de multiplication. Une IA peut écrire beaucoup de code. Ce que vous devez apprendre, c'est poser la bonne question, détecter les faux signaux, vérifier une analyse et transformer un résultat en décision fiable."

"Première question : can you beat randomness?"

## Promesse de séance

À la fin, les étudiants doivent retenir :
- randomness is not intuitive;
- a pattern is not automatically a signal;
- Data Science is often about proving that a pattern is fake;
- Python is the instrument, not the objective.

## Déroulé

### 0:00-0:15 — Hook

Afficher la question : "Can you beat randomness?"

Demander aux étudiants :
- "Quels numéros EuroMillions sortent le plus souvent selon vous ?"
- "Un numéro froid est-il plus susceptible de sortir ?"
- "Si une fréquence est plus élevée, est-ce une preuve ?"

Ne pas corriger tout de suite. Faire émerger les intuitions.

### 0:15-0:35 — Cadre du cours

Présenter la logique du semestre :
- question;
- données;
- nettoyage;
- analyse;
- modèle;
- validation;
- décision.

Phrase clé :
"Vous pouvez utiliser ChatGPT/Codex. Mais vous restez responsables de la question, de la vérification et de la décision."

### 0:35-1:10 — Démo guidée : fréquence

Notebook : `B1_S00_Can_You_Beat_Randomness.ipynb`

Cellules à jouer :
- ouverture;
- chargement dataset;
- préparation colonnes;
- fréquence des numéros;
- fréquence des Lucky Stars.

À faire verbaliser :
- "Quel numéro semble gagner ?"
- "Est-ce que l'écart est énorme ou normal ?"
- "Quelle preuve faudrait-il pour affirmer un vrai biais ?"

Si le dataset manque : passer au plan B Google Trends.

### 1:10-1:25 — Pause active

Mini-défi :
"Écrivez une phrase de décision incorrecte à partir du graphique."

Exemple attendu :
"Le numéro 23 est meilleur, donc il faut le jouer."

Puis correction :
"Non. C'est une histoire séduisante, pas une preuve."

### 1:25-2:00 — Hot numbers, cold numbers, gambler's fallacy

Cellules à jouer :
- most frequent numbers;
- least frequent numbers;
- overdue numbers;
- gambler's fallacy.

Message :
"Un système aléatoire peut produire des classements, des séries et des retards. Ce n'est pas parce que l'histoire existe qu'elle explique quelque chose."

### 2:00-2:45 — Exercice étudiant

Consigne :
"Choisissez une affirmation intuitive sur les tirages. Testez-la avec le notebook. Concluez en trois phrases : observation, interprétation, limite."

Exemples :
- "Les petits nombres sortent-ils plus souvent ?"
- "Les Lucky Stars ont-elles des favoris ?"
- "Les numéros d'anniversaire créent-ils un biais stratégique chez les humains ?"
- "Un numéro en retard est-il vraiment plus intéressant ?"

Livrable :
- une cellule de code;
- un graphique ou tableau;
- une décision refusée ou acceptée;
- une limite.

### 2:45-3:10 — Monte Carlo

Cellules à jouer :
- simulation random;
- comparaison intuition vs hasard;
- rapport de simulation.

Question :
"Est-ce que votre cerveau est confortable avec ce que produit le hasard ?"

Conclusion :
"Le hasard a souvent l'air moins régulier que ce qu'on imagine."

### 3:10-3:25 — Debrief décision

Faire écrire :
"Data Science starts when intuition fails."

Puis relier au reste du cours :
- prochaine séance : mauvaise donnée -> mauvaise décision;
- ensuite : visualisation -> interprétation;
- ensuite : modèles -> confiance;
- fin : produit de décision.

### 3:25-3:30 — Sortie

Question de sortie :
"Donnez un exemple professionnel où une équipe peut confondre bruit et signal."

Réponses possibles :
- baisse ponctuelle de ventes;
- pic Google Trends;
- variation météo;
- avis client isolé;
- métrique produit mal segmentée.

## Plan B Google Trends

Si le dataset EuroMillions n'est pas disponible :
- ouvrir `B1_S00_S01_onboarding_google_trends.ipynb`;
- garder le même message : faux signal vs preuve;
- montrer ChatGPT vs iPhone vs météo;
- demander : "Quel signal justifie une décision produit ?"

Ce plan B est suffisant pour une très bonne séance.

## Ce qu'il ne faut pas faire

- Ne pas dérouler toutes les cellules.
- Ne pas promettre de prédire la loterie.
- Ne pas expliquer pandas trop longtemps.
- Ne pas répondre à tout techniquement si l'intuition n'est pas comprise.
- Ne pas laisser ChatGPT devenir la source de vérité.

## Évaluation légère

Noter surtout :
- qualité de la question;
- honnêteté de l'interprétation;
- capacité à distinguer signal et bruit;
- clarté de la limite;
- code qui tourne.

## Phrase finale

"Le premier réflexe data n'est pas de trouver un modèle. C'est de demander : est-ce que ce que je vois est réel, utile, et suffisant pour décider ?"
