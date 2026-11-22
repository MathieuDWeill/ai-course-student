# AML_05 - Choisir les expériences et leur budget

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Quelle expérience mérite le prochain budget de calcul ?

## Ce que nous réutilisons

Les erreurs, les représentations, les ensembles et la boucle neuronale.

## Ce que vous devez savoir montrer

Choisir une expérience à partir d’une erreur observée et conclure même en cas d’échec.

## Les mots du chapitre

**Hypothèse** : Une explication ou un effet attendu que l’expérience peut examiner.

**Budget** : Les limites annoncées en essais, temps, données ou ressources.

**OOF** : Des prédictions obtenues pour chaque observation sans l’entraîner dans le modèle du fold correspondant.

**Ensemble** : Une combinaison de modèles ou de prédictions.

## Comprendre le raisonnement

Une nouvelle expérience répond à une observation : quelle erreur veut-on réduire, par quel mécanisme et à quel coût ? « Tester un gros modèle » n’est pas encore une hypothèse. « Une transformation compressant les grandes valeurs pourrait réduire la sensibilité aux extrêmes » est plus précis et permet une ablation.

Un test sur quelques lignes vérifie les formes et le contrat. Un petit budget élimine ensuite les pistes manifestement défaillantes ; les candidats justifiés reçoivent davantage de calcul. Un échec correctement documenté évite de répéter la même idée sans apprendre.

La ressource mesurée précise le périmètre : préparation, fit, prédiction, mémoire du processus ou mémoire du GPU ne sont pas interchangeables. Une comparaison de durées indique machine, versions, nombre de lignes et éventuel échauffement. Le cache peut accélérer un second passage sans rendre l’algorithme intrinsèquement meilleur.

Les prédictions hors fold peuvent servir à analyser les erreurs ou construire une combinaison sans entraîner la combinaison sur des prédictions obtenues sur leurs propres lignes d’apprentissage. Elles restent des données de développement : sélectionner de nombreuses variantes sur elles peut aussi les suradapter. Un ensemble utile apporte des erreurs complémentaires et justifie son coût.

## Un calcul à savoir lire

Budget de fits = configurations × folds × seeds. Douze configurations, trois folds et deux seeds donnent 72 fits. À quatre minutes chacun, le budget séquentiel estimé est de 288 minutes, soit 4 h 48, hors préparation et autres calculs. Paralléliser modifie le temps mural et la mémoire nécessaire.

## AML_05-D1 - Exemple résolu

Douze configurations, trois folds et deux seeds représentent 72 fits. À quatre minutes par fit, le budget séquentiel est de 288 minutes, soit quatre heures et quarante-huit minutes, hors préparation.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
fits=12*3*2; minutes=fits*4
print(fits,minutes,divmod(minutes,60))
```

Sortie du calcul pédagogique :

```text
72 288 (4, 48)
```

## AML_05-D2 - Démonstration accompagnée

Construire des prédictions hors fold. Cette démonstration est exécutée dans le notebook du chapitre, au repère **AML_05-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
X,y=make_classification(n_samples=180,n_features=6,n_informative=3,random_state=17)
oof=np.full(len(y),np.nan)
for tr,va in StratifiedKFold(3,shuffle=True,random_state=17).split(X,y):
    assert not set(tr)&set(va)
    model=LogisticRegression(max_iter=500).fit(X[tr],y[tr])
    oof[va]=model.predict_proba(X[va])[:,1]
assert np.isfinite(oof).all()
print('Prédictions hors fold :',len(oof),'fits :',3)
print('AUC de développement :',round(roc_auc_score(y,oof),3))
print('Ce développement ne doit pas être présenté comme test final indépendant.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Prédictions hors fold : 180 fits : 3
AUC de développement : 0.936
Ce développement ne doit pas être présenté comme test final indépendant.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## AML_05-E1 - Expliquer

Une variante gagne 0,0002 d’AUC et multiplie le temps de prédiction par dix. Quelle conclusion écrire ?

## AML_05-E2 - Transférer

Deux modèles ont des scores voisins et exactement les mêmes erreurs. Pourquoi leur moyenne peut-elle apporter peu ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## AML_05-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Lancer plusieurs changements à la fois, oublier les échecs ou comparer des durées mesurées sur des matériels différents sans le préciser.

## La suite du parcours

La dernière journée ML transforme le candidat choisi en système vérifiable et livrable.

## Références techniques

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/model_evaluation.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
