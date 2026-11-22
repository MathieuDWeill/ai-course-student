# Kit étudiant - Parcours de la donnée à l’IA appliquée

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage selon NOTICE_UTILISATION.md.

Chaque chapitre possède un PDF rédigé, un PowerPoint sans notes professeur, un notebook et une fiche de démarrage. Les exemples résolus sont des éléments de cours ; les réponses aux exercices E1 et E2 restent dans la version professeur.

## Choisir le chapitre

- [PY_01 - Comprendre la question et les tableaux](PY_01/README.md)
- [PY_02 - Fiabiliser les données avec pandas](PY_02/README.md)
- [PY_03 - Explorer et mesurer une association](PY_03/README.md)
- [PY_04 - Construire une référence supervisée](PY_04/README.md)
- [PY_05 - Explorer sans cible et distinguer la recommandation](PY_05/README.md)
- [PY_06 - Rendre une analyse reproductible](PY_06/README.md)
- [PY_07 - Défendre un résultat et une décision](PY_07/README.md)
- [AML_01 - Décrire une expérience de bout en bout](AML_01/README.md)
- [AML_02 - Choisir une validation qui répond à la question](AML_02/README.md)
- [AML_03 - Comprendre arbres, forêts et boosting](AML_03/README.md)
- [AML_04 - Comprendre la boucle d’un réseau](AML_04/README.md)
- [AML_05 - Choisir les expériences et leur budget](AML_05/README.md)
- [AML_06 - Livrer et surveiller un système](AML_06/README.md)
- [NLP_01 - Représenter le texte avec une référence simple](NLP_01/README.md)
- [NLP_02 - Comprendre embeddings, attention et adaptation](NLP_02/README.md)
- [CV_01 - Comprendre pixels, tenseurs et convolution](CV_01/README.md)
- [CV_02 - Évaluer la robustesse et livrer la vision](CV_02/README.md)

## Télécharger les fichiers

Sur GitHub, un notebook s’affiche en lecture : cela ne l’exécute pas. [Télécharger le kit étudiant](../../kits/Parcours_IA_Etudiant.zip?raw=true), extraire le ZIP, puis ouvrir le terminal dans le dossier extrait. Le kit contient les 17 chapitres et leurs supports. Ne pas déplacer seulement un fichier en perdant ses compagnons.

## Installer et ouvrir les exemples autonomes

Python 3.12 recommandé. Ouvrir un terminal dans le dossier contenant requirements.txt. Les commandes ci-dessous créent un environnement séparé ; ne pas les lancer à l’intérieur du ZIP.

Windows PowerShell :

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name parcours-ia-socle --display-name "Parcours IA"
.\.venv\Scripts\python.exe verifier_installation.py
.\.venv\Scripts\python.exe -m jupyter lab
```

macOS/Linux :

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name parcours-ia-socle --display-name "Parcours IA"
.venv/bin/python verifier_installation.py
.venv/bin/python -m jupyter lab
```

Ouvrir le notebook du chapitre. Redémarrer le noyau et exécuter dans l’ordre. Une connexion est nécessaire pour l’installation, pas pour les exemples une fois les dépendances installées. Les calculs n’utilisent ni compte Kaggle, ni clé API, ni GPU.

Les ateliers sur données de compétition restent des applications supplémentaires avec leurs prérequis. Les sorties de ces exemples autonomes ne mesurent pas un résultat Kaggle. Les dépendances installées doivent être compatibles avec la version de Python ; noter leurs versions si une sortie diffère.

Dans Jupyter, sélectionner **Parcours IA** avant d’exécuter. Le vérificateur doit annoncer **PRÊT POUR LES EXEMPLES DU SOCLE**. Si le dossier a été déplacé après installation, recréer l’environnement et enregistrer à nouveau le noyau ; un ancien noyau peut pointer vers un autre Python.
