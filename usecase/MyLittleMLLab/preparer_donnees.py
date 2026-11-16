"""Placer trois CSV depuis un ZIP Kaggle déjà téléchargé, sans réseau ni identifiants."""
import argparse
import csv
import io
from pathlib import Path
import shutil
import zipfile

NAMES = ('train.csv', 'test.csv', 'sample_submission.csv')
ROOT = Path(__file__).resolve().parent

def prepare(archive, destination=None):
    destination = Path(destination) if destination else ROOT/'data/competitions/playground-series-s6e11'
    with zipfile.ZipFile(archive) as z:
        selected = {}
        for name in NAMES:
            matches = [i for i in z.infolist() if not i.is_dir() and Path(i.filename).name == name]
            if len(matches) != 1:
                raise ValueError(f'{name} : un seul fichier attendu dans le ZIP, trouvé {len(matches)}.')
            selected[name] = matches[0]
        # Vérifier les trois en-têtes avant de toucher aux fichiers du laboratoire.
        headers = {}
        for name, item in selected.items():
            with z.open(item) as raw, io.TextIOWrapper(raw, encoding='utf-8-sig', newline='') as text:
                headers[name] = next(csv.reader(text))
        if 'id' not in headers['train.csv'] or 'is_fraud' not in headers['train.csv']:
            raise ValueError('Le train doit contenir id et is_fraud. Vérifiez la compétition téléchargée.')
        if 'id' not in headers['test.csv'] or 'is_fraud' in headers['test.csv']:
            raise ValueError('Le test doit contenir id, sans is_fraud.')
        if headers['sample_submission.csv'] != ['id', 'is_fraud']:
            raise ValueError('Format attendu pour sample_submission.csv : id,is_fraud.')
        if set(headers['train.csv']) - {'is_fraud'} != set(headers['test.csv']):
            raise ValueError('Colonnes train/test incohérentes.')
        destination.mkdir(parents=True, exist_ok=True)
        for name, item in selected.items():
            # Destination fixe : aucun chemin fourni dans le ZIP n’est extrait.
            with z.open(item) as source, (destination/name).open('wb') as target:
                shutil.copyfileobj(source, target)
            print(f'OK : {name}')
    print(f'Données prêtes dans {destination}')
    return destination

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive', type=Path, help='Chemin du ZIP officiel playground-series-s6e11.zip')
    args = p.parse_args()
    try:
        prepare(args.archive)
    except (OSError, ValueError, zipfile.BadZipFile, StopIteration) as error:
        p.exit(1, f'Données non préparées : {error}\n')
