# CV_01 - Comprendre pixels, tenseurs et convolution

Conception pédagogique : Mathieu Weill. Usage personnel d’apprentissage ; droits et crédits tiers conservés.

## La question

Comment des pixels deviennent-ils des variables utiles ?

## Ce que nous réutilisons

Les tableaux NumPy, les batches et le réseau entraîné.

## Ce que vous devez savoir montrer

Nommer les axes, contrôler le prétraitement et séparer augmentation train et validation.

## Les mots du chapitre

**Canal** : Une composante de l’image, par exemple rouge, vert ou bleu.

**Batch** : Un lot d’images représenté dans un tenseur.

**Convolution** : Un calcul local appliquant un filtre partagé entre positions.

**Backbone** : La partie du réseau servant à extraire une représentation.

## Comprendre le raisonnement

Une image couleur est un tableau de pixels avec plusieurs canaux. Un batch ajoute un axe pour les observations. Certaines bibliothèques utilisent hauteur-largeur-canaux ; une convention fréquente dans PyTorch est batch-canaux-hauteur-largeur. Le contenu peut être identique mais l’ordre des axes change le calcul. On vérifie aussi type, plage des valeurs et normalisation.

Une convolution applique un même filtre à plusieurs positions, ce qui partage les paramètres. Elle extrait des motifs locaux qui se combinent dans les couches suivantes. Un exemple numérique de filtre illustre l’opération ; il ne démontre pas qu’un filtre appris détecte toujours un concept humain nommé.

Le transfert réutilise un réseau préentraîné comme extracteur. On peut d’abord geler le backbone et apprendre une tête. Le prétraitement doit correspondre aux poids choisis ; la conversion des canaux et le redimensionnement font partie du système.

L’augmentation transforme les images du train pour varier les exemples. Une transformation n’est pertinente que si elle préserve la cible pour le problème étudié. Un retournement peut convenir à chiens/chats mais changer le sens d’un caractère. La validation reste déterministe dans le protocole de base. Des doublons ou plusieurs images de la même source peuvent exiger une séparation par groupe.

Une architecture CNN combine généralement plusieurs opérations. Une activation ReLU remplace les valeurs négatives par zéro et introduit une non-linéarité. Une opération de pooling agrège des valeurs locales, par exemple par maximum. La tête transforme la représentation extraite en scores pour la tâche ; remplacer la tête ne signifie pas réentraîner automatiquement tout le backbone.

## Un calcul à savoir lire

Sans padding, avec un pas de 1, un filtre de taille 2×2 sur une image 3×3 donne une sortie 2×2. Un batch de forme (8,3,64,64) contient 98 304 valeurs. En float32, les valeurs occupent 393 216 octets ; ce nombre exclut activations, gradients et paramètres.

## CV_01-D1 - Exemple résolu

Un batch de huit images RGB de 64 par 64 pixels contient 8 × 3 × 64 × 64 valeurs. En float32, les seules valeurs représentent 393 216 octets, hors activations, gradients et modèle.

Avant de lancer Python, prévoir la sortie et expliquer l’unité de chaque quantité.

```python
batch=8; canaux=3; hauteur=largeur=64
valeurs=batch*canaux*hauteur*largeur
print(valeurs,valeurs*4)
```

Sortie du calcul pédagogique :

```text
98304 393216
```

## CV_01-D2 - Démonstration accompagnée

Appliquer un filtre local et nommer les axes. Cette démonstration est exécutée dans le notebook du chapitre, au repère **CV_01-D2**. Lire les entrées et les contrôles avant de l’exécuter. Le détail des sorties dépend, lorsque des bibliothèques interviennent, des versions et du protocole indiqués dans le carnet.

```python
import numpy as np
image=np.arange(9,dtype=float).reshape(3,3)
kernel=np.array([[1.,0.],[0.,-1.]])
output=np.array([[np.sum(image[i:i+2,j:j+2]*kernel)
                  for j in range(2)] for i in range(2)])
print('Image :',image.tolist())
print('Sortie du filtre :',output.tolist())
batch=np.zeros((8,3,64,64),dtype=np.float32)
print('Axes batch/canaux/hauteur/largeur :',batch.shape)
print('Octets des valeurs seulement :',batch.nbytes)
assert output.shape==(2,2)
print('Le calcul utilise la convention de corrélation croisée des couches usuelles.')
```

Exemple court et autonome de compréhension. Les données sont fabriquées ou intégrées à scikit-learn ; aucune donnée de compétition n’est substituée silencieusement.

## Sortie de référence de D2

```text
Image : [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]
Sortie du filtre : [[-4.0, -4.0], [-4.0, -4.0]]
Axes batch/canaux/hauteur/largeur : (8, 3, 64, 64)
Octets des valeurs seulement : 393216
Le calcul utilise la convention de corrélation croisée des couches usuelles.
```

Exemple exécuté localement sur CPU. Les résultats dépendent du petit jeu, du protocole et des versions consignées ; ils ne sont pas une performance Kaggle.

## Comment examiner la sortie

Vérifier d’abord que le programme répond à la question annoncée. Identifier une valeur, son unité ou son rôle ; expliquer ensuite pourquoi cette observation soutient ou non le raisonnement. Les assertions vérifient des propriétés précises du petit exemple, pas une performance universelle.

## CV_01-E1 - Expliquer

Le nom du fichier train indique chat ou chien. Peut-on utiliser ce nom comme variable d’entrée si les fichiers test portent seulement un numéro ?

## CV_01-E2 - Transférer

Pourquoi faut-il reprendre la normalisation attendue par les poids préentraînés ?

Écrire une réponse et sa justification avant la correction collective. Les réponses aux exercices ne figurent pas dans cette version.

## Reprendre après un blocage

Relever le repère, le message exact et le résultat attendu. Vérifier les cellules précédentes, l’environnement, les types et les dimensions. Refaire le petit calcul avant d’augmenter les données ou la complexité. Si plusieurs personnes sont bloquées, demander une reprise collective.

## CV_01-B - Bilan individuel

- Je sais expliquer les mots du chapitre avec un exemple.
- Je peux justifier une sortie, sans recopier seulement le nombre.
- Je peux citer une limite et la prochaine vérification.

Trace à conserver : une réponse personnelle, une sortie interprétée et une limite. Les modalités de remise ou de notation sont annoncées séparément ; ce chapitre ne crée pas de nouveau barème.

## Erreur fréquente

Confondre axes, entraîner sur les noms de fichiers ou annoncer la mémoire totale à partir de la seule taille du batch.

## La suite du parcours

La dernière séance vérifie le coût, la robustesse et le retour complet de l’inférence image.

## Références techniques

- https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html

Les données de compétition, les modèles préentraînés et les logiciels tiers conservent leurs règles et licences. Les scores des exemples intégrés ou fabriqués ne constituent pas des scores Kaggle.
