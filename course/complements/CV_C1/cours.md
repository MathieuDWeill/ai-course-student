# CV_C1 — Détection et segmentation

Conception pédagogique : Mathieu Weill.

## Question et progression

Quelle différence entre reconnaître une image, localiser un objet et attribuer une classe à ses pixels ?

À placer après CV_01. Durée indicative : 60 minutes, à adapter aux acquis.

Preuve attendue : Distinguer les sorties et calculer une IoU, puis lire des inférences préentraînées sans les présenter comme des annotations.

## Trois tâches, trois annotations

Classification : classe de l’image. Détection : boîtes et classes des objets. Segmentation sémantique : classe de chaque pixel.

Une image peut contenir un chien et un chat. Une classification globale ne dit pas où ils sont. La détection fournit des boîtes, classes et scores. La segmentation sémantique décrit les pixels, mais ne sépare pas forcément deux individus d’une même classe. La segmentation d’instances attribue un masque à chaque objet identifié. Ces tâches demandent des annotations et métriques différentes.

Question de vérification : Un masque sémantique distingue-t-il forcément deux chiens qui se touchent ?

## Les coordonnées d’une boîte

Une boîte peut s’écrire (xmin, ymin, xmax, ymax). Vérifier l’ordre, le repère et le redimensionnement avant de la dessiner.

Le coin supérieur gauche de l’image définit souvent l’origine. Notre détecteur renvoie les coordonnées dans l’image qui lui est fournie. Si nous réduisons l’image, nous devons conserver ce repère pour afficher les boîtes. Le score n’est pas une garantie universelle de correction ; le seuil retenu modifie ce qui est affiché.

Question de vérification : Pourquoi une boîte peut-elle sembler décalée sur l’image originale ?

## L’intersection sur union

IoU = surface de l’intersection / surface de l’union. Elle vaut 1 pour des régions identiques et 0 pour des régions disjointes de surface non nulle.

Pour deux boîtes, calculons d’abord leur intersection. L’union est la somme de leurs surfaces moins l’intersection. Cette mesure ne suffit pas à évaluer un détecteur complet : il faut aussi la classe, les scores, l’appariement des prédictions aux vérités terrain et un protocole tel que mAP. Pour la segmentation, nous pouvons calculer l’IoU par classe puis annoncer la règle de moyenne et le traitement des classes absentes.

Question de vérification : Une boîte correcte sur un objet suffit-elle à annoncer une mAP ?

## Une inférence n’est pas une évaluation

Le laboratoire fournit SSDLite pour la détection et LRASPP pour la segmentation. Les poids et les transformations sont associés au modèle.

Nous utilisons de vrais modèles préentraînés, pas des boîtes dessinées à la main pour imiter leurs sorties. L’exécution télécharge des poids à la demande et sauvegarde les résultats. Sans annotation de référence, nous pouvons inspecter des erreurs visibles mais pas annoncer une qualité chiffrée sur notre domaine. Les classes disponibles sont celles des poids utilisés ; un objet absent de ce vocabulaire ne peut pas être reconnu comme une nouvelle classe.

Question de vérification : Le modèle peut-il reconnaître n’importe quel objet nommé par l’utilisateur ?

## CV_C1-D1 — Calculer une IoU de boîtes

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
def box_iou(a,b):
 inter=max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
 sa=(a[2]-a[0])*(a[3]-a[1]);sb=(b[2]-b[0])*(b[3]-b[1])
 return inter/(sa+sb-inter)
iou=box_iou([0,0,4,4],[2,0,6,4])
print('IoU :',round(iou,3))
assert abs(iou-1/3)<1e-8
```

## CV_C1-D2 — Calculer une IoU de masque

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
import numpy as np
truth=np.array([[1,1],[0,0]],dtype=bool)
pred=np.array([[1,0],[1,0]],dtype=bool)
inter=np.logical_and(truth,pred).sum();union=np.logical_or(truth,pred).sum()
print('IoU classe positive :',round(float(inter/union),3))
assert inter==1 and union==3
```

## Détection et segmentation réelles

Dans `laboratoire`, préparer une image autorisée dont on connaît le contenu, puis lancer :

```bash
python vision.py chemin/vers/image.jpg --download-and-run
```

Le premier lancement télécharge les poids SSDLite et LRASPP. Le dossier `runs/vision` reçoit `detections.png`, le masque de classes `mask.png` et `report.json`. Le masque brut contient des indices de classes, pas une image couleur lisible. Le rapport donne les classes présentes et la forme du masque.

Vérifier les objets manqués et les faux positifs. Pour mesurer une IoU réelle, annoter d’abord la référence ; ne pas prendre les prédictions comme vérité terrain. Le code réduit la résolution pour limiter la mémoire. Préparer les poids avant la séance ; sans eux, limiter le bilan aux calculs de D1/D2.

## Sorties résolues et limites

Sur l’image dog.jpg du dépôt pytorch/hub, le détecteur réel trouve dog avec un score d’environ 0,814. Le masque prédit contient fond et dog. Ce sont des sorties observées sans annotation indépendante : nous n’annonçons ni mAP ni IoU réelle. Les valeurs du tableau sont au contraire celles de régions fabriquées dont nous connaissons la référence.

## CV_C1-E — Exercice individuel

Un modèle affiche un score 0,95 sur une boîte qui entoure la mauvaise espèce. Quelles informations faut-il pour l’évaluer ? Distinguer segmentation sémantique et d’instances.

Écrire une réponse justifiée avant la correction collective.

## Bilan

Distinguer les sorties et calculer une IoU, puis lire des inférences préentraînées sans les présenter comme des annotations.

Une sortie expliquée : …

Une limite : …

Une prochaine vérification : …

## Références

- https://docs.pytorch.org/vision/stable/models.html
- https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html
