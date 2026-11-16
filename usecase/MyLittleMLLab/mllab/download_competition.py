"""Aide au téléchargement explicite. N'accepte jamais les règles à votre place."""
from pathlib import Path
import argparse,subprocess,zipfile
from .core import ROOT
from .competition import SPECS,get_folder
p=argparse.ArgumentParser();p.add_argument('key',choices=SPECS);a=p.parse_args();spec=SPECS[a.key];folder=get_folder(a.key);folder.mkdir(parents=True,exist_ok=True)
print('Lire les règles et accepter personnellement sur',spec['url'])
print('Aucune soumission ne sera effectuée. Destination privée locale :',folder)
subprocess.run(['kaggle','competitions','download','-c',spec['slug'],'-p',str(folder)],check=True)
archive=folder/(spec['slug']+'.zip')
if archive.exists():
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            f=Path(name)
            if f.is_absolute() or '..' in f.parts:raise ValueError('Chemin archive invalide')
        z.extractall(folder)
print('Téléchargement terminé. Pour catsdogs : extraire également train.zip et test.zip dans train/ et test/.')
