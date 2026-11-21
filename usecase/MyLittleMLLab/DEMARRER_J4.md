# Démarrer J4

## Version à utiliser pour la séance

Télécharger à nouveau **AML_04_atelier.ipynb**, placer le fichier dans notebooks et redémarrer le noyau. Cette version ajoute des étapes guidées : les anciens numéros de cellules ne correspondent plus. Le PowerPoint Classe et le cours rédigé utilisent les nouveaux repères ci-dessous.

[Feuille des exercices accompagnés](EXERCICES_J4.md). Les exercices commencent par un exemple résolu, continuent par une réponse intermédiaire vérifiée, puis une correction collective.

## Si vous avez commencé avec le ZIP J1

1. Fermer le notebook précédent après l’avoir enregistré.
2. Télécharger [AML_04_atelier.ipynb](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/usecase/MyLittleMLLab/notebooks/AML_04_atelier.ipynb). Si le navigateur affiche du JSON, enregistrer le fichier en conservant l’extension `.ipynb`.
3. Placer ce fichier dans **MyLittleMLLab/notebooks**, à côté d’AML_01 et AML_02. Conserver l’environnement, les dossiers mllab, data et runs. Aucun git pull.
4. Dans une cellule temporaire de Jupyter : `%pip install "torch>=2.4,<3"`. Attendre la fin, puis Kernel → Restart Kernel. Cette étape nécessite une connexion et peut prendre plusieurs minutes ; la faire avant la séance. PyTorch utilise le CPU dans cet atelier.
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

Importer [KAGGLE_AML_04.ipynb](https://github.com/MathieuDWeill/ai-course-student/raw/refs/heads/main/usecase/MyLittleMLLab/templates/KAGGLE_AML_04.ipynb), ajouter les données officielles via Add Input, puis exécuter. Aucun git clone ni fichier de code supplémentaire à transférer. Les données restent soumises aux règles Kaggle. Les quotas et l’ouverture du dépôt se vérifient sur le compte.

Le notebook adapte les chemins, conserve le même budget et écrit les fichiers dans `/kaggle/working/MyLittleMLLab/runs/J4`. Télécharger les résultats pour les comparer au local : mêmes empreintes de données, mêmes folds, versions à noter. La variante Kaggle possède deux cellules de plus que le notebook local : les repères du PowerPoint s’appliquent au notebook local.

## À conserver

Le dossier runs/J4 contient les tableaux, les prédictions et le manifeste. Compléter le journal : hypothèse, preuve, décision, prochaine expérience. Le score public reste inconnu avant un dépôt réel. Le contrôle local déjà vu en J2 est un contrôle de développement, pas un test indépendant supplémentaire.

## Repères du notebook local

- Cellule 3 : Le contrat et les ressources.
- Cellule 5 : Un poids et deux tailles de pas.
- Cellule 7 : Les rôles de backward et step.
- Cellule 9 : Un batch visible, une couche visible.
- Cellule 11 : Logits, softmax et cross-entropy.
- Cellule 13 : Les gradients de chaque poids.
- Cellule 15 : Pourquoi ajouter une non-linéarité.
- Cellule 17 : Les transformations numériques.
- Cellule 19 : Les dimensions et la référence constante.
- Cellule 21 : La boucle tabulaire complète.
- Cellule 23 : Les courbes sur un fold.
- Cellule 25 : train, eval et no_grad.
- Cellule 27 : Deux learning rates, trois folds.
- Cellule 29 : Un early stopping explicite.
- Cellule 31 : Le contrôle après le choix.
- Cellule 33 : Exporter un candidat complet.
- Cellule 35 : Vérifier le retour des artefacts.
- Cellule 37 : Le journal et la décision.

[Glossaire des mots et des calculs du laboratoire](GLOSSAIRE_ML_AVANCE.md).

Le cours projeté utilise la version Atelier Vivant. Le notebook renforcé et ses numéros de cellules restent identiques. Les activités sont individuelles et corrigées avec le professeur. [Questions de pop culture](PAUSES_POP_CULTURE.md).

Préparer le [carnet de défis](CARNET_DEFIS.md). Les réponses individuelles se placent sur le carnet, dans un fichier à part ou à la fin du notebook pour conserver les repères de cellules. Les résultats se révèlent après les prédictions.
