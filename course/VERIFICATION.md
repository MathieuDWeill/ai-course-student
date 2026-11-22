# Ce qui est vérifié

Le socle comprend 17 notebooks guidés, chacun avec deux démonstrations exécutables, un cours PDF et une présentation. Les notebooks ont été exécutés dans des noyaux neufs sur CPU dans l’environnement de préparation local. Les propriétés importantes sont contrôlées par des assertions ; une version de bibliothèque peut modifier certains scores illustratifs.

Le dépôt possède des contrôles automatiques de navigation, de présence des trois supports, de structure des notebooks et de retrait des notes de présentation professeur. Une exécution automatique du socle sur Linux est configurée avec deux versions de Python. Son dernier résultat est accessible dans [GitHub Actions](https://github.com/MathieuDWeill/ai-course-student/actions/workflows/student-distribution.yml).

Les assertions ne constituent pas une validation universelle du cours ou d’un modèle. Les sept notebooks historiques principaux du premier module Python ont également été exécutés localement dans l’ordre, sans erreur de cellule. Les cellules des ateliers de compétition ne sont pas réexécutées par le contrôle du socle. Il n’est pas affirmé qu’une installation Windows, un GPU, un entraînement Kaggle authentifié ou un déroulé réel de sept heures ait été testé par cette édition.

Les données officielles et poids préentraînés ne sont pas redistribués. La préparation des applications texte et image est distincte de celle des exemples autonomes. Le détail de l’environnement local figure dans [le relevé de vérification](verification.json).

Les exemples résolus font partie du cours. Les réponses des exercices E1/E2, annotations et notes professeur restent privées. Les fichiers de notes sont contrôlés automatiquement ; le sens du contenu visible demande également une relecture éditoriale.
