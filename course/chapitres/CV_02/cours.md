# CV_02 - Évaluer la robustesse et livrer la vision

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Un score image se traduit-il en une inférence fiable ?

## Ce que nous réutilisons

Le transfert, le contrat d’inférence et les artefacts complets.

## Ce que vous devez savoir montrer

Vérifier sens des probabilités, limites, rechargement et mesure du coût.

## Les mots du chapitre

**Log-loss** : La pénalité associée à la probabilité attribuée à la vraie classe.

**Robustesse** : Le comportement sous des variations définies des entrées.

**Hors domaine** : Une entrée différente de la population couverte par l’évaluation.

**Latence** : La durée d’une inférence selon un périmètre et une machine précisés.

## Comprendre le raisonnement

Une tête seule et une adaptation partielle n’utilisent pas le même nombre de paramètres entraînables. On compare leur performance sur les mêmes images et on mesure le coût. Changer simultanément le split, l’augmentation et le backbone empêche d’attribuer clairement un gain à l’adaptation.

La robustesse ne se résume pas à un score moyen. Une galerie d’erreurs examine flou, cadrage, lumière, plusieurs objets et images hors domaine. Un réseau peut produire un score élevé pour une entrée qu’il ne sait pas traiter. Si le système doit refuser certaines entrées, cette règle fait partie du contrat et doit être évaluée.

La log-loss évalue la probabilité assignée à la vraie classe et pénalise fortement une erreur très confiante. Pour un problème chiens/chats, l’inversion du sens de la probabilité peut détruire le résultat sans changer les dimensions du CSV. On vérifie donc explicitement la classe positive et les identifiants.

Le pipeline livré recharge poids et prétraitement, puis produit les mêmes sorties sur un lot connu. La durée d’inférence mentionne batch, machine, échauffement et périmètre mesuré. Un GPU peut nécessiter une synchronisation pour chronométrer correctement. La fiche modèle précise les populations évaluées, les limites et l’usage prévu ; elle n’annonce pas une compétence universelle sur toutes les images.

## Un calcul à savoir lire

La log-loss binaire est la moyenne de −[y ln(p) + (1−y) ln(1−p)]. Pour une observation positive, p=0,9 donne environ 0,105, tandis que p=0,1 donne environ 2,303. Une erreur très confiante reçoit donc une forte pénalité ; le sens de la probabilité doit être vérifié.

## CV_02-D1 - Exemple résolu

Pour un exemple de classe positive, une probabilité 0,9 donne une perte -log(0,9), environ 0,105. Une probabilité 0,1 donne environ 2,303 : la prédiction fausse et confiante est bien plus pénalisée.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
from math import log
print(round(-log(0.9),3),round(-log(0.1),3))
```

Sortie du calcul pédagogique :

```text
0.105 2.303
```

## CV_02-D2 - Démonstration accompagnée

La confiance erronée est pénalisée. Cette démonstration est exécutée dans le notebook du chapitre, au repère **CV_02-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
from pathlib import Path
from tempfile import TemporaryDirectory
from sklearn.metrics import log_loss
y=np.array([1,0])
for name,p in [('raisonnable',np.array([.8,.2])),
               ('inverse_confiante',np.array([.01,.99]))]:
    print(name,'log-loss :',round(log_loss(y,p,labels=[0,1]),3))
features=np.array([[.2,.3,.8],[.8,.3,.1]])
weights=np.array([1.,0.,-1.])
predict=lambda w: 1/(1+np.exp(-(features@w)))
reference=predict(weights)
with TemporaryDirectory() as d:
    path=Path(d)/'petit_modele.npz'
    np.savez(path,weights=weights)
    with np.load(path,allow_pickle=False) as artifact:
        restored=artifact['weights']
    assert np.allclose(reference,predict(restored))
print('Poids du petit modèle sauvegardés et rechargés : prédictions identiques.')
print('Démonstration numérique sur trois caractéristiques, distincte du CNN de l’atelier.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
raisonnable log-loss : 0.223
inverse_confiante log-loss : 4.605
Poids du petit modèle sauvegardés et rechargés : prédictions identiques.
Démonstration numérique sur trois caractéristiques, distincte du CNN de l’atelier.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## CV_02-E1 - Expliquer

Une image contient à la fois un chat et un chien. Quelle limite cela expose-t-il pour une classification binaire à une seule étiquette ?

## CV_02-E2 - Transférer

La durée d’un batch GPU est mesurée sans attendre la fin des opérations. Que peut-on conclure ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## CV_02-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Présenter un préentraînement comme une garantie de généralisation ou ignorer le sens de la classe positive.

## La suite du parcours

Le parcours se clôt sur une compétence commune : poser une question, évaluer honnêtement et livrer une prédiction dont on sait discuter les limites.

## Références techniques

- https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
