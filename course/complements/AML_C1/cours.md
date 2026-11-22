# AML_C1 — CNN : du filtre au classifieur

Conception pédagogique : Mathieu Weill.

## Question et progression

Comment un réseau exploite-t-il la structure spatiale d’une image ?

À placer après AML_04. Durée indicative : 45 minutes, à adapter aux acquis.

Preuve attendue : Expliquer les dimensions d’une convolution et entraîner un petit CNN sur des chiffres intégrés.

## Les pixels ont des voisins

Une image est un tenseur. Un CNN applique les mêmes paramètres à plusieurs positions pour rechercher un motif local.

Nous réutilisons la boucle de J4 : prédiction, perte, gradient et mise à jour. Ce qui change est l’architecture. Un filtre parcourt des voisinages ; le partage des poids réduit le nombre de paramètres par rapport à une couche dense sur tous les pixels. Le réseau apprend les filtres. Un filtre fixé à la main aide à comprendre le calcul mais ne constitue pas un entraînement.

Question de vérification : La boucle d’apprentissage change-t-elle avec une convolution ?

## La forme d’une convolution

Pour une dimension spatiale : sortie = partie entière de (entrée + 2 × padding − dilation × (noyau − 1) − 1) / stride + 1.

Prenons une image de huit par huit, un noyau de trois, un pas de un et un padding de un. Nous conservons huit par huit. Avec huit filtres nous obtenons huit cartes. Le batch reste un axe séparé. Un MaxPool de deux réduit ensuite huit par huit à quatre par quatre. Nous annonçons les formes avant de lire les sorties.

Question de vérification : Après Conv2d(1,8,3,padding=1), quelle forme pour un batch de 16 images 8 × 8 ?

## ResNet et EfficientNet

ResNet utilise des connexions résiduelles. EfficientNet étudie un équilibrage de profondeur, largeur et résolution. Le préentraînement ne dispense pas d’évaluation locale.

Une connexion résiduelle permet d’ajouter une représentation transformée à une représentation compatible. Les dimensions doivent être adaptées si elles diffèrent. EfficientNet ne signifie pas meilleur sur tout matériel : le temps mesuré dépend de l’architecture, du batch et de la machine. Les ateliers vision utilisent ResNet ; ce complément fait le lien entre l’architecture et les notions de ML avancé.

Question de vérification : Un modèle plus petit est-il nécessairement plus rapide sur notre machine ?

## Le score décrit un protocole

Séparer les données avant l’apprentissage. Entraîner sur train, mesurer sur les observations réservées et consigner le budget.

Notre jeu de chiffres est intégré à scikit-learn. Ce ne sont pas les données Kaggle de chiens et chats. Nous allons faire deux epochs sur CPU pour lire la chaîne complète, sans chercher un record. Un bon résultat sur des chiffres de huit par huit ne prouve pas une robustesse sur des photos réelles ni une généralisation à de nouveaux auteurs.

Question de vérification : Le test aléatoire garantit-il une performance sur un nouveau style d’écriture ?

## AML_C1-D1 — Vérifier une convolution

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
import torch
from torch import nn
torch.set_num_threads(2);torch.manual_seed(42)
x=torch.arange(9,dtype=torch.float32).reshape(1,1,3,3)
conv=nn.Conv2d(1,1,2,bias=False)
with torch.no_grad():conv.weight.fill_(1)
z=conv(x)
print(z.flatten().tolist())
assert z.flatten().tolist()==[8.,12.,20.,24.]
```

## AML_C1-D2 — Entraîner un CNN réel sur digits

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset,DataLoader
X,y=load_digits(return_X_y=True)
a,b=train_test_split(range(len(y)),test_size=.25,stratify=y,random_state=42)
X=torch.tensor(X.reshape(-1,1,8,8)/16,dtype=torch.float32)
y=torch.tensor(y,dtype=torch.long)
net=nn.Sequential(nn.Conv2d(1,8,3,padding=1),nn.ReLU(),
 nn.MaxPool2d(2),nn.Flatten(),nn.Linear(8*4*4,10))
loader=DataLoader(TensorDataset(X[a],y[a]),batch_size=64,shuffle=True)
opt=torch.optim.Adam(net.parameters(),lr=.01)
for epoch in range(2):
 net.train()
 for xb,yb in loader:
  opt.zero_grad();loss=nn.functional.cross_entropy(net(xb),yb)
  loss.backward();opt.step()
net.eval()
with torch.no_grad():accuracy=(net(X[b]).argmax(1)==y[b]).float().mean().item()
print('Test digits, deux epochs :',round(accuracy,3))
assert net(X[b[:2]]).shape==(2,10)
```

## Sorties résolues et limites

Le calcul fixé de convolution donne 8, 12, 20 et 24. Le réseau entraîné sur digits obtient 0,878 sur la partition réservée lors de notre exécution CPU de deux epochs. Ce chiffre décrit ce protocole et ne constitue pas une cible à recopier. La forme des logits est batch par dix classes.

## AML_C1-E — Exercice individuel

Après huit filtres et un pooling 2 × 2 sur des images 8 × 8, combien de valeurs entrent dans la couche dense ? Pourquoi cela ne donne-t-il pas le nombre de paramètres du réseau ?

Écrire une réponse justifiée avant la correction collective.

## Bilan

Expliquer les dimensions d’une convolution et entraîner un petit CNN sur des chiffres intégrés.

Une sortie expliquée : …

Une limite : …

Une prochaine vérification : …

## Références

- https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html
- https://docs.pytorch.org/vision/stable/models.html
