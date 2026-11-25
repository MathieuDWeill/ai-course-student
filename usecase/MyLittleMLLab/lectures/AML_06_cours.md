# J6 — Livrer un système vérifiable

Conception pédagogique : Mathieu Weill.

Repères D1 à D12 communs au notebook, à la projection et au guide.

## 2. Les huit étapes de J6

7 heures pédagogiques ; pauses à ajouter selon l’emploi du temps.

Nous allons construire les preuves dans l’ordre. Chaque bloc réutilise le précédent. Si le rechargement échoue, nous le corrigeons avant l’API. Si le CSV est mal aligné, nous ne le déposons pas. Les démonstrations restent accompagnées, et chacun doit manipuler ou expliquer une étape. La dernière partie est une revue du système et de ses limites, pas une compétition de vitesse.

Question à expliquer : Peut-on ignorer un contrôle raté pour finir la démonstration ?

## 3. La progression reste la même

Python : données → J2 : split → J3/J4 : modèles → J5 : choix → J6 : système

Un système fiable réutilise des gestes déjà appris. La jointure vient de pandas. La séparation vient de la validation. Le prétraitement appris fait partie du pipeline. Le choix figé vient du budget d’expériences. L’API ajoute une interface pour une autre application. Elle n’efface pas les étapes précédentes. Nous allons relier chaque contrôle technique à un risque concret pour que la liste de fichiers ait un sens.

Question à expliquer : Quelle notion de Python évitera aujourd’hui une erreur silencieuse ?

## 4. Un résultat correct peut être livré incorrectement — D2

Même modèle, mauvais ordre de lignes : mauvais fichier.

Une prédiction possède une valeur et un destinataire. Si nous envoyons le score d’un paiement à un autre paiement, le modèle n’a pas changé mais le résultat livré est faux. Ce risque est plus banal qu’une formule compliquée. Nous allons commencer par trois identifiants visibles. Vous pourrez vérifier le résultat sans croire le programme sur parole. Le même contrôle sera ensuite appliqué aux centaines de milliers de lignes du test officiel.

Question à expliquer : La même longueur garantit-elle le bon alignement ?

## 5. D1 · Lire le choix avant de réentraîner — D1

runs/J5/decision.json doit exister ; mêmes données et même liste d’IDs.

Ouvrez le notebook AML zéro six et le repère D1. Le code refuse de poursuivre si la décision de J5 manque. C’est volontaire : nous ne remplaçons pas un résultat absent par un gagnant imaginé. Le fichier indique la limite de données, les membres et le nombre de fits de refit. Si un autre étudiant fournit une décision, elle doit correspondre aux mêmes données et au même protocole. Nous vérifions ces conditions avant d’apprendre.

https://github.com/MathieuDWeill/ai-course-student/blob/main/course/seances/AML_06.md

Question à expliquer : Que faire si decision.json manque ?

## 6. Trois identifiants, deux ordres — D2

Exemple fictif : sample 18, 12, 27 ; prédictions 12, 18, 27.

Lisez la table sans calculer de modèle. Le score de douze vaut zéro virgule neuf, celui de dix-huit zéro virgule un et celui de vingt-sept zéro virgule trois. Le sample demande un autre ordre. Copier simplement la colonne conserve les valeurs mais les attache aux mauvaises lignes. Nous devons utiliser la clé id. Une clé dit quelle observation reçoit la valeur, indépendamment de sa position actuelle dans un tableau.

Question à expliquer : Quel score doit suivre l’identifiant 18 ?

## 7. D2 · La jointure corrige le destinataire — D2

left join sur id ; validate="one_to_one" ; ordre du sample conservé.

Une jointure relie les lignes par leur identifiant. Le paramètre one to one exige ici une ligne de chaque côté pour chaque clé ; il aide à repérer les doublons. Nous vérifions aussi que l’ensemble des identifiants est complet. Sinon, une jointure pourrait laisser des valeurs manquantes. Le résultat final doit conserver l’ordre du sample. Il ne suffit pas que merge termine sans erreur : les contrôles après la jointure sont indispensables.

```text
aligned = align_submission(sample_demo, pred_demo)
assert np.allclose(aligned.is_fraud, [0.1, 0.9, 0.3])
display(aligned)
```

Question à expliquer : Une jointure suffit-elle à détecter tout identifiant manquant ?

## 8. Le contrat de sortie du CSV — D7

id unique · ordre officiel · deux colonnes · scores finis entre 0 et 1

Le contrat de sortie explique ce que le destinataire attend. Ici, Kaggle fournit les identifiants et les noms de colonnes. Nous ne devons pas ajouter un index CSV ou transformer les scores en classes si le format demande des probabilités estimées. Les contrôles sont simples, mais chacun correspond à une panne possible. La soumission au classement est une action distincte, avec ses règles et sa disponibilité, que ce notebook ne réalise pas.

Question à expliquer : Pourquoi ne pas exporter seulement 0 ou 1 ?

## 9. Refit : réapprendre le candidat retenu — D3

Même configuration choisie ; tout le train de développement déclaré.

Les modèles de CV ont appris chacun sur une partie des lignes. Pour la livraison, nous réentraînons le candidat choisi sur le train de développement complet prévu, dans la limite annoncée. Les paramètres appris changent, mais nous ne cherchons pas de nouveau C. Nous ne réintroduisons pas les labels du contrôle pour décider. Le refit est donc une étape d’entraînement qui suit la sélection, pas une seconde compétition cachée.

Question à expliquer : Refit signifie-t-il relancer tous les candidats ?

## 10. D3 · Sauvegarder le pipeline complet — D3

Prétraitement + modèle(s) + composition ; manifeste séparé.

Le pipeline contient l’imputation, l’encodage, la mise à l’échelle si elle est utilisée et le modèle. Nous le sauvegardons ensemble pour éviter de refaire un prétraitement différent au moment de prédire. Le manifeste décrit les versions, les données et l’empreinte du fichier. Ce texte rend la livraison compréhensible, mais le fichier sérialisé doit provenir d’une source approuvée. Un hash ne transforme pas un fichier inconnu en fichier sûr.

Question à expliquer : Que manquerait-il à des coefficients seuls ?

## 11. Le manifeste est une fiche technique — D3

Il décrit la version livrée ; il ne contient pas les données officielles complètes.

Un manifeste est un inventaire de ce qu’il faut savoir pour utiliser cette version. Le modèle choisi, le nombre de lignes apprises et les versions de bibliothèques permettent de comprendre le contexte. L’empreinte aide à détecter une modification du fichier par rapport à cette fiche. Si quelqu’un modifie à la fois le fichier et la fiche, ce contrôle ne prouve pas son honnêteté : la provenance et les droits restent importants.

Question à expliquer : Une empreinte prouve-t-elle à elle seule qu’un modèle inconnu est fiable ?

## 12. D4 · Décrire les entrées attendues — D4

Clés, types, valeurs null, catégories et sens de la sortie.

Le contrat précise les noms de colonnes et leur type. Un booléen signifie vrai ou faux ; il ne se confond pas avec une chaîne de texte. Une clé absente est refusée, alors qu’une valeur null est admise dans la politique de ce pipeline et sera imputée avec ce qui a été appris. Une catégorie inconnue peut être traitée techniquement sans garantir une bonne qualité sur cette catégorie. Accepter une entrée et prédire correctement sont deux questions distinctes.

Question à expliquer : Une clé absente et une valeur null sont-elles la même chose ?

## 13. Une unité peut changer le sens sans changer le type — D4

20 euros et 20 centimes sont deux nombres ; le contrat doit préciser le sens.

Le type informatique ne suffit pas à comprendre une donnée. Le nombre vingt peut représenter un montant, une ancienneté ou un nombre d’actions. Dans cet atelier, nous conservons le sens et l’échelle des colonnes du jeu officiel. Dans un service réel, il faudrait documenter les unités et la disponibilité des variables au moment de la décision. Un nombre techniquement valide dans la mauvaise unité peut produire un résultat absurde sans déclencher d’erreur de Python.

Question à expliquer : Une validation de type détecte-t-elle automatiquement une mauvaise unité ?

## 14. D4 · Une entrée valide donne trois scores — D4

Trois lignes JSON → trois scores de la classe 1 ; calibration non démontrée.

Le fichier exemple contient trois observations déjà disponibles dans le laboratoire. JSON transporte des clés et des valeurs ; il ne transporte pas l’objet Python du modèle. Le serveur reconstruira un tableau dans l’ordre attendu par le pipeline. Nous regardons trois scores pour vérifier le contrat. Un score proche de zéro ou de un ne suffit pas à prouver une calibration correcte. Aujourd’hui, nous garantissons le chemin et la signification annoncée de la sortie, pas une certitude sur un cas individuel.

Question à expliquer : Trois observations doivent-elles donner trois scores ?

## 15. D5 · Trois refus attendus — D5

Clé absente, clé supplémentaire, texte à la place d’un nombre.

Un test négatif envoie volontairement une entrée invalide. Le résultat attendu est alors un refus compréhensible, pas un score inventé. Ce refus protège le sens du service. Nous modifions des copies des données pour conserver l’exemple correct. Chaque étudiant doit expliquer un cas : quelle règle est rompue et quelle réponse attendre. Un message d’erreur prévu fait partie d’une démonstration réussie. Il ne faut pas le confondre avec une panne inattendue.

Question à expliquer : Un refus attendu signifie-t-il que le modèle est cassé ?

## 16. Les catégories nouvelles ne sont pas magiques — D5

Le pipeline prévoit leur traitement ; la qualité reste une question d’évaluation.

Un système peut rencontrer une chaîne de catégorie absente du train. Le pipeline garde la politique d’encodage apprise et la manière de traiter l’inconnu. C’est préférable à réapprendre un encodage sur les requêtes. Mais cela ne prouve pas que le risque est bien estimé pour cette nouvelle catégorie. Nous devons surveiller leur fréquence et analyser la qualité lorsque les labels arrivent. La robustesse de format et la généralisation ne sont pas interchangeables.

Question à expliquer : Faut-il réentraîner l’encodeur à chaque nouvelle requête ?

## 17. Prédire en mémoire ne prouve pas le rechargement — D6

Le notebook peut cacher des objets, des imports ou des transformations déjà présents.

Si nous sauvegardons le modèle puis continuons à utiliser la variable en mémoire, nous n’avons rien vérifié sur le fichier. Même recharger dans le même notebook peut masquer une dépendance oubliée. Nous allons donc créer un nouveau processus Python. Ce programme devra lire le modèle et un fichier d’entrée, puis écrire les scores. Il n’aura pas accès aux variables de notre noyau. C’est une preuve plus forte de ce que nous avons réellement livré.

Question à expliquer : Quel objet le nouveau processus ne doit-il pas réutiliser ?

## 18. D6 · Un programme séparé utilise la livraison — D6

python -m mllab.delivery_j56 avec bundle, entrée et sortie.

L’option tiret m demande à Python d’exécuter un module du laboratoire. Les options bundle, input et output donnent les chemins nécessaires. Le même exécutable Python conserve notre environnement pour cette vérification. Ce n’est pas encore un test sur tous les PC et Mac possibles, mais il détecte la dépendance aux variables du notebook. La commande est affichée pour qu’une autre personne puisse comprendre ce qui est relancé. Aucun réseau n’est utilisé ici.

```text
python -m mllab.delivery_j56 \
  --bundle runs/J6/release \
  --input runs/J6/release/exemple_entree.json \
  --output runs/J6/release/resultat_recharge.json
```

Question à expliquer : La commande entraîne-t-elle à nouveau le modèle ?

## 19. Comparer avec une tolérance numérique — D6

Même forme, même ordre, valeurs proches selon rtol et atol.

Les nombres flottants sont des approximations informatiques. Nous vérifions que les scores avant et après sont proches dans une tolérance annoncée, avec NumPy allclose. Une petite tolérance ne permet pas d’accepter une inversion de lignes ou une différence importante. Les contrôles de forme et d’ordre restent nécessaires. Un environnement logiciel différent peut aussi rendre un artefact incompatible ; c’est pour cela que les versions sont consignées et que le modèle peut devoir être reconstruit.

```text
assert np.allclose(expected, reloaded["scores"],
                   rtol=1e-6, atol=1e-8)
# Ce contrôle ne remplace pas le contrat de données.
```

Question à expliquer : Pourquoi ne pas simplement dire « les deux listes existent » ?

## 20. Reproduire ailleurs demande plus qu’un fichier — D6

Code, dépendances, contrat, modèle et instructions vont ensemble.

Le nouveau processus utilise encore le même ordinateur. Pour transmettre le projet à quelqu’un d’autre, il faut également donner le code utile et les versions, expliquer l’installation et respecter les droits sur les données. Le modèle sérialisé n’est pas une application autonome. Si une bibliothèque manque, le destinataire doit pouvoir comprendre ce qui manque. Une archive livrable réunit donc les fichiers et un chemin de vérification, sans y glisser des données ou des secrets non autorisés.

Question à expliquer : Un fichier joblib est-il un programme autonome universel ?

## 21. D7 · Produire les scores du test officiel — D7

Le refit prédit ; le sample détermine IDs, ordre et colonnes.

Nous utilisons maintenant le test sans labels de la compétition. Son rôle est de recevoir les scores, pas de nous apprendre directement quel candidat est meilleur localement. Le pipeline figé traite les données et la jointure aligne les valeurs. Nous vérifions chaque invariant avant d’écrire le fichier. Le notebook ne clique pas sur une soumission et ne contacte pas Kaggle. Son résultat est un CSV local vérifié, que l’on peut ensuite examiner selon les règles et la disponibilité du concours.

Question à expliquer : Peut-on calculer ici l’AUC du test Kaggle ?

## 22. Contrôler la bonne chose au bon moment — D7

Fichier créé ≠ fichier correct ≠ soumission acceptée ≠ résultat de production.

Ces quatre étapes sont souvent confondues. Un fichier peut exister avec le mauvais ordre. Une plateforme peut accepter un format sans que le modèle soit bon. Un leaderboard peut mesurer une compétition sans représenter une entreprise future. Nous ne retirons rien à la valeur de Kaggle en précisant cela : nous comprenons exactement quelle preuve chaque étape donne. Une explication rigoureuse permet de défendre le travail sans lui prêter une portée qu’il n’a pas.

Question à expliquer : Une soumission acceptée prouve-t-elle l’efficacité en entreprise ?

## 23. Entraîner, servir, recevoir : trois rôles — D8

Le notebook apprend ; le service prédit ; le client envoie une requête.

L’entraînement produit un état de modèle. Le service charge cet état et l’utilise pour les nouvelles entrées. Le client est le programme qui appelle ce service. Dans notre démonstration, nous ne réentraînons pas le modèle à chaque requête. Cela ferait dépendre le résultat du contenu et de l’ordre des appels, en plus de consommer du calcul inutile. Nous gardons le service simple pour rendre son contrat visible.

Question à expliquer : Où se déroule le fit dans notre parcours ?

## 24. REST, HTTP et FastAPI : le rappel utile — D8

Un style d’organisation, un protocole d’échange et un outil Python.

REST décrit un style d’architecture. HTTP porte ici une requête avec une méthode et un chemin. FastAPI nous aide à écrire les routes du serveur Python et à valider les données. Les trois notions peuvent se combiner sans être synonymes. Nos deux routes illustrent une petite API HTTP ; elles ne suffisent pas à revendiquer toutes les contraintes d’un service REST complet. Nous gardons la distinction de J3_2 et nous la mettons en pratique.

Question à expliquer : POST est-il le nom d’une bibliothèque Python ?

## 25. Deux routes, deux résultats attendus — D8

GET /health : prêt ; POST /predictions : scores ou refus.

La route health permet de vérifier qu’une version est chargée et d’identifier son empreinte. Elle ne prouve pas une bonne qualité de prédiction. La route predictions reçoit des lignes, applique le contrat et renvoie un score par ligne. Si le contrat est invalide, nous attendons un refus. Le code de réponse est un indicateur simple : deux cents pour une réussite prévue, quatre cent vingt-deux pour les entrées invalides de notre exemple.

Question à expliquer : Un /health qui répond prouve-t-il une bonne AUC ?

## 26. D8 · Tester sans ouvrir un port réseau — D8

TestClient appelle l’application localement dans le processus.

Nous commençons par le client de test. Il permet de vérifier les routes et les réponses sans dépendre d’un port déjà utilisé ni d’un navigateur. Cela évite une difficulté de démonstration sans cacher le contrat. Ce test ne mesure pas une latence réseau et ne représente pas une charge de production. Il vérifie une application locale avec des requêtes déterminées. Nous lançons d’abord l’entrée correcte, puis l’entrée dont une clé a été retirée.

```text
client = TestClient(create_app(RELEASE))
client.get('/health')
client.post('/predictions', json={'rows': rows})
```

Question à expliquer : Pourquoi tester d’abord sans serveur réseau ?

## 27. Le refus est une fonctionnalité — D8

Réponse invalide → message explicite ; aucune probabilité inventée.

Le cas invalide nous intéresse autant que le cas normal. Un service qui renvoie toujours quelque chose peut masquer une entrée incorrecte. Notre objectif est d’indiquer clairement la règle rompue. L’utilisateur du service peut alors corriger son programme. Dans un système plus complet, il faudrait aussi décider quels détails d’erreur peuvent être exposés, comment authentifier le client et quoi journaliser. Notre exemple ne résout pas automatiquement ces questions de production.

Question à expliquer : Faut-il remplacer un nombre invalide par zéro sans le dire ?

## 28. Afficher la documentation dans le navigateur — D8

Terminal du laboratoire → uvicorn sur 127.0.0.1:8006 → /docs

Le kit contient api_j6.py. Dans un terminal ouvert à la racine du laboratoire, la commande démarre le service local. L’adresse cent vingt-sept point zéro point zéro point un signifie cette machine. Dans le navigateur, la page docs permet d’essayer les routes. Copiez le contenu d’exemple_entree.json dans le corps de la requête, pas un extrait de trois colonnes seulement. Pour arrêter le serveur, utilisez contrôle C dans son terminal. Ne lancez pas cette commande dans une cellule bloquante du notebook.

```text
python -m uvicorn api_j6:app --host 127.0.0.1 --port 8006

Navigateur : http://127.0.0.1:8006/docs
```

Question à expliquer : Où doit être exécutée cette commande ?

## 29. Ce que l’API locale ne fournit pas encore — D8

Authentification, protection réseau, supervision et objectifs de service restent à définir.

Notre API fonctionne pour la démonstration locale. Elle n’est pas une promesse de production sécurisée et dimensionnée. Il faudrait notamment authentifier les utilisateurs, maîtriser les accès, surveiller la disponibilité et fixer les limites de service. Nous n’allons pas transformer cela en longue liste abstraite : retenez qu’un appel local réussi vérifie un chemin fonctionnel, dans des conditions précises. La fiche modèle et le guide doivent annoncer cette limite pour éviter un usage non prévu.

Question à expliquer : Peut-on exposer ce service tel quel à toute l’entreprise ?

## 30. Après la livraison, les entrées peuvent changer — D9

Plus de valeurs manquantes, nouvelles catégories, échelles différentes…

Un modèle est appris sur un historique. Les entrées reçues ensuite peuvent changer. Un changement peut venir d’une erreur de collecte, d’une nouvelle population ou d’un vrai changement du phénomène. Nous devons donc observer les entrées et comprendre leur provenance. La présence d’un changement ne dit pas automatiquement que le modèle est devenu mauvais. Elle déclenche une vérification, avec des labels lorsqu’ils deviennent disponibles.

Question à expliquer : Une dérive d’entrée est-elle déjà une mesure d’AUC ?

## 31. D9 · Un décalage fabriqué pour voir le mécanisme — D9

Nous déplaçons une variable numérique ; cela ne décrit pas une dérive réelle observée.

Le notebook prend un lot de référence et fabrique un second lot en déplaçant une variable. L’histogramme montre alors une distribution différente. Nous comparons une moyenne et un taux de valeurs manquantes. C’est un exemple construit pour rendre le phénomène visible. Les scores changent éventuellement, mais nous n’avons pas créé de nouvelles vérités terrain. Nous ne pouvons donc pas annoncer une nouvelle performance à partir de ces seules entrées modifiées.

Question à expliquer : Pourquoi ne pas calculer une accuracy sur les scores seuls ?

## 32. Surveiller les entrées et les sorties — D9

Une alerte de distribution demande une enquête, pas un remplacement automatique.

La moyenne d’une variable est un signal parmi d’autres. Elle peut bouger sans perte de classement, ou rester stable alors que certains groupes se dégradent. Nous regardons aussi les valeurs manquantes, les catégories nouvelles et les scores. Pour mesurer la qualité, nous attendons les résultats réels et vérifions leur délai et leur couverture. Une métrique d’exploitation doit préciser son périmètre, comme nos temps d’inférence en J5.

Question à expliquer : Une moyenne stable garantit-elle une qualité stable ?

## 33. D10 · Qui fait quoi après l’alerte ? — D10

Contrôler la source, les unités et le prétraitement avant de changer le modèle.

Une alerte sans responsable est un bruit de plus. Notre politique nomme l’équipe qui vérifie. La première action consiste à comprendre la source et les données : une unité changée peut expliquer le signal. Ensuite, nous décidons s’il faut revenir à une version approuvée ou préparer une nouvelle expérience. Réentraîner automatiquement sur des données incorrectes peut aggraver le problème. Nous enregistrons la réponse choisie et gardons les preuves.

Question à expliquer : Pourquoi ne pas réentraîner au premier signal ?

## 34. Le retour arrière doit être préparé — D10

Recharger une version approuvée et conserver l’historique des décisions.

Un retour arrière n’est pas une suppression des erreurs du journal. Il consiste à remettre une version connue, avec son modèle, son prétraitement et son contrat. Encore faut-il savoir quelle version était approuvée et comment vérifier son rechargement. Notre test du nouveau processus prépare cette capacité. Dans un vrai système, il faudrait aussi maîtriser le trafic, les requêtes en cours et les effets des décisions déjà prises. Ici, nous documentons le mécanisme sans promettre toute cette infrastructure.

Question à expliquer : Que faut-il garder avec l’ancienne version ?

## 35. La fiche modèle explique les limites d’usage — D11

Question, données, choix, sortie, conditions et limites dans un document court.

La fiche modèle s’adresse à quelqu’un qui n’a pas suivi nos journées. Elle doit expliquer la question, les lignes utilisées, la règle de sélection et ce que signifie le score. Elle doit aussi annoncer les limites : données de compétition, contrôle déjà consulté, calibration non démontrée et absence de preuve d’efficacité en entreprise. Ces phrases ne dévalorisent pas le modèle. Elles permettent de décider de son usage avec une information correcte.

Question à expliquer : À qui la fiche doit-elle être compréhensible ?

## 36. D11 · Ce qui entre dans la livraison — D11

Modèle, manifeste, exemple, résultat rechargé, code, versions et fiche.

Nous créons l’archive seulement après les contrôles. Elle inclut un exemple d’entrée et le résultat du rechargement pour faciliter la reproduction. Le code d’inférence accompagne le modèle. Nous n’ajoutons pas les données officielles brutes, les tokens ou les sorties personnelles d’authentification. Les droits sur les données et les modèles restent à respecter, même si un fichier est techniquement facile à copier. La transmission d’un modèle sérialisé suppose aussi une relation de confiance.

Question à expliquer : Pourquoi ne pas glisser tout le dossier de travail dans le ZIP ?

## 37. La commande de reproduction appartient à la livraison — D11

Un autre doit savoir quoi installer, quoi ouvrir et quoi vérifier.

Dire lance le code ne suffit pas. Le destinataire doit connaître la racine de travail, les dépendances et les chemins d’entrée et de sortie. Le guide fournit la commande de rechargement et la commande du serveur local, qui ont des rôles différents. Une personne vérifie le résultat, une autre explique les options. Nous testons cela en revue croisée pour repérer les connaissances restées seulement dans la tête de l’auteur.

Question à expliquer : Quelle différence entre la commande du module et celle d’uvicorn ?

## 38. Revue croisée du paquet — D12

Le voisin suit le guide, reproduit trois scores et explique un refus.

Nous formons des binômes de vérification au sein des trinômes, puis échangeons les rôles. Le destinataire ne doit pas dépendre d’instructions orales improvisées de l’auteur. Il lit la fiche et suit le guide. S’il rencontre un blocage, nous l’écrivons précisément : dépendance, chemin ou contrat. Nous ne copions pas un résultat préfabriqué à la place d’une exécution manquante. Cette étape évalue la livraison, pas seulement la personne qui a écrit le modèle.

Question à expliquer : Quel blocage mérite de modifier le guide ?

## 39. Une grille de preuves concrètes — D12

Le bilan distingue chaque réussite technique de la qualité du modèle.

Le notebook rassemble des indicateurs booléens : présence de la décision, fichier du modèle, rechargement, CSV aligné, API valide et refus correct. Chaque vrai correspond à une preuve déterminée. Si tout est vrai, le système pédagogique est cohérent dans l’environnement testé. Cela ne prouve pas qu’il bloque des fraudes réelles sans conséquence. La conclusion doit rester au niveau de la preuve, avec les limites de la fiche modèle.

Question à expliquer : Tous les voyants vrais prouvent-ils une généralisation universelle ?

## 40. Restitution : une chaîne, une preuve, une limite — D12

Expliquer le système plutôt que réciter le nom des bibliothèques.

Chaque trinôme présente la question, un trajet de données et une preuve de contrôle. Un membre explique les entrées, un autre le modèle et le rechargement, le troisième les sorties et les limites. Puis je pose une question à une personne qui n’a pas expliqué cette partie. Nous cherchons une compréhension partagée. Vous pouvez afficher une sortie ou un fichier, mais vous devez dire ce que cela démontre et ce qui reste inconnu.

Question à expliquer : Que dire après « mon API répond » ?

## 41. Le bilan individuel du parcours ML

Question → protocole → modèle → expérience → livraison → surveillance

Écrivez un exemple de fuite à éviter, une raison de conserver une référence et un contrôle de livraison que vous avez réellement effectué. Ajoutez une chose que vous ne savez pas encore conclure. Le but n’est pas de prétendre tout maîtriser. Il est de pouvoir prendre une prochaine décision sans masquer les preuves manquantes. Nous corrigeons ensemble les confusions les plus fréquentes avant de passer aux données texte et image.

Question à expliquer : Quel contrôle pouvez-vous maintenant expliquer sans ouvrir le code ?

## 42. Texte et image : les entrées changent, la méthode reste

TF-IDF, embeddings et pixels prolongeront le même protocole.

Dans la suite, une entrée pourra devenir une phrase ou une image. Nous devrons apprendre une représentation, contrôler les dimensions et choisir des modèles adaptés. Nous garderons les réflexes du parcours : question explicite, séparation adaptée, référence, comparaison, budget et contrat d’inférence. Un modèle préentraîné ne supprime pas ces exigences. La livraison d’un texte ou d’une image devra elle aussi expliquer ce qui est accepté, ce qui est refusé et comment la qualité est vérifiée.

Question à expliquer : Un modèle préentraîné dispense-t-il d’une validation adaptée ?

## 43. Les prochains contrats : texte et image

Une phrase, des tokens ; une image, des pixels et des canaux.

Une entrée texte demande de préciser langue, longueur et traitement des valeurs absentes. Une entrée image demande notamment un format, une taille et des canaux. Ces décisions changent le prétraitement et le contrat, comme l’ordre de nos colonnes aujourd’hui. Nous conserverons la séparation entre apprentissage des transformations et inférence. Nous ne pouvons pas remplacer une image manquante ou un texte vide sans annoncer une règle. Le nouveau domaine apporte des notions, mais il prolonge notre chaîne de contrôles.

Question à expliquer : Une image de taille différente peut-elle être ignorée silencieusement ?

## 44. Votre preuve finale — D12

Un paquet vérifiable ; une explication individuelle ; une limite reconnue.

Nous terminons les six journées de ML avec une chaîne complète, depuis la question jusqu’aux contrôles d’inférence. Le paquet n’est pas une fin en soi : il matérialise un choix et des preuves. Gardez les fichiers utiles, la fiche et la commande de reproduction. La prochaine expérience peut améliorer le système, mais elle devra conserver la même honnêteté de méthode. Un résultat négatif, un refus prévu et une limite clairement formulée sont aussi des signes de travail d’ingénieur.

Question à expliquer : Que faudrait-il vérifier avant un usage réel ?
