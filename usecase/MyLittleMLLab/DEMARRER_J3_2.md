# J3 — Deuxième atelier

Conception pédagogique : Mathieu Weill.

Télécharger **AML_03_2_atelier.ipynb**, le placer à côté d’AML_03_atelier.ipynb et l’ouvrir avec le même noyau. Aucun git pull nécessaire. Les cellules du premier atelier restent identiques.

Les repères B1 à B5 sont autonomes et utilisent dix paiements fabriqués. B6 à B12 préparent puis réalisent la boucle API Kaggle, au signal du professeur. Les appels sont désactivés par défaut. Installer la CLI selon B6, authentifier son propre compte hors projection, puis autoriser une commande à la fois.

À préparer : compte Kaggle accessible, navigateur, connexion et Python 3.11+. Les règles de compétition et autorisations doivent être traitées par le titulaire du compte. Aucun jeton dans les notebooks ou GitHub. Un refus d’accès ne se corrige pas en partageant les identifiants d’un camarade.

Pour la démonstration ML complète, reprendre le template KAGGLE_AML_03.ipynb du kit J3/J4. La petite sonde de ce deuxième atelier sert uniquement à vérifier le trajet des fichiers.

## Se faire accompagner par GitHub Copilot

Ouvrir le dossier de cours dans VS Code, puis le chat GitHub Copilot. Lui donner accès au guide et au notebook de cet atelier. Copier le prompt suivant :

```text
Aide-moi à configurer l’API Kaggle pour l’atelier AML_03_2_atelier.ipynb.

Commence par lire DEMARRER_J3_2.md et les consignes du notebook. Respecte-les et ne modifie pas le premier atelier AML_03_atelier.ipynb.

Accompagne-moi une étape à la fois :
1. Identifie mon système et l’environnement Python utilisé par Jupyter.
2. Installe Kaggle CLI 2.2.5 et six dans cet environnement, puis vérifie la version.
3. Guide-moi pour m’authentifier personnellement avec Kaggle.
4. Vérifie l’accès à playground-series-s6e11 et liste ses fichiers.
5. Télécharge d’abord sample_submission.csv dans le dossier prévu par l’atelier et vérifie le fichier reçu.
6. Aide-moi à préparer la sonde privée CPU décrite dans le notebook.
7. Avant son envoi, montre-moi les fichiers, la référence du notebook distant et les ressources demandées. Attends mon accord.
8. Guide-moi pour suivre son état, récupérer rapport.json et vérifier son contenu.

Pour chaque étape, explique brièvement son objectif, propose la commande adaptée à mon système et vérifie le résultat avant de continuer. Respecte les points d’arrêt et le signal du professeur : ne lance pas toute la procédure d’un seul coup.

Ne me demande jamais de coller un jeton dans le chat. N’affiche aucun secret et n’enregistre aucun identifiant secret dans le notebook ou GitHub. Je réalise moi-même les étapes de connexion et d’acceptation des règles.

Ne lance aucune soumission au classement, aucun GPU et aucune modification d’un notebook distant existant sans mon accord.

Termine par un bilan : étapes réellement réussies, preuves obtenues, blocages éventuels et prochaine action. N’invente jamais une réussite.
```

Copilot accompagne l’installation ; vous devez pouvoir expliquer ce que chaque commande fait et montrer la preuve qu’elle a fonctionné. Si le guide ou le notebook manque dans votre dossier, le récupérer avant de demander à Copilot de poursuivre. Pour un dépannage, partager le message d’erreur utile sans secret.

## API, REST et FastAPI

Les diapositives 74A et 74B et le rappel B6 du notebook expliquent la distinction. REST décrit un style d’architecture ; FastAPI est un framework Python pour construire une API. Pour cet atelier, nous utilisons la CLI Kaggle : ne pas installer FastAPI pour réaliser B6.
