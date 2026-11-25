# J5 — Choisir une expérience utile

Conception pédagogique : Mathieu Weill.

Repères D1 à D12 communs au notebook, à la projection et au guide.

## 2. Le parcours de la journée

7 heures pédagogiques ; pauses à ajouter selon l’emploi du temps.

La journée alterne des démonstrations courtes et des manipulations guidées. Nous ne lançons pas douze expériences au hasard. Chaque bloc laisse une trace : une hypothèse, un budget, des prédictions ou une décision. Chacun garde son notebook. Pour les vérifications, nous travaillons par trinômes : opérateur, vérificateur et rapporteur, puis les rôles changent. Être rapporteur demande de comprendre le résultat, pas seulement de lire le code.

Question à expliquer : Quelle trace annonce notre intention avant le calcul ?

## 3. De Python au choix d’expérience

Données fiables → validation → modèles → apprentissage → décision d’essai

Dans Python pour la data science, nous avons appris à décrire une ligne et à contrôler les colonnes. J1 et J2 ont ajouté un protocole et une séparation crédible. J3 a comparé plusieurs modèles. J4 a ouvert le calcul du réseau. J5 ne remplace rien : il utilise ces preuves pour décider quoi essayer ensuite. Sans données fiables, une optimisation perfectionnée ne nous sauve pas. Sans séparation, un gain peut simplement être une fuite.

Question à expliquer : Quelle règle de J2 gardons-nous ?

## 4. Rappel : paramètres et hyperparamètres

Poids appris pendant le fit ; réglages choisis avant le fit.

Un coefficient logistique est appris à partir des données. C est un réglage choisi avant l’entraînement. Modifier C puis réentraîner constitue donc une nouvelle expérience. Les folds sont les parties utilisées pour comparer ces expériences. Ce sont trois objets distincts : ce que le modèle apprend, ce que nous décidons de tester et la façon de mesurer. La seed rend une partie des choix aléatoires reproductible ; elle ne garantit pas la qualité.

Question à expliquer : C est-il appris automatiquement pendant ce fit ?

## 5. Une proposition testable

« Essayons plus gros » ou « Changeons un réglage, mêmes folds » ?

Je vous donne deux propositions. La première demande un modèle plus gros, sans dire ce que signifie mieux. La seconde conserve les mêmes lignes et les mêmes folds, et teste un autre niveau de régularisation avec l’AUC comme critère. La seconde permet de préparer un calcul et une conclusion, y compris négative. Une hypothèse n’a pas besoin d’être compliquée. Elle doit permettre de distinguer ce qui a été essayé de ce qui a été observé.

Question à expliquer : Quelle proposition peut-on vérifier sans changer les règles ensuite ?

## 6. L’hypothèse et son risque d’échec — D2

Observation → modification → effet attendu → critère d’arrêt

Notre référence est déjà compétitive. Nous testons si un frein différent sur les coefficients améliore le classement. Il est possible que le frein actuel soit déjà adapté. Dans ce cas, l’expérience échoue à améliorer le score, mais elle a réduit une incertitude. Il faut écrire cette conclusion au lieu de multiplier les variantes jusqu’à trouver quelque chose de positif. Le budget nous empêche aussi de transformer une intuition en recherche infinie.

Question à expliquer : Si la variante perd, avons-nous forcément travaillé pour rien ?

## 7. La question Kaggle de J5 — D1

Classer les fraudes avec les mêmes données et la même ROC-AUC.

Nous restons sur la compétition de détection de fraude. L’AUC officielle évalue le classement des scores, sans fixer un seuil d’alerte. Aujourd’hui, nous optimisons une comparaison locale ; nous ne promettons aucun score public. Le contrôle local déjà consulté ne redevient pas neuf parce que nous changeons de notebook. Nous ne l’utilisons pas pour choisir les candidats dans J5. Nous utiliserons seulement la validation croisée prévue.

Question à expliquer : Peut-on appeler le contrôle déjà consulté un test final indépendant ?

## 8. Ouvrir le bon atelier — D1

GitHub étudiant → AML_05 → kit J5 → notebooks/AML_05_atelier.ipynb

Téléchargez le kit J5 et ouvrez le notebook nommé AML zéro cinq atelier. Il contient les repères D1 à D12. Ces mêmes repères figurent ici et dans le PDF. Le kit conserve le laboratoire, ajoute les fonctions nécessaires et ne contient pas les données officielles. Si vous partez du ZIP, aucun git pull n’est nécessaire. Extrayez le kit dans un nouveau dossier et suivez le guide pour retrouver les trois CSV. Nous exécutons D1 ensemble avant de continuer.

https://github.com/MathieuDWeill/ai-course-student/blob/main/course/seances/AML_05.md

Question à expliquer : Quel repère ouvrez-vous maintenant ?

## 9. D1 · Vérifier le terrain de comparaison — D1

15 000 lignes train, trois folds, seed 2026 et CPU dans le profil de classe.

Nous lisons les sorties du contrat. La quantité de lignes est une limite de calcul, pas la totalité du dataset. L’empreinte des identifiants est une sorte de résumé vérifiable de la liste utilisée. Si deux expériences n’ont pas les mêmes identifiants, elles ne mesurent pas exactement la même chose. Une empreinte identique ne suffit pas à tout prouver : les valeurs des fichiers et les paramètres comptent aussi. Prenons le temps de nommer ce qui est fixé.

Question à expliquer : La limite de lignes est-elle une métrique de qualité ?

## 10. Un fit, une époque, une prédiction — D2

Trois coûts différents à ne pas additionner sans les nommer.

Un fit est un appel qui entraîne un modèle. Une époque est un passage sur les données dans certaines boucles d’apprentissage, comme celle du réseau. Une prédiction utilise des paramètres déjà appris. Dans notre budget J5, nous comptons les fits de validation croisée. Les 80 étapes internes du boosting ne deviennent pas 80 candidats. Et la moyenne de deux colonnes de scores ne déclenche aucun nouvel entraînement. Cette distinction évite de sous-estimer ou de multiplier artificiellement le budget.

Question à expliquer : Quatre candidats sur trois folds représentent combien de fits ?

## 11. Un budget qui semble petit peut durer longtemps — D2

Exemple fictif : 12 configurations × 3 folds × 2 seeds.

Calculons avant d’utiliser une machine. Douze configurations multipliées par trois folds puis deux seeds donnent soixante-douze entraînements. Avec quatre minutes par entraînement, cela fait deux cent quatre-vingt-huit minutes, soit quatre heures quarante-huit. C’est un budget séquentiel fictif, qui ne comprend ni les téléchargements ni les erreurs de manipulation. Paralléliser peut réduire le temps écoulé, mais ne supprime pas le travail et peut demander davantage de mémoire.

Question à expliquer : Le chiffre 288 comprend-il tout le travail de la journée ?

## 12. Le budget réel de l’atelier — D2

2 fits techniques + 12 fits CV = 14 fits en J5.

Nous limitons volontairement la recherche. Deux petits entraînements vérifient d’abord que le chemin technique fonctionne. Ensuite, quatre candidats passent sur trois folds identiques. Nous n’ajoutons pas de recherche de poids pour la moyenne. J6 entraînera uniquement le candidat retenu sur le train de développement : un fit pour un modèle seul, deux pour la combinaison prévue. Écrire ces coûts maintenant permet de comparer le programme au travail réellement effectué.

Question à expliquer : Les deux petits fits techniques remplacent-ils la CV ?

## 13. D2 · Écrire avant le calcul — D2

Observation, hypothèse, conditions fixes et arrêt sont enregistrés dans un JSON.

Un fichier JSON conserve un petit dictionnaire sous une forme lisible par d’autres programmes. Ici, il n’enregistre aucun secret. Il contient ce que nous voulons vérifier et les conditions de l’essai. Nous ne l’écrivons pas seulement après avoir vu le gagnant. Sinon, nous risquons de raconter que nous avions prévu une amélioration alors que nous avons exploré beaucoup de variantes. Le fichier plan avant calcul joue le rôle d’un engagement de méthode.

Question à expliquer : Pourquoi l’enregistrer avant le tournoi ?

## 14. D3 · Tester le chemin sur 600 lignes — D3

Deux modèles ; 100 probabilités à vérifier ; aucun classement de qualité.

Le petit test technique répond à une question simple : le code peut-il apprendre puis produire cent scores finis ? Nous ne prenons pas son score pour décider du meilleur modèle. Les premières lignes ne constituent pas une nouvelle expérience de validation fiable. Ce petit passage sert à détecter une colonne incorrecte, un objet manquant ou une forme inattendue. Une fois le contrat vérifié, nous passons au protocole prévu, sans chercher un résultat flatteur sur ce jouet technique.

Question à expliquer : Pourquoi ne pas choisir le modèle à cette étape ?

## 15. Petit test réussi : ce que cela prouve — D3

Deux fits terminés, deux sorties de 100 valeurs ; la généralisation reste à mesurer.

Un programme peut terminer sans fournir un modèle utile. Le succès technique signifie que les entrées et les calculs sont cohérents pour cet essai. Il ne mesure pas la capacité à traiter de nouveaux cas. Nous gardons donc deux formulations distinctes : le calcul fonctionne et le modèle améliore l’AUC. La première peut être vraie alors que la seconde est fausse. Aujourd’hui, vous devez pouvoir dire laquelle vous avez vérifiée.

Question à expliquer : Quel mot manque à « mon modèle marche » ?

## 16. Une prédiction hors fold — D4

La ligne est prédite par un modèle qui ne l’a pas apprise.

Imaginons trois paquets A, B et C. Pour prédire A, nous apprenons sur B et C. Pour prédire B, nous apprenons sur A et C. Pour prédire C, nous apprenons sur A et B. À la fin, chaque ligne a exactement un score obtenu sans être dans le train du modèle correspondant. Le prétraitement est inclus dans ce train. Nous appelons cette collection OOF, ou hors fold. Ce n’est pas un nouveau test final : nous allons l’utiliser pour développer et sélectionner.

Question à expliquer : Pour prédire A, le prétraitement peut-il être appris sur A ?

## 17. Vérifier la couverture OOF — D4

Chaque ligne reçoit exactement un score de validation.

Le tableau des folds doit couvrir tout le train de développement une seule fois en validation. Si une ligne ne reçoit aucun score, notre colonne OOF est incomplète. Si elle reçoit plusieurs scores écrasés sans le dire, nous ne savons plus ce qu’elle représente. Le notebook compte les passages et vérifie que les identifiants d’entraînement et de validation ne se croisent pas dans un même fold. Ce sont des contrôles de protocole concrets.

Question à expliquer : Quelle valeur doit avoir le compteur de validation pour chaque ligne ?

## 18. D4 · Lire les tailles des folds — D4

Le compteur vaut 1 partout ; les trois validations contiennent les deux classes.

Nous lançons D4 et lisons les tailles. À quinze mille lignes, les trois validations ont cinq mille observations chacune et les trains de fold dix mille. La stratification essaie de conserver la proportion des classes ; elle ne crée pas de nouvelles fraudes et ne remplace pas une séparation chronologique si l’usage l’exige. Nous travaillons ici dans le protocole pédagogique annoncé. Lire les effectifs évite de comparer des AUC calculées sur des parties incompatibles.

Question à expliquer : La stratification prouve-t-elle que le split est adapté au futur ?

## 19. Quatre candidats, des questions séparées — D5

Trois niveaux de régularisation et le boosting déjà connu.

Nous n’essayons pas simultanément une nouvelle architecture, un nouveau split et une nouvelle métrique. Les trois régressions logistiques ne diffèrent que par C. Le boosting répond à une autre comparaison, déjà introduite en J3, avec ses paramètres fixés. Ce tableau ne permet pas d’attribuer tout écart entre boosting et logistique à un seul hyperparamètre : ce sont deux familles différentes. Il permet en revanche une comparaison contrôlée entre les trois valeurs de C.

Question à expliquer : Quelle comparaison isole ici le changement de C ?

## 20. C : un réglage du frein — D5

Pour cette logistique : C petit → régularisation plus forte.

Le frein est une analogie : la régularisation limite la liberté des coefficients. Un frein plus fort peut réduire l’adaptation excessive, mais il peut aussi empêcher d’apprendre un signal utile. Un frein plus faible peut aider ou nuire. Nous n’allons donc pas décréter que petit C est toujours préférable. Nous testons trois valeurs sous le même protocole. Ces valeurs ne sont pas des pourcentages de données et ne désignent pas le nombre de neurones.

Question à expliquer : C=0,01 impose-t-il plus ou moins de régularisation que C=0,1 ?

## 21. D5 · Lancer une seule fois le tournoi — D5

12 fits CV ; pipeline appris séparément dans chaque fold.

Nous avons maintenant assez de contrôles pour lancer. Ne modifiez pas les candidats pendant le calcul. Le code crée une nouvelle copie du pipeline pour chaque fold, apprend seulement sur son train puis écrit les scores de validation à leur place. Une copie indépendante évite de conserver des paramètres appris sur une autre partie. Si le calcul échoue, notez le candidat et le message. Relancer sans lire l’erreur n’est pas une stratégie d’optimisation.

```text
oof, scores, fold_models = tournament(ctx, RUN)
assert len(scores) == 12
display(summary(scores))
```

Question à expliquer : Pourquoi recréer le modèle pour chaque fold ?

## 22. Le résultat local du tournoi — D5

Valeurs de la vérification CPU, profil 15 000 lignes ; vos durées peuvent varier.

Nous lisons d’abord les noms et l’axe. La référence reste devant dans cette exécution. La régularisation plus faible est proche, la plus forte est moins bonne et le boosting est derrière. Ce résultat ne rend pas le boosting mauvais partout. Il répond à notre problème, notre représentation et notre budget. Nous conservons la précision des chiffres dans le tableau, mais nous n’inventons pas de certitude à partir d’un petit écart moyen.

Question à expliquer : Quel candidat apporte ici le meilleur classement moyen ?

## 23. D6 · Ouvrir la moyenne — D6

Trois folds → trois comparaisons, pas une promesse.

Une moyenne résume plusieurs résultats. Elle peut cacher un gain présent seulement dans un fold ou une perte régulière. Nous regardons donc les trois scores, avec les mêmes lignes pour chaque candidat. Un écart positif signifie meilleur que la référence dans ce fold ; un écart négatif signifie moins bon. Nous ne prenons pas la dispersion de trois nombres pour un intervalle de confiance. C’est un outil de lecture, pas une preuve statistique complète.

Question à expliquer : Que signifie un écart de −0,01 à la référence ?

## 24. Comparer une différence à la fois — D6

D6 affiche aussi les écarts à la référence pour chaque fold.

Prenez un candidat et suivez sa ligne dans les trois folds. N’additionnez pas directement des pourcentages d’erreurs et des points d’AUC : ce ne sont pas les mêmes quantités. Demandez-vous si le changement va dans le même sens et s’il vaut la complexité ajoutée. La décision peut aussi dépendre d’une contrainte de temps, mais nous devons la mesurer et annoncer la règle. Nous ne changeons pas la règle après lecture pour favoriser un candidat.

Question à expliquer : Un écart moyen minuscule suffit-il à justifier une livraison plus complexe ?

## 25. Premier verdict : aucune victoire obligatoire — D6

Une expérience peut éliminer une piste sans produire un meilleur modèle.

Nous devons accepter un résultat défavorable à notre intuition. Une explication honnête dit : voici le réglage testé, voici le protocole, voici les trois observations et voici la limite. Une mauvaise explication transforme une perte en succès sans preuve, ou relance dix variantes en cachant les neuf premières. Nous gardons les résultats négatifs dans le journal pour éviter de refaire la même recherche. La compétence consiste aussi à savoir s’arrêter.

Question à expliquer : Que doit conserver le journal d’une variante qui perd ?

## 26. Deux modèles peuvent se tromper différemment — D7

Exemple fictif : observer les erreurs avant de calculer une moyenne.

Nous revenons à quatre lignes seulement. Les deux premières sont normales, les deux dernières frauduleuses. A alerte à tort sur la deuxième ligne ; B sur la première. Ils font donc le même nombre d’erreurs, mais pas sur les mêmes exemples. C’est une raison d’examiner une combinaison, pas une garantie. Si les deux modèles se trompaient de la même façon avec les mêmes scores, une moyenne n’apporterait rien.

Question à expliquer : Le nombre d’erreurs suffit-il à mesurer leur complémentarité ?

## 27. D7 · Moyenne 50/50 sur quatre lignes — D7

Même poids pour A et B ; le seuil reste une décision distincte.

Pour la première ligne, zéro virgule un plus zéro virgule sept, divisé par deux, donne zéro virgule quatre. Pour la deuxième, nous obtenons zéro virgule quarante-cinq. Les deux scores sont sous le seuil de moitié, donc les fausses alertes disparaissent dans ce jouet. Ce n’est pas une loi générale. La moyenne peut aussi déplacer un score correct du mauvais côté du seuil. Nous testons un mécanisme visible avant de revenir aux données officielles.

Question à expliquer : La moyenne du deuxième exemple vaut-elle 0,9 ?

## 28. Ce que le jouet prouve et ne prouve pas — D7

Au seuil 0,5 : A fait 1 erreur, B fait 1 erreur, la moyenne 0 dans ce jouet.

Le résultat peut sembler spectaculaire sur quatre lignes. C’est précisément pour cela qu’il faut préciser le contexte. Nous avons construit ces valeurs pour montrer un mécanisme. Elles ne démontrent pas qu’une moyenne gagnera sur des milliers de paiements ni sur la compétition. La bonne transition consiste à garder l’idée, à fixer les poids avant la mesure et à appliquer le même protocole aux vraies données. L’illustration explique ; la validation compare.

Question à expliquer : Pourquoi ne pas annoncer déjà que l’ensemble est meilleur ?

## 29. Réutiliser les OOF sans tricher — D8

Combiner les scores de lignes non apprises ; garder les poids 50/50 fixés.

Pour une ligne donnée, nous combinons la prédiction OOF de la référence et celle du boosting. Chacune vient d’un modèle entraîné sans cette ligne. Nous n’entraînons pas ici un modèle supplémentaire qui apprendrait des poids. Si nous essayions beaucoup de poids pour retenir celui qui gagne, nous utiliserions cette même validation pour sélectionner davantage de variantes. Le risque de suradaptation au développement augmenterait. Le budget de recherche doit donc compter aussi les décisions prises.

Question à expliquer : Pourquoi ne pas tester cent poids gratuitement ?

## 30. D8 · Le vrai résultat de la combinaison — D8

La moyenne 50/50 est un cinquième candidat ; elle n’ajoute aucun fit.

Nous retrouvons les vraies observations de compétition. La moyenne ne dépasse pas la référence dans cette vérification. Le contraste avec le jouet est utile : il montre qu’un mécanisme plausible n’est pas une promesse de gain. Nous pouvons abandonner cet ensemble précis sans conclure que tous les ensembles sont inutiles. Les poids, les représentations et les données changeraient la question ; ils demanderaient un autre plan d’expérience.

Question à expliquer : L’absence de gain signifie-t-elle que le code est faux ?

## 31. OOF regroupées et moyenne des folds — D8

Deux calculs descriptifs ; notre règle de sélection utilise la moyenne des folds.

L’AUC d’une grande colonne OOF compare des scores provenant de plusieurs modèles de fold. La moyenne des trois AUC calcule d’abord un résultat dans chaque fold, puis les résume. Ces deux nombres ne sont pas obligés d’être identiques. Nous avons fixé la seconde règle pour sélectionner les candidats. Ne remplaçons pas la métrique annoncée par le nombre le plus flatteur après lecture. Ce point est une question de protocole, pas une querelle de vocabulaire.

Question à expliquer : Quel nombre doit décider dans cet atelier ?

## 32. L’AUC et les erreurs au seuil répondent à deux questions — D8

La table d’erreurs de D8 utilise 0,5 ; elle n’est pas la règle de sélection.

Le tableau croisé indique si deux modèles se trompent sur les mêmes lignes au seuil de moitié. Ce tableau peut être utile pour comprendre des comportements, mais notre objectif officiel reste le classement ROC-AUC. Deux scores peuvent franchir un seuil différemment tout en conservant le même classement. Nous gardons donc la finalité de chaque sortie : l’AUC pour la comparaison annoncée, les erreurs au seuil pour un diagnostic complémentaire.

Question à expliquer : Peut-on remplacer l’AUC par ce tableau sans l’annoncer ?

## 33. Le prix d’un ensemble se paie après la sélection — D9

Zéro fit pour la moyenne de scores ; deux modèles à réentraîner et à utiliser.

Dans le notebook, nous avons déjà les colonnes OOF. Les moyenner est peu coûteux. Mais pour servir de nouvelles lignes, nous devons disposer des deux modèles entraînés et calculer leurs deux sorties. Il faut donc regarder le coût futur et pas seulement la facilité du calcul de la moyenne aujourd’hui. Un gain minuscule peut ne pas justifier ce coût. Cette décision doit rester liée à l’usage, avec une règle annoncée.

Question à expliquer : Combien de modèles faut-il garder pour cette moyenne ?

## 34. D9 · Mesurer le temps d’inférence — D9

1 000 lignes, un passage de préparation, cinq répétitions ; médiane locale.

Nous chronométrons une opération précise sur cette machine. Un passage préalable limite l’effet du premier appel, puis nous prenons cinq mesures et leur médiane. La médiane est la valeur au milieu des mesures triées. Elle réduit l’influence d’un passage exceptionnellement lent, sans supprimer toutes les variations. Ce temps inclut ici le prétraitement et les prédictions des pipelines utilisés. Il ne mesure ni le réseau Internet ni une API distante.

Question à expliquer : Peut-on comparer cette durée à celle d’un autre PC sans contexte ?

## 35. La mémoire : nommer ce qui est mesuré — D9

nbytes mesure le tableau de valeurs ; pas la RAM totale ni la mémoire GPU.

Un tableau de quinze mille probabilités stockées sur huit octets utilise cent vingt mille octets pour ses valeurs. Cela n’inclut pas tout le programme, les objets Python, les modèles ni les données d’entrée. Si nous n’avons pas mesuré la mémoire totale, nous écrivons non mesurée. Le même principe vaut pour un GPU que nous n’utilisons pas. Une petite valeur n’est utile que si son périmètre est clair.

Question à expliquer : 120 000 octets représentent-ils toute la mémoire du laboratoire ?

## 36. Un gain peut être trop cher pour l’usage

Exemple fictif : AUC +0,0002, inférence ×10.

Il manque une information avant de dire oui ou non : l’usage. Un calcul de nuit tolère parfois une durée supérieure. Une prédiction interactive peut avoir une limite stricte. Il faut aussi examiner la stabilité du gain et les moyens de retour arrière. Nous ne décidons pas uniquement avec une colonne de score. Dans l’atelier, la règle de classement est fixée pour être reproductible ; cette discussion prépare une règle de livraison plus complète.

Question à expliquer : Quelle question poser avant d’accepter la variante ?

## 37. D10 · Figer le choix — D10

Le nom, les membres, les poids, le protocole et les limites vont dans decision.json.

Figer ne veut pas dire que le modèle sera bon pour toujours. Cela signifie que nous arrêtons les choix pour cette version et que nous enregistrons ce qui a été décidé. La prochaine étape ne relancera pas une recherche cachée. Le fichier indique aussi si J6 doit entraîner un ou deux modèles. Nous allons garder la règle de départage pour qu’un autre puisse retrouver le choix à partir des mêmes scores.

Question à expliquer : Le fichier decision.json contient-il déjà le modèle entraîné de livraison ?

## 38. Choisir sur la CV change le statut de la CV — D10

Le meilleur score observé sert à choisir ; il ne devient pas un test final neuf.

Nous avons regardé plusieurs candidats sur les mêmes folds. Le candidat retenu a été choisi en partie parce qu’il y réussit bien. Réutiliser ces mêmes résultats comme une estimation parfaitement indépendante serait trop optimiste. La bonne formulation parle d’un résultat de développement. Une évaluation finale distincte se prépare avant la sélection et selon l’usage. Dans ce cours, nous n’inventons pas un nouveau jeu vierge après avoir déjà consulté le contrôle.

Question à expliquer : La validation croisée devient-elle indépendante parce qu’elle a trois folds ?

## 39. D11 · Reproduire sur Kaggle — D11

Même code, mêmes entrées, mêmes folds, mêmes réglages ; calcul CPU déclaré.

Le template Kaggle de J5 embarque les fonctions du laboratoire et adapte les chemins. Il attend les données officielles ajoutées par le titulaire du compte. Nous ne copions pas de token dans le notebook. Avant de comparer un score, nous comparons les empreintes, la limite de données, les versions et les paramètres. Un changement de temps peut venir du matériel ; un changement de qualité demande un examen plus complet. Le template n’effectue aucune soumission automatique.

Question à expliquer : Le matériel distant garantit-il un meilleur score ?

## 40. Le transfert, une étape à constater — D11

Importer templates/KAGGLE_AML_05.ipynb, ajouter les données, exécuter puis récupérer les sorties.

Nous procédons avec le même chemin guidé qu’au début de J4. Créez un notebook Kaggle, importez le fichier de la séance puis ajoutez la compétition dans les entrées autorisées. Vérifiez CPU et accès privé. Exécutez et attendez un état terminé avant de chercher les fichiers. Si la compétition est fermée à la date où vous redonnez ce cours, nous restons sur le calcul autorisé et le bilan ; nous ne promettons pas une soumission classée.

https://github.com/MathieuDWeill/ai-course-student/blob/main/usecase/MyLittleMLLab/templates/KAGGLE_AML_05.ipynb

Question à expliquer : Qu’est-ce qui prouve qu’un run distant a terminé ?

## 41. D12 · Retrouver les preuves — D12

Le dossier runs/J5 rassemble les sorties ; les données officielles ne vont pas sur GitHub public.

Nous distinguons les fichiers utiles au raisonnement. Les scores par fold expliquent la comparaison. Les OOF permettent les diagnostics et la moyenne. Le protocole identifie les conditions. La décision indique ce qui sera livré. Tout n’a pas vocation à être publié : les fichiers de lignes de compétition peuvent être soumis à des conditions de redistribution. Pour le cours public, nous gardons le code, les supports et des résumés de résultats sans les données brutes.

Question à expliquer : Quel fichier J6 utilisera-t-il en premier ?

## 42. Revue croisée : expliquer le voisin — D12

Un étudiant montre une preuve ; un autre explique ce qu’elle permet de conclure.

Nous échangeons les rôles. Le propriétaire du notebook choisit un fichier, sans donner immédiatement sa conclusion. Le vérificateur nomme les données et le critère. Le rapporteur dit une phrase de conclusion et une limite. Si quelqu’un ne peut pas expliquer une valeur, nous reprenons cette valeur ensemble plutôt que de passer à un nouveau modèle. Chaque personne doit produire une réponse individuelle à la fin, même si le travail technique a été fait en trinôme.

Question à expliquer : Quelle preuve changerait votre décision actuelle ?

## 43. Le billet de sortie individuel

Hypothèse · budget · preuve · limite · prochaine décision

Écrivez cinq phrases courtes, avec les mots de votre résultat. Ne racontez pas tous les détails du code. Dites ce que vous avez voulu tester, combien de fits ont été réalisés, ce que le tableau montre, ce qu’il ne montre pas et ce que vous conservez pour J6. Nous relisons deux réponses et chacun corrige la sienne. Cela vérifie la compréhension individuelle, pas seulement la présence d’un notebook exécuté.

Question à expliquer : Peut-on écrire un score Kaggle public dans ce billet ?

## 44. Ce que J5 laisse à J6 — D12

Un choix figé et des preuves ; demain, un système rechargeable.

Nous terminons avec une décision, même si c’est de garder la référence. J6 ne consiste pas à lancer encore des candidats. Il consiste à rendre le résultat utilisable et contrôlable : entrée définie, pipeline conservé, fichier aligné, API testée et limites écrites. Le passage au texte et à l’image gardera la même exigence. Les représentations changeront, mais nous devrons toujours expliquer la question et montrer une preuve.

Question à expliquer : Quelle est la première action de J6 ?
