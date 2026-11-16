# Sources et séparation des faits

Consultées le 6 novembre 2026. Les descriptions de compétitions sont résumées, pas reproduites intégralement. Les scores locaux sont ceux des fichiers de validation ; aucun score de leaderboard n'est inventé.

## Compétitions

- Kaggle, [Predicting Credit Card Fraud](https://www.kaggle.com/competitions/playground-series-s6e11/overview) : cible, ROC-AUC, format, calendrier et récompenses.
- Kaggle, [Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started) : F1 binaire, format des classes, statut Getting Started et classement roulant.
- Kaggle, [Dogs vs. Cats Redux](https://www.kaggle.com/competitions/dogs-vs-cats-redux-kernels-edition) : tâche, log-loss et caractère historique.
- Kaggle, [Notebooks](https://www.kaggle.com/docs/notebooks), [conditions](https://www.kaggle.com/terms) et [CLI](https://github.com/Kaggle/kaggle-cli/blob/main/docs/competitions.md) : à vérifier avant l'usage effectif du service. Les quotas ne sont pas fixés dans le cours.

## Méthodes et logiciels

- scikit-learn, [pièges et fuites](https://scikit-learn.org/stable/common_pitfalls), [validation croisée](https://scikit-learn.org/stable/modules/cross_validation.html), [pipelines](https://scikit-learn.org/stable/modules/compose.html).
- PyTorch, [bases](https://docs.pytorch.org/tutorials/beginner/basics/intro.html), [optimisation](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html), [transfert](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html).
- Hugging Face, [fine-tuning](https://huggingface.co/docs/transformers/training) : la page actuelle présente notamment un modèle causal ; notre TP de classification binaire adapte explicitement un encodeur BERT, pas une copie de ce tutoriel.
- [BERT-tiny](https://huggingface.co/prajjwal1/bert-tiny) : poids anglophones pour les expériences courtes, pas recommandation de meilleur modèle.
- [ResNet18](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet18.html) : poids ImageNet et prétraitement associé.

## Points à ne pas surinterpréter

Données officielles de concours ne signifie pas données non synthétiques (Playground). Validation stratifiée ne signifie pas validation temporelle ou par personne. Un run court de transfert ne garantit pas de gain. Le leaderboard public n'est pas une validation locale. Les fichiers sources officiels des UE doivent encore confirmer le mapping du cours.
