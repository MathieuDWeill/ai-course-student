# AML_C2 — API REST, livraison et suivi MLOps

Conception pédagogique : Mathieu Weill.

## Question et progression

Comment rendre une prédiction appelable, vérifiable et maintenable ?

À placer après AML_06. Durée indicative : 90 minutes, à adapter aux acquis.

Preuve attendue : Appeler /predict, refuser une entrée invalide, tester le rechargement et expliquer une alerte de dérive.

## Le modèle devient un service

Le client envoie du JSON à POST /predict. Le service valide les champs, applique le pipeline sauvegardé et renvoie la prédiction avec sa version.

Nous avons déjà un artefact et son prétraitement. Une API donne un contrat d’échange à un autre programme. REST est un style d’interface fondé sur les ressources et HTTP. Notre exemple utilise une route de prédiction. Une fonction Python appelée dans le notebook ne prouve pas qu’un serveur HTTP fonctionne. Nous testerons les deux : contrat en mémoire, puis serveur local.

Question de vérification : Pourquoi ne pas réentraîner dans /predict ?

## Un contrat vérifiable

Les noms, types, unités et bornes font partie du contrat. Une requête incomplète est refusée ; les champs supplémentaires aussi dans cette démonstration.

La validation évite qu’une largeur négative soit acceptée comme une mesure de fleur. Nos bornes sont pédagogiques et ne remplacent pas une définition métier. Les probabilités sont accompagnées de l’ordre des classes. Sans cet ordre, une liste de nombres est ambiguë. Le service annonce iris-v1 : ce nom désigne une version du système, pas une garantie de qualité.

Question de vérification : Une réponse HTTP 200 prouve-t-elle que la prédiction est juste ?

## CI et livraison contrôlée

La CI réexécute les contrôles à chaque changement. Le déploiement utilise un artefact identifié, des tests et une possibilité de retour à la version précédente.

CI signifie intégration continue. Le fichier fourni installe l’environnement et lance pytest sur un dépôt d’exercice. CD peut désigner livraison continue ou déploiement continu ; ici nous préparons une livraison avec décision humaine. Nous ne publions aucun service Internet automatiquement. Il reste à traiter authentification, HTTPS, secrets, charge et exploitation pour un service réel.

Question de vérification : Si les tests passent, doit-on forcément déployer ?

## Observer, vérifier, revenir en arrière

Suivre la version, la latence et les erreurs techniques. Surveiller les entrées ; mesurer la performance quand les vrais labels arrivent. Prévoir qui décide du retour arrière.

La dérive de données est un changement des entrées. Elle peut signaler un problème de capteur ou une population différente, sans prouver une dégradation du score. Notre alerte compare des moyennes standardisées : c’est une heuristique pédagogique, pas un test statistique universel. Nous ne déclenchons pas un réentraînement automatique. Nous vérifions, récupérons les labels si possible, comparons les versions et gardons un artefact de retour.

Question de vérification : Une distribution stable exclut-elle une baisse de performance ?

## AML_C2-D1 — Tester le contrat REST

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
from pathlib import Path
import sys
lab=Path.cwd().parent/'laboratoire'
assert (lab/'api.py').exists(), 'Conserver les dossiers du kit ensemble.'
sys.path.insert(0,str(lab.resolve()))
from api import app,train_artifact,drift_report
from fastapi.testclient import TestClient
train_artifact()
row=dict(sepal_length=5.1,sepal_width=3.5,petal_length=1.4,petal_width=.2)
with TestClient(app) as client:
 response=client.post('/predict',json=row)
 print(response.status_code,response.json())
 assert response.status_code==200
 assert client.post('/predict',json={}).status_code==422
```

## AML_C2-D2 — Distinguer alerte et performance

Prévoir une sortie, exécuter, puis expliquer une assertion.

```python
import numpy as np
ref=np.array([[0.,1.],[1.,2.],[2.,3.]])
print('Même distribution :',drift_report(ref,ref)['alert'])
print('Décalage :',drift_report(ref,ref+2)['alert'])
assert not drift_report(ref,ref)['alert']
assert drift_report(ref,ref+2)['alert']
```

## Mise en service locale réelle

Dans un terminal ouvert dans `laboratoire`, exécuter :

```bash
python api.py
python -m pytest -q
python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

Garder le serveur ouvert. Dans le navigateur, ouvrir **http://127.0.0.1:8000/docs**. Déplier POST /predict, cliquer Try it out puis envoyer les quatre mesures de D1. Vérifier la réponse et le code 200. Retirer un champ : observer le refus 422. Arrêter le serveur avec Ctrl+C.

La démonstration du notebook emploie TestClient sans réseau ; cette étape vérifie un vrai serveur local. Le pipeline reste celui sauvegardé. Ne charger aucun fichier joblib inconnu.

## Mise en pratique CI et maintenance

Copier le contenu de `laboratoire` à la racine d’un dépôt d’exercice personnel, y compris `.github/workflows/ci.yml`. Au prochain push, observer la tâche de tests dans Actions. Dans une branche, modifier une assertion pour la rendre fausse, observer l’échec, puis la corriger. Le service ne se déploie pas automatiquement. La CI du dépôt de cours contrôle aussi le laboratoire.

Conserver `runs/model.joblib` avec son environnement et sa version. Comparer les contrôles avant une nouvelle version. Tenir une fiche : indicateur, seuil, fréquence, responsable, action et version de retour. Le journal local mesure version, classe et latence ; il ne constitue pas une plateforme de supervision de production.

## Sorties résolues et limites

Ces refus sont réellement testés. La requête valide donne setosa avec une probabilité proche de 0,981 dans notre exécution. Les probabilités sont dans l’ordre setosa, versicolor, virginica. La latence varie ; ne pas la traiter comme une constante du modèle. TestClient ne traverse pas le réseau ; le serveur localhost a aussi été vérifié séparément.

## AML_C2-E — Exercice individuel

La latence double, les entrées changent et les labels ne sont pas encore connus. Que peut-on affirmer ? Quelles actions mener avant de remplacer le modèle ?

Écrire une réponse justifiée avant la correction collective.

## Bilan

Appeler /predict, refuser une entrée invalide, tester le rechargement et expliquer une alerte de dérive.

Une sortie expliquée : …

Une limite : …

Une prochaine vérification : …

## Références

- https://fastapi.tiangolo.com/tutorial/testing/
- https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python
