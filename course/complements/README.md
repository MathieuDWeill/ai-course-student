# Compléments du parcours IA

Conception pédagogique : Mathieu Weill.

- [PY_C1 — Clustering hiérarchique et responsabilité](PY_C1/README.md), après PY_05, 45 min indicatives.
- [AML_C1 — CNN : du filtre au classifieur](AML_C1/README.md), après AML_04, 45 min indicatives.
- [AML_C2 — API REST, livraison et suivi MLOps](AML_C2/README.md), après AML_06, 90 min indicatives.
- [NLP_C1 — GPT, résumé et assistant documentaire](NLP_C1/README.md), après NLP_02, 75 min indicatives.
- [CV_C1 — Détection et segmentation](CV_C1/README.md), après CV_01, 60 min indicatives.
- [MM_C1 — Application texte-image et audit final](MM_C1/README.md), après CV_02, 60 min indicatives.

## Installer sans modifier son ancien atelier

Extraire le kit dans un nouveau dossier. Conserver tous les dossiers côte à côte. Python 3.12 recommandé ; CPU suffisant pour les exemples. Créer un environnement séparé.

Windows PowerShell :

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r laboratoire/requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

macOS/Linux :

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r laboratoire/requirements.txt
.venv/bin/python -m jupyter lab
```

Pour CNN, génération et vision : remplacer `requirements.txt` par `requirements-ia.txt` lors de l’installation. Pour lancer un script ensuite, utiliser le Python de cet environnement (ou l’activer). Sur un matériel sans roue PyTorch compatible, préparer une exécution Kaggle CPU avec les mêmes fichiers et consigner le changement d’environnement. L’interface Streamlit est destinée à une exécution locale.

Internet est nécessaire à l’installation et au premier téléchargement des poids. Les exemples centraux n’exigent ni clé API ni abonnement. Les extensions préentraînées demandent espace disque et mémoire supplémentaires ; préparer les téléchargements avant le cours. Les scripts n’envoient pas de requête à une API commerciale et ne publient pas de service sur Internet.

## Organisation

Les exercices étudiants sont sans corrigés. Les exemples résolus et assertions sont des éléments du cours. Chaque module relie cours, notebook et présentation avec D1/D2/E. Les compléments prolongent le catalogue ; ils ne remplacent pas les ateliers Kaggle existants.

Les poids et jeux de données tiers restent soumis à leurs licences. Utiliser des images et textes autorisés, sans données personnelles sensibles. Les supports pédagogiques portent la mention Mathieu Weill et les droits du parcours ; les licences tierces demeurent applicables.

[Ce qui a été vérifié et ses limites](VERIFICATION.md).
