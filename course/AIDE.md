# Reprendre après un blocage

Conception pédagogique : Mathieu Weill.

## Identifier le problème

1. Noter le nom du notebook et la cellule concernée.
2. Copier le message d’erreur complet, sans identifiant, token ou donnée confidentielle.
3. Décrire ce qui était attendu et ce qui est observé.
4. Vérifier que les cellules précédentes ont été exécutées dans l’ordre.

## Vérifications fréquentes

| Symptôme | Première vérification | Reprise |
|---|---|---|
| Fichier introuvable | Emplacement et nom exact du fichier | Utiliser l’arborescence du guide ; ne pas inventer des données de remplacement. |
| Module introuvable | Environnement et noyau du notebook | Installer avec le Python prévu par le guide, puis redémarrer le noyau. |
| Variable non définie | Cellules exécutées et état du noyau | Repartir de la cellule d’installation/import ; relancer dans l’ordre. |
| Mauvaises dimensions | Forme des entrées, nombre de lignes, axes | Afficher les dimensions sur une petite entrée avant l’entraînement. |
| Calcul trop long | Taille des données et budget lancé | Utiliser le profil court prévu ; demander avant de lancer plusieurs recherches. |
| Résultat différent | Split, versions, seed et paramètres | Documenter l’écart ; une sortie de référence n’est pas un nombre à recopier. |

## Demander de l’aide utilement

« Je suis dans ce notebook, à cette cellule. Je voulais obtenir ceci. Voici le message exact. J’ai vérifié ce point. » Montrer le code et les dernières lignes utiles, pas uniquement « ça ne marche pas ».

Si plusieurs personnes bloquent au même endroit, le signaler pour une reprise collective. Si le problème matériel dure, suivre la démonstration projetée et noter le raisonnement ; reprendre la manipulation une fois l’installation réparée.

[Catalogue](CATALOGUE.md)
