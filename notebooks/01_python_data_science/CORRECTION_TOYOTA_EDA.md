# Correction - Toyota EDA Lab

Cette correction correspond aux cellules `Your code goes here` de `EDA_Toyota.ipynb`.

## Préparation

Le notebook charge :

```python
path = "Dataset/Toyota.csv"
df = pd.read_csv(path)
```

Résultat attendu au départ :

```text
1446 lignes, 10 colonnes
```

## Cellule 13 - Afficher les 10 premières lignes

```python
df.head(n=10)
```

## Cellule 17 - Afficher les 8 dernières lignes

```python
df.tail(n=8)
```

## Cellule 24 - Types des colonnes

```python
df.dtypes
```

## Cellule 28 - Explorer `FuelType`

```python
df["FuelType"]
df["FuelType"][0:20]
```

## Cellule 30 - Valeurs uniques de `FuelType`

```python
df["FuelType"].unique()
```

Valeurs observées avant nettoyage :

```text
Petrol, petrol, CNG, Diesel, diesel, CompressedNaturalGas, methane
```

## Cellule 32 - Nettoyer `FuelType`

```python
petrol_boolean = df["FuelType"] == "petrol"
df.loc[petrol_boolean, "FuelType"] = "Petrol"

df.loc[df["FuelType"] == "diesel", "FuelType"] = "Diesel"
df.loc[df["FuelType"].isin(["CompressedNaturalGas", "methane"]), "FuelType"] = "CNG"
```

## Cellule 35 - Vérifier `FuelType`

```python
df["FuelType"].unique()
```

Résultat attendu :

```text
Petrol, CNG, Diesel
```

## Cellule 37 - Afficher les valeurs manquantes

```python
df.isnull()
```

## Cellule 39 - Compter les valeurs manquantes

```python
df.isnull().sum()
```

Résultat attendu :

```text
Price       7
Age         5
KM          6
FuelType    0
HP          0
MetColor    0
Automatic   0
CC          0
Doors       0
Weight      0
```

## Cellule 43 - Nombre de lignes avant suppression

```python
df.shape
```

Résultat attendu :

```text
(1446, 10)
```

Le notebook supprime ensuite les lignes incomplètes :

```python
df.dropna(axis=0, how="any", inplace=True)
```

## Cellule 47 - Nombre de lignes après suppression

```python
df.shape
```

Résultat attendu :

```text
(1436, 10)
```

## Cellule 51 - Distribution du prix

```python
bins = np.arange(0, 33000, 1000)
df["Price"].plot(kind="hist", bins=bins)
plt.xlabel("Price")
plt.title("Distribution of Toyota prices")
```

## Cellule 54 - Distribution de l'âge

```python
bins = np.arange(0, 81, 1)
df["Age"].plot(kind="hist", bins=bins)
plt.xlabel("Age in months")
plt.title("Distribution of car age")
```

## Cellule 56 - Relation âge / prix

```python
df.plot(kind="scatter", x="Age", y="Price")
plt.title("Price by age")
```

Interprétation attendue :

```text
Plus la voiture est âgée, plus le prix tend à baisser.
```

## Cellule 63 - Valeurs uniques de `MetColor`

```python
df["MetColor"].unique()
```

Résultat attendu :

```text
0 et 1
```

## Cellule 66 - Prix moyen par couleur métallisée

```python
df.groupby("MetColor")["Price"].mean()
```

Résultat indicatif :

```text
MetColor = 0 : environ 10162
MetColor = 1 : environ 11005
```

## Cellule 68 - Boxplot prix / couleur métallisée

```python
df.boxplot(by="MetColor", column="Price", showmeans=True)
plt.title("Price by metallic color")
plt.suptitle("")
```

## Cellule 73 - Valeurs uniques de `Doors`

```python
df["Doors"].unique()
```

Résultat avant recodage :

```text
2, 3, 4, 5
```

Le notebook recode ensuite :

```python
df["Doors"].replace([2, 3, 4, 5], [0, 0, 1, 1], inplace=True)
```

Interprétation :

```text
0 = 3 portes
1 = 5 portes
```

## Cellule 99 - Distribution de `FuelType`

```python
df["FuelType"].value_counts()
df["FuelType"].value_counts().plot(kind="bar")
plt.title("Fuel type distribution")
```

Résultat indicatif :

```text
Petrol : 1264
Diesel : 155
CNG    : 17
```

## Cellule 104 - Matrice de corrélation

```python
features = ["Price", "Age", "KM", "Weight", "CC", "HP"]
df[features].corr()
```

Points clés :

```text
Age est fortement négativement corrélé au prix.
Weight est positivement corrélé au prix.
KM est négativement corrélé au prix.
```

## Cellule 111 - Corrélation pour Petrol

```python
features = ["Price", "Age", "KM", "Weight", "CC", "HP"]
df[df["FuelType"] == "Petrol"][features].corr()
```

Version heatmap :

```python
sns.heatmap(
    df[df["FuelType"] == "Petrol"][features].corr(),
    annot=True,
    center=0,
    cmap="BrBG",
)
```

## Cellule 113 - Corrélation pour Diesel

```python
features = ["Price", "Age", "KM", "Weight", "CC", "HP"]
df[df["FuelType"] == "Diesel"][features].corr()
```

Version heatmap :

```python
sns.heatmap(
    df[df["FuelType"] == "Diesel"][features].corr(),
    annot=True,
    center=0,
    cmap="BrBG",
)
```

## Cellule 119 - Weight / Price coloré par carburant

```python
sns.lmplot(
    x="Weight",
    y="Price",
    hue="FuelType",
    data=df,
    fit_reg=False,
    scatter_kws={"alpha": 0.8, "s": 8},
    height=6,
    aspect=1.5,
)
```

## Cellule 123 - HP / Price

Exercice A :

```python
plt.figure()
sns.lmplot(
    x="HP",
    y="Price",
    hue="FuelType",
    data=df,
    fit_reg=False,
    scatter_kws={"alpha": 0.8, "s": 8},
    height=6,
    aspect=1.5,
)
```

Exercice B :

```python
plt.figure()
sns.boxplot(x="FuelType", y="HP", data=df, showmeans=True)
plt.title("Horsepower by fuel type")
```

## Cellule 127 - Synthèse EDA

Points possibles :

```text
Data insight:
- Age est le signal le plus fort pour expliquer Price.
- KM diminue généralement le prix.
- FuelType change les relations entre HP, Weight, KM et Price.
- CNG est très minoritaire, donc les conclusions sur CNG sont fragiles.

Data summary:
- 10 lignes contiennent des valeurs manquantes.
- FuelType devait être standardisé.
- Doors contenait des valeurs incohérentes métier.
- Petrol domine fortement le dataset.

Outliers:
- Certaines voitures très chères méritent une vérification.
- Certains poids semblent atypiques.
- Les segments Diesel/CNG doivent être interprétés séparément.

Dataset ready for modeling:
- FuelType nettoyé.
- Lignes incomplètes supprimées.
- Doors recodé en variable binaire.
- Encodage one-hot et standardisation possibles avant modélisation.
```

## Cellule 142 - Afficher l'encodage one-hot

```python
df_ohe.head(15)
```

Colonnes attendues :

```text
FuelType_CNG
FuelType_Diesel
FuelType_Petrol
```

## Cellule 146 - Afficher le dataset standardisé

```python
df_ohe_scaled.head(15)
```

Interprétation :

```text
Age, KM, HP, CC et Weight sont centrées-réduites.
Les variables binaires restent en 0/1 ou True/False.
```

## Message pédagogique

Le but du lab n'est pas seulement de tracer des graphiques.

Le vrai objectif est :

```text
nettoyer les incohérences,
comprendre les distributions,
repérer les variables utiles,
identifier les limites du dataset,
préparer une base fiable pour un modèle.
```

