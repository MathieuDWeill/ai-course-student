# Démarrer J3

## Version à utiliser pour la séance

Télécharger à nouveau **AML_03_atelier.ipynb**, placer le fichier dans notebooks et redémarrer le noyau. Cette version ajoute des étapes guidées : les anciens numéros de cellules ne correspondent plus. Le PowerPoint Classe et le cours rédigé utilisent les nouveaux repères ci-dessous.

[Feuille des exercices accompagnés](EXERCICES_J3.md). Les exercices commencent par un exemple résolu, continuent par une réponse intermédiaire vérifiée, puis une correction collective.

## Si vous avez commencé avec le ZIP J1

1. Fermer le notebook précédent après l’avoir enregistré.
2. Télécharger [AML_03_atelier.ipynb](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/usecase/MyLittleMLLab/notebooks/AML_03_atelier.ipynb). Si le navigateur affiche du JSON, enregistrer le fichier en conservant l’extension `.ipynb`.
3. Placer ce fichier dans **MyLittleMLLab/notebooks**, à côté d’AML_01 et AML_02. Conserver l’environnement, les dossiers mllab, data et runs. Aucun git pull.
4. Aucune installation supplémentaire pour J3.
5. Ouvrir le notebook avec le même environnement Python que J1/J2. Exécuter les cellules dans l’ordre au signal du professeur. Les numéros de cellules comptent aussi les textes.

Le [kit de mise à jour J3/J4](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/kits/MyLittleMLLab_J3_J4_Mise_a_jour.zip) contient les deux notebooks et leurs cours. Copier les notebooks dans notebooks ; copier lectures et templates si vous souhaitez une copie locale des cours et des variantes Kaggle. Le kit ne remplace pas l’installation initiale.

## Reprendre après une erreur

- `mllab` introuvable : vérifier que le notebook est dans notebooks, avec mllab au niveau parent. Ne pas déplacer seulement le notebook dans un autre projet.
- Données absentes : réutiliser les données officielles préparées pour J1/J2 ; ne pas les remplacer par un jeu simulé.
- `torch` absent en J4 : installer avec %pip dans le noyau courant, puis redémarrer le noyau. Une installation dans un autre Python ne suffit pas.
- Redémarrage : relancer les cellules précédentes dans l’ordre. Les variables d’un ancien notebook ne sont pas partagées automatiquement.
- Machine lente : garder le calcul sur CPU et les limites proposées ; ne pas lancer plusieurs recherches en parallèle. Utiliser les sorties projetées pendant un dépannage.

Sur un Mac Intel ou une architecture sans roue PyTorch compatible, utiliser la variante Kaggle CPU.

## Le même atelier sur Kaggle

Importer [KAGGLE_AML_03.ipynb](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/usecase/MyLittleMLLab/templates/KAGGLE_AML_03.ipynb), ajouter les données officielles via Add Input, puis exécuter. Aucun git clone ni fichier de code supplémentaire à transférer. Les données restent soumises aux règles Kaggle. Les quotas et l’ouverture du dépôt se vérifient sur le compte.

Le notebook adapte les chemins, conserve le même budget et écrit les fichiers dans `/kaggle/working/MyLittleMLLab/runs/J3`. Télécharger les résultats pour les comparer au local : mêmes empreintes de données, mêmes folds, versions à noter. La variante Kaggle possède deux cellules de plus que le notebook local : les repères du PowerPoint s’appliquent au notebook local.

## À conserver

Le dossier runs/J3 contient les tableaux, les prédictions et le manifeste. Compléter le journal : hypothèse, preuve, décision, prochaine expérience. Le score public reste inconnu avant un dépôt réel. Le contrôle local déjà vu en J2 est un contrôle de développement, pas un test indépendant supplémentaire.

## Repères du notebook local

- Cellule 3 : Le contrat et le budget.
- Cellule 5 : Lire une règle et calculer Gini.
- Cellule 7 : Profondeur et mémorisation.
- Cellule 9 : Bootstrap et moyenne de forêt.
- Cellule 11 : Construire trois étapes de boosting.
- Cellule 13 : Les familles et les catégories.
- Cellule 15 : Le tournoi initial.
- Cellule 17 : Une expérience de représentation.
- Cellule 19 : Une recherche bornée.
- Cellule 21 : La décision arrêtée avant le contrôle.
- Cellule 23 : L’importance par permutation.
- Cellule 25 : L’audit des sous-groupes.
- Cellule 27 : Le candidat et le CSV Kaggle.
- Cellule 29 : Le journal et la décision.
- Cellule 31 : La vérification finale.

[Glossaire des mots et des calculs du laboratoire](GLOSSAIRE_ML_AVANCE.md).

Le cours projeté utilise la version illustrée. Le notebook renforcé et ses numéros de cellules restent identiques. Les activités sont individuelles et corrigées avec le professeur. [Questions de pop culture](PAUSES_POP_CULTURE.md).
