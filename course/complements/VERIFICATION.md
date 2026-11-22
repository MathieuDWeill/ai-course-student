# Vérifications et limites des compléments

Conception pédagogique : Mathieu Weill.

Les six notebooks ont été exécutés intégralement dans des noyaux neufs sur macOS, Python 3.12, CPU. Douze cellules de code passent leurs assertions. Les modèles préentraînés font l’objet de commandes distinctes, explicitement signalées dans les notebooks.

- API : tests du contrat, refus d’entrées invalides et rechargement des probabilités vérifiés ; serveur Uvicorn local appelé réellement via HTTP.
- CNN : convolution fixée et entraînement de deux epochs sur digits exécutés. Le score du cours décrit cette partition intégrée, pas les données Kaggle.
- Génération : DistilGPT2 exécuté avec une révision identifiée. L’essai de résumé échoue ; cet échec est conservé et expliqué, sans sortie de remplacement inventée.
- Vision : SSDLite et LRASPP exécutés sur une image de contrôle. Les sorties ne sont pas des annotations ; aucune mAP ni IoU réelle n’est annoncée sans référence indépendante.
- Fusion : recherche combinée exécutée avec labels prédits et requête texte. Le petit catalogue et les cas de comparaison du notebook sont fabriqués pour expliquer le raisonnement.
- Supports : versions étudiantes sans parties PowerPoint de notes/commentaires ; notebooks sans sorties enregistrées ni corrections d’exercices. Les exemples résolus restent dans le cours.

L’environnement de chaque PC/Mac, la construction Docker, l’hébergement distant et une exécution authentifiée Kaggle demandent des vérifications distinctes. Les poids ne sont pas inclus dans le ZIP. Les installations nécessitent Internet ; les poids sont téléchargés à la demande. Préparer ces téléchargements avant de lancer une démonstration en classe.

Les calculs déterministes ont des assertions ; les temps et certains résultats d’entraînement peuvent varier selon versions et matériel. Une présence de supports ne certifie pas une compétence acquise : les questions de vérification et le bilan individuel font partie de la séance.
