# J4 — Feuille de travail accompagnée

Travail individuel guidé, avec une réponse écrite à chaque étape. Les exemples miniatures expliquent le mécanisme et ne constituent pas une évaluation Kaggle.

## 1. Deux pas d’apprentissage (20 min)

x=3, cible=1, w0=2. Perte L=(3w−1)². Gradient=2(3w−1)×3. Learning rate=0,01.

Calculer prédiction, perte, gradient et nouveau poids pour deux étapes. Recalculer le gradient au poids courant. Repartir de w=2 et tester learning rate=1. Vérification cellules 5 et 7.

## 2. Le batch entièrement visible (20 min)

X=[[1,0],[0,1],[1,1]], classes=[0,1,1]. Poids de la classe 0 : [0,2 ; −0,1]. Poids de la classe 1 : [−0,3 ; 0,4]. Biais nuls.

1. Calculer les deux logits de chaque observation et leurs formes matricielles.
2. À partir du softmax affiché, choisir la probabilité de la vraie classe.
3. Calculer −log(p) pour chaque ligne puis la moyenne.
4. Après backward, lire un gradient de poids et calculer sa mise à jour SGD au pas 0,1.

Vérification cellules 9, 11 et 13.

## 3. Paramètres et ressources (20 min)

Architecture d entrées, 32 neurones cachés, ReLU, deux logits. Compter les poids et les biais de chaque couche. Refaire avec 16 neurones et d=60. Le batch change-t-il ce nombre ?

10 000 lignes, batch=256, huit epochs : combien de mises à jour ? Puis deux learning rates et trois folds ? Que change un batch=128 ?

## 4. Diagnostic des courbes (20 min)

A : train et validation restent élevés. B : train baisse et validation remonte. C : la perte oscille ou devient non finie. Proposer pour chaque cas une hypothèse, une vérification concrète et une seule modification éventuelle.

## 5. Choisir un modèle (15 min)

Après la cellule 27, distinguer le meilleur learning rate du réseau et le meilleur modèle du tableau. Donner deux chiffres et une limite. Pourquoi une bonne accuracy ne suffit-elle pas sur ces paiements ?

## 6. Early stopping (15 min)

Pertes validation aux epochs 1 à 5 : 0,50 ; 0,35 ; 0,36 ; 0,37 ; 0,38. Patience trois, critère minimal. À quelle epoch arrêter ? Quels poids garder ? Si l’AUC maximale est ailleurs, notre règle l’a-t-elle optimisée ? Comparer à la démonstration réelle cellule 29.

## 7. Transfert et artefacts (20 min)

Associer chaque fichier à son rôle : poids_reseau.pt, pretraitement.joblib, manifest.json, comparaison.csv, submission_J4.csv. Que faut-il comparer entre une exécution locale et une exécution Kaggle ? Quelle vérification fait la cellule 35 ?

## 8. Réparer la boucle (20 min)

Lire sans exécuter ce code incorrect. Réécrire l’apprentissage et la mesure, puis expliquer quatre erreurs.

```python
# Code volontairement incorrect à analyser sur papier.
for xb, yb in batches:
    probs = torch.softmax(net(xb), dim=1)
    loss = criterion(probs, yb)
    optimizer.step()
    loss.backward()
valid_logits = net(x_valid)
```

## 9. Bilan individuel (5 min)

En une phrase chacun : forward, backward, step, zero_grad, validation croisée, prétraitement ajusté. Expliquer ensuite pourquoi le meilleur réseau peut perdre face à la référence.

## Pauses illustrées

Répondre individuellement avant la correction collective. [Retrouver les huit scénarios](PAUSES_POP_CULTURE.md). Pour chaque cas : une prédiction, une justification et le lien avec le notebook.
