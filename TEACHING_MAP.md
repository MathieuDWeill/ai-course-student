# Teaching Map

Progression pedagogique: Data Science -> ML Engineering -> Applied AI.

## Audit rapide

Sources officielles preservees:
- `S4-B2-Python-Data-Science.docx`: bases Python data science, pandas, EDA, visualisation, premiers modeles ML.
- `S3-EXP-IA-MLOps-Final.docx`: ML avance, deep learning, optimisation, regularisation, deploiement, MLOps.
- `S4-EXP-IA-NLP-Vision-Final.docx`: NLP, transformers, computer vision, applications intelligentes, analyse ethique.

Actifs repo reutilisables:
- notebooks Bloc 1 existants autour de Google Trends et signaux faibles;
- snapshots CSV versionnes dans `data/snapshots/`;
- templates Kaggle compatibles local/Kaggle;
- scripts `setup.sh`, `check.sh`, `run.sh`.

Manques combles ici:
- progression commune entre les 3 modules;
- framework projet partage;
- bridge explicite cours -> Kaggle -> portfolio.

Incoherences a surveiller:
- les notebooks actuels couvrent surtout le module Data Science;
- les modules MLOps et NLP/Vision doivent etre ajoutes progressivement sans casser le socle.

## Module 1 - Python for Data Science

Objectif: rendre les etudiants autonomes sur l'analyse de donnees avec Python.

Ce que les etudiants apprennent:
- charger, nettoyer et transformer un dataset;
- produire une EDA utile;
- construire une baseline ML simple;
- expliquer limites, biais et decisions possibles.

Connexion au module suivant:
- un notebook propre devient un pipeline;
- une baseline devient un modele a evaluer, versionner et deployer;
- les limites identifiees deviennent des exigences MLOps.

Logique projet:
- partir de signaux faibles publics;
- produire un dataset propre;
- raconter une decision avec preuves et limites.

## Module 2 - Advanced ML + MLOps

Objectif: passer d'une analyse reproductible a un systeme ML exploitable.

Ce que les etudiants apprennent:
- entrainer et comparer des modeles plus complexes;
- utiliser reseaux de neurones et regularisation;
- evaluer robustesse, erreurs et generalisation;
- documenter, packager et deployer un modele.

Connexion au module suivant:
- un modele deploye devient une brique applicative;
- les APIs, artefacts et tests servent aux applications NLP/Vision;
- la supervision MLOps prepare l'evaluation d'applications IA.

Logique projet:
- transformer la baseline en pipeline ML;
- exposer une prediction ou recommandation;
- livrer documentation technique + demo.

## Module 3 - NLP + Vision

Objectif: construire des applications IA a partir de texte, image ou signaux multimodaux.

Ce que les etudiants apprennent:
- utiliser embeddings, transformers et modeles pre-entraines;
- construire une application NLP ou vision;
- combiner prediction, interface et evaluation;
- integrer limites techniques, donnees et ethique.

Connexion finale:
- l'etudiant livre une application intelligente comprehensible;
- le projet devient un portfolio public: notebook, dataset, demo, rapport court.

Logique projet:
- partir d'un besoin utilisateur;
- choisir texte, image ou multimodal;
- livrer une application utile, testable et responsable.

## Progression commune

1. Signal: identifier une source publique et une question utile.
2. Dataset: nettoyer, documenter, versionner.
3. Insight: explorer et formuler une decision.
4. Model: construire une baseline puis l'ameliorer.
5. System: deployer, monitorer, documenter.
6. Application: integrer NLP/Vision et evaluer l'usage reel.
