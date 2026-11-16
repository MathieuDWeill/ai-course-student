"""Vérification du laboratoire J1 sans entraînement ni soumission."""
from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parent

def main():
    missing = []
    for module in ['numpy', 'pandas', 'sklearn', 'matplotlib', 'jupyterlab', 'ipykernel', 'nbformat', 'nbclient', 'psutil']:
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(module)
    if missing:
        print('Dépendances manquantes :', ', '.join(missing))
        print('Installez requirements.txt avec le Python de .venv, puis relancez ce script.')
        return 1
    from mllab.competition import read_competition
    try:
        train, test, sample = read_competition('fraud')
    except (OSError, ValueError) as error:
        print(error)
        print('Voir README.md, étape 3 : récupération des données Kaggle.')
        return 1
    notebook = ROOT/'notebooks/AML_01_atelier.ipynb'
    if not notebook.is_file():
        print('Notebook absent : récupérez le kit complet.')
        return 1
    print('Python :', sys.version.split()[0])
    print('Données train / test :', train.shape, '/', test.shape)
    print('PRÊT POUR J1 : ouvrez notebooks/AML_01_atelier.ipynb dans JupyterLab.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
