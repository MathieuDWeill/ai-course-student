# Les mots du laboratoire

Les exemples concernent le classement de paiements selon leur risque de fraude.

|Terme|Sens et exemple|
|---|---|
|Observation|Une ligne de données. Ici, un paiement.|
|Variable ou feature|Une information décrivant la ligne, comme le montant. Elle doit être disponible au moment de prédire.|
|Cible ou target|La réponse que l’on cherche à prédire. Ici, 0 pour normal et 1 pour fraude dans les lignes étiquetées.|
|Modèle|Une règle calculable qui transforme les variables en une sortie.|
|Paramètre|Une valeur apprise pendant le fit, comme un coefficient ou un seuil d’arbre.|
|Hyperparamètre|Un choix qui pilote l’apprentissage, comme la profondeur maximale ou le learning rate.|
|Fit ou entraînement|L’opération qui ajuste les paramètres à partir des exemples d’apprentissage.|
|Prédiction|Le résultat produit avec des paramètres déjà ajustés, pour une ligne donnée.|
|Référence ou baseline|Une solution minimale servant de point de comparaison. Une probabilité constante constitue une première référence.|
|Split|Une séparation des données selon le besoin d’évaluation. Les lignes, sources ou dates peuvent imposer des contraintes.|
|Fold|Une partie des données utilisée dans la validation croisée. À trois folds, chaque partie sert une fois à évaluer et les deux autres à apprendre.|
|Validation croisée ou CV|Plusieurs entraînements sur des séparations organisées pour comparer des candidats. Les transformations sont ajustées dans chaque fit.|
|Fuite de données|Une information disponible pendant l’expérience qui ne devrait pas l’être au moment de prédire. Par exemple, ajuster une transformation avec la validation ou utiliser une réponse future.|
|Pipeline|Un enchaînement de transformations et d’un modèle. Son fit ajuste les transformations sur les lignes d’apprentissage.|
|Imputation|Une règle pour remplacer une valeur manquante. Par exemple, une médiane calculée uniquement sur le train.|
|Mise à l’échelle|Une transformation de l’échelle numérique, comme soustraire la moyenne puis diviser par l’écart-type appris sur le train.|
|One-hot|Une représentation qui crée des indicateurs pour les catégories. Elle ne donne pas une distance numérique naturelle entre mobile et desktop.|
|Encodage ordinal|Une représentation par codes numériques. Si le modèle traite ces codes comme des quantités, il peut introduire un ordre arbitraire.|
|Ablation|Une comparaison contrôlée de variantes pour attribuer un effet à une modification. Ici, remplacer ou ajouter quatre variables log1p.|
|AUC ROC|Une mesure de classement des scores entre les deux classes. Une AUC de 0,93 ne signifie pas que 93 % des fraudes sont détectées.|
|Accuracy|La proportion de classes prédites correctement à un seuil. Elle peut être élevée même si toutes les fraudes rares sont ratées.|
|Rappel ou recall|La part des fraudes réellement présentes que les alertes détectent. TP/(TP+FN).|
|Précision|La part des alertes qui correspondent réellement à une fraude. TP/(TP+FP).|
|Seuil ou threshold|La valeur à partir de laquelle un score déclenche une alerte. Elle transforme un classement en décision.|
|Faux positif|Une alerte sur un paiement normal.|
|Faux négatif|Une fraude que le modèle n’alerte pas au seuil choisi.|
|Dispersion|La variation entre les scores observés, par exemple leur écart-type sur les folds. Cet écart-type n’est pas automatiquement un intervalle de confiance.|
|Surapprentissage|Le modèle apprend des particularités du train qui se reproduisent mal sur des observations séparées. Un score train élevé ne suffit pas au diagnostic.|
|Gini|Un critère de mélange des classes utilisé dans certains arbres. Il vaut 1 − somme des proportions au carré. Une feuille pure donne zéro.|
|Bootstrap|Un tirage de lignes avec remise. Une ligne peut apparaître plusieurs fois dans un même échantillon.|
|Forêt|Un ensemble d’arbres construits avec de l’aléa, dont on combine les prédictions. Les arbres internes ne sont pas des folds de CV.|
|Boosting|Une construction séquentielle qui ajoute des corrections pour réduire une perte.|
|Perte ou loss|La fonction numérique que l’apprentissage cherche à réduire. Elle peut différer de la métrique officielle d’évaluation.|
|MSE|La moyenne des erreurs au carré. Elle sert au petit exemple de boosting en régression.|
|Gradient|Les dérivées locales de la perte par rapport aux paramètres. Il indique comment la perte varie près des poids courants.|
|Forward|Le calcul de la sortie à partir des entrées et des poids courants.|
|Backward|Le calcul des gradients par rétropropagation. Dans notre boucle PyTorch, il ne modifie pas directement les poids.|
|Step|L’appel de l’optimiseur qui met à jour les poids selon les gradients et sa règle.|
|zero_grad|La remise à zéro des gradients avant un nouveau calcul, pour éviter une accumulation involontaire.|
|Learning rate|Un hyperparamètre qui règle la taille des mises à jour. Un pas plus grand peut accélérer, osciller ou diverger.|
|Logit|Un score brut produit par le classifieur avant normalisation. Il peut être négatif et n’est pas une probabilité.|
|Softmax|Une transformation de plusieurs logits en probabilités qui somment à un.|
|Cross-entropy|Une perte de classification. Pour une ligne, sa forme simple est −log de la probabilité de la vraie classe. CrossEntropyLoss attend ici directement les logits.|
|Neurone et couche|Un neurone combine ses entrées avec des poids et un biais. Une couche rassemble plusieurs de ces calculs.|
|ReLU|La fonction max(0,z), qui ajoute une non-linéarité.|
|Batch|Un groupe de lignes traité pour une mise à jour. Le dernier batch peut être plus petit.|
|Epoch|Un passage sur l’ensemble d’apprentissage. Une epoch comprend plusieurs batches.|
|Float32|Un type numérique de 32 bits, soit quatre octets par valeur, hors autres objets et allocations.|
|SGD|Un optimiseur dont la mise à jour simple soustrait learning rate × gradient.|
|AdamW|Un optimiseur avec adaptation des mises à jour et weight decay découplé. Sa mise à jour n’est pas exactement la simple formule SGD.|
|Régularisation|Un choix qui limite certaines solutions ou la capacité d’apprentissage. Son effet se vérifie sur le protocole.|
|Weight decay|Un mécanisme qui agit sur les poids selon l’optimiseur. Dans notre réseau principal, il est fixé à 0,01 avec AdamW.|
|Dropout|Un mécanisme qui annule aléatoirement certaines activations pendant l’apprentissage. Sa démonstration est séparée du réseau principal.|
|Early stopping|Une règle d’arrêt fondée sur une mesure de validation. Elle doit préciser critère, patience et checkpoint conservé.|
|Checkpoint|Une sauvegarde d’un état du modèle. Il faut aussi conserver architecture et prétraitement pour reproduire une prédiction.|
|train et eval|Des modes de module PyTorch qui changent certains comportements, comme dropout. eval ne désactive pas à lui seul les gradients.|
|no_grad|Un contexte PyTorch qui évite l’enregistrement des nouveaux calculs pour les gradients. Il ne change pas le mode train/eval.|
|Seed|Une valeur qui initialise des générateurs aléatoires. Elle aide à reproduire une configuration, sans garantir une identité entre tous les matériels et versions.|
|CPU et GPU|Deux types de ressources de calcul. Un GPU peut accélérer certaines opérations, mais ne corrige ni un mauvais split ni une mauvaise cible.|
|n_jobs|Le nombre de tâches parallèles demandé à certains outils. Le laboratoire utilise n_jobs=1 pour éviter une concurrence excessive.|
|Run|Une exécution identifiée avec ses résultats et sa configuration.|
|Manifeste|Un fichier décrivant les éléments de l’expérience, comme données, choix, budget et empreintes.|
|Empreinte SHA-256|Un résumé calculé d’un fichier qui permet de détecter un changement de contenu.|
|CSV de soumission|Un fichier de prédictions au format attendu. Sa validité technique ne prouve pas la qualité du modèle.|
|Score public|Le résultat renvoyé après un dépôt réel sur la partie publique d’une compétition. Il reste inconnu avant ce retour.|
