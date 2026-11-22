# MM_C1 — Application texte-image et audit final

Conception pédagogique : Mathieu Weill.

## Question et progression

Comment assembler une application multimodale sans confondre ses erreurs et celles de chaque brique ?

À placer après CV_02. Durée indicative : 60 minutes, à adapter aux acquis.

Preuve attendue : Montrer comment texte et image influencent le résultat, comparer aux ablations et documenter un risque.

## Une fusion tardive explicite

Image → détecteur → labels. Question texte + labels prédits → recherche dans un catalogue. Le résultat dépend des deux modalités.

Combiner texte et image ne signifie pas nécessairement entraîner un grand modèle multimodal. Notre application utilise une fusion tardive : une brique transforme l’image en labels, une autre combine ces labels et la requête. Cette architecture est limitée mais compréhensible. Elle ne calcule pas une représentation jointe apprise comme CLIP et ne décrit pas toutes les relations visibles dans l’image.

Question de vérification : Une application multimodale exige-t-elle un seul réseau de bout en bout ?

## Comparer les ablations

Évaluer texte seul, image seule et combinaison sur les mêmes cas. Conserver les résultats par cas, pas seulement une moyenne.

Une ablation enlève une brique pour mesurer sa contribution. Si le texte suffit déjà à toutes les requêtes, l’image peut ajouter du coût sans valeur. Si le détecteur se trompe, sa mauvaise étiquette peut dominer la recherche. Nous choisissons des requêtes ambiguës où l’image aide, et des requêtes explicites où elle peut au contraire perturber le résultat. Le bon constat peut être que la fusion n’améliore pas ce jeu de cas.

Question de vérification : Si le système combiné réussit, peut-on conclure que les deux modalités sont utiles ?

## Une matrice d’essai avant la soutenance

Préparer des cas normaux, ambigus, hors domaine et contradictoires. Pour chacun : résultat attendu, sortie obtenue et action après erreur.

Un test contradictoire peut demander un catalogue transport avec une photo d’animal. Notre système doit montrer cette contradiction plutôt que prétendre comprendre l’intention. Nous conservons les versions des poids, l’image autorisée, la requête et les sorties. Nous notons aussi temps, mémoire et limites de vocabulaire. Les quatre catégories du catalogue sont fabriquées pour le cours ; elles ne sont pas une compétition Kaggle supplémentaire.

Question de vérification : Que faut-il montrer en plus d’une démonstration qui marche une fois ?

## La fiche éthique est une décision d’usage

Préciser données autorisées, personnes concernées, risques, limites, intervention humaine et règle de retrait. Une simple liste de valeurs ne suffit pas.

Prenons une photo contenant une personne : nous ne devons pas déduire des caractéristiques sensibles pour enrichir une réponse. Un catalogue mal représenté peut exclure certains usages. Nous décrivons qui sera affecté par une erreur et ce que l’application doit refuser. Le rapport final relie une erreur constatée à une mesure concrète, par exemple ne pas utiliser l’outil pour une décision de sécurité et prévoir une vérification humaine.

Question de vérification : Une mention « peut se tromper » suffit-elle pour un usage à fort impact ?

## MM_C1-D1 — Lire une fusion tardive

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
from pathlib import Path
import sys
lab=Path.cwd().parent/'laboratoire'
sys.path.insert(0,str(lab.resolve()))
from vision import retrieve
# Entrée fabriquée pour expliquer la fusion, pas sortie d’un détecteur.
report={'detections':[{'label':'dog'}]}
r=retrieve('animal domestique',report)
print(r['ranking'])
assert r['ranking'][0][0]=='dog'
```

## MM_C1-D2 — Comparer une ablation

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
text_only=retrieve('animal domestique',{'detections':[]})
combined=retrieve('animal domestique',report)
print('Texte seul :',text_only['ranking'])
print('Texte et label visuel :',combined['ranking'])
print('Limite : un seul cas fabriqué ne mesure pas le gain général de la fusion.')
assert len(combined['ranking'])==4
```

## Application complète sur une image réelle

Réutiliser l’environnement et les poids de CV_C1. Dans `laboratoire` :

```bash
python vision.py chemin/vers/image.jpg --download-and-run --query "animal domestique"
```

Le terminal montre les prédictions visuelles et le classement du catalogue. Remplacer la requête, puis l’image, en gardant l’autre entrée fixe. Une interface locale est également fournie :

```bash
python -m pip install "streamlit>=1.40,<2"
python -m streamlit run app_multimodal.py
```

Ouvrir l’adresse locale affichée. Importer une image autorisée, saisir une requête et cliquer Analyser. Le premier calcul peut télécharger des poids. L’interface affiche le classement combiné et les deux ablations. Aucun fichier n’est envoyé à un service d’IA distant par ce code ; les téléchargements de poids nécessitent Internet.

## Remise de l’application

Conserver le code, les versions, quatre cas documentés et les résultats texte seul/image seule/combinaison, une mesure de durée et une fiche de limites. Le rapport éthique décrit un risque concret, les personnes affectées, une mesure de réduction et un usage exclu. Présenter une réussite et un échec, puis justifier l’action après cet échec. Ce complément ne modifie pas les barèmes déjà annoncés.

## Sorties résolues et limites

Le texte animal domestique laisse dog et cat à égalité. L’ajout du label dog favorise cette catégorie. L’ordre d’un classement peut masquer une égalité : le premier élément du texte seul n’est pas une victoire du modèle. Le score est une similarité TF-IDF, pas une probabilité. Une erreur du détecteur peut faire basculer la recherche dans le mauvais sens.

## MM_C1-E — Exercice individuel

Préparer quatre cas d’essai, dont un contradictoire, puis expliquer comment une erreur du détecteur se propage à la réponse finale. Quelle action limite son impact ?

Écrire une réponse justifiée avant la correction collective.

## Bilan

Montrer comment texte et image influencent le résultat, comparer aux ablations et documenter un risque.

Une sortie expliquée : …

Une limite : …

Une prochaine vérification : …

## Références

- https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
- https://docs.pytorch.org/vision/stable/models.html
