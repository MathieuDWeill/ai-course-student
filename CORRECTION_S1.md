# Correction S1 - Logic Over Code

## Idee centrale

Un code qui tourne n'est pas une preuve que le resultat est vrai.

Le but de la seance n'est pas de memoriser pandas.
Le but est de comprendre comment une analyse peut devenir fausse si le grain, les cles ou les jointures ne sont pas verifies.

## Question de depart

Question :

```text
Quel produit se vend le mieux ?
```

Reponse attendue :

```text
Cela depend de la definition de "se vend le mieux".
```

Definitions possibles :

- par quantite vendue ;
- par chiffre d'affaires ;
- par marge ;
- par nombre de commandes.

Point cle :

```text
Mesurable ne veut pas dire pertinent.
```

## NumPy

Calcul :

```python
prices = np.array([12.0, 25.0, 8.0, 40.0])
quantities = np.array([3, 1, 5, 2])
revenue_by_line = prices * quantities
```

Resultat :

```text
[36. 25. 40. 80.]
total = 181.0
mean = 45.25
max = 80.0
```

Mini-challenge TTC :

```python
prices_ttc = prices * 1.20
revenue_ttc = prices_ttc * quantities
```

Resultat :

```text
CA TTC = 217.2
```

## Grain des tables

Reponses attendues :

```text
customers   = une ligne par client
orders      = une ligne par commande
order_lines = une ligne par produit dans une commande
products    = une ligne par produit
```

Table de faits naturelle :

```text
order_lines
```

Pourquoi :

```text
Le chiffre d'affaires se calcule au grain ligne de commande :
quantity x unit_price
```

## Cles

Reponses attendues :

```text
customers.customer_id unique: True
orders.order_id unique: True
products.product_id unique: True
order_lines (order_id, line_id) unique: True
```

## Fait de vente

La table `fact_sales` est construite en joignant :

- `order_lines` ;
- `orders` ;
- `customers` ;
- `products`.

Chaque jointure doit respecter une hypothese de cardinalite.

Resultats de reference :

```text
Rows: 8
Reference revenue: 634
```

Formule :

```python
fact_sales["revenue"] = fact_sales["quantity"] * fact_sales["unit_price"]
```

## Meilleur produit

Reponse attendue :

```text
Le meilleur produit depend de la mesure choisie.
Le leader par quantite peut etre different du leader par chiffre d'affaires.
```

Phrase correcte :

```text
Selon la definition retenue, le meilleur produit n'est pas forcement le meme.
```

## Mauvaise jointure

Resultats attendus :

```text
Rows before: 8 | after: 16
CA before: 634 | after: 1268
Inflation: 2.0 x
```

Interpretation :

```text
La table customer_tags contient plusieurs lignes par client.
La jointure duplique donc les lignes de vente.
Le code fonctionne, mais le resultat est faux.
```

## Controle avec validate

`validate="many_to_one"` permet de faire echouer une hypothese incorrecte.

Dans ce cas, l'hypothese incorrecte est :

```text
Chaque client a une seule ligne dans customer_tags.
```

Cette hypothese est fausse.
Pandas peut donc detecter l'erreur.

Point cle :

```text
Une bonne erreur vaut mieux qu'un mauvais resultat silencieux.
```

## Contrat de donnees minimal

Tous les controles doivent etre vrais :

```text
customer_id_unique: True
order_id_unique: True
product_id_unique: True
order_line_composite_key_unique: True
quantities_positive: True
prices_non_negative: True
fact_rows_preserved: True
```

## Exit ticket

1. Question a poser avant de coder :

```text
Quelle decision veut-on prendre et comment definit-on la mesure ?
```

2. Exemple de proxy trompeur :

```text
La quantite vendue peut etre trompeuse si l'objectif reel est le chiffre d'affaires ou la marge.
```

3. Verification possible :

```text
Le chiffre d'affaires total peut etre verifie en controlant le grain,
les cardinalites, le nombre de lignes avant/apres jointure,
et une somme independante.
```

## A retenir

```text
Avant de calculer, on comprend.
Avant de conclure, on verifie.
Le code qui tourne n'est pas une preuve que le resultat est vrai.
```

