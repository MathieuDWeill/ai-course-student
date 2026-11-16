"""Télécharger les poids autorisés avant la séance, sur la machine qui les utilisera."""
import argparse,hashlib,json
from pathlib import Path
from .core import ROOT,write_json
p=argparse.ArgumentParser();p.add_argument('--text',action='store_true');p.add_argument('--vision',action='store_true');a=p.parse_args()
manifest={}
if a.text:
    from .deep import setup,load_text_model
    setup();tok,model=load_text_model(allow_download=True)
    manifest['text']={'model':'prajjwal1/bert-tiny','revision':getattr(model.config,'_commit_hash',None),'language':'anglais','note':'Tête de classification initialisée ; encoder préentraîné. Vérifier la licence du modèle avant redistribution.'}
if a.vision:
    import torch
    from torchvision.models import resnet18,ResNet18_Weights
    w=ResNet18_Weights.DEFAULT;resnet18(weights=w)
    path=Path(torch.hub.get_dir())/'checkpoints'/Path(w.url).name
    manifest['vision']={'architecture':'resnet18','weights':str(w),'url':w.url,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
if not manifest:p.error('Choisir --text et/ou --vision')
out=ROOT/'runs/asset_preparation';out.mkdir(parents=True,exist_ok=True);write_json(out/'manifest.json',manifest);print(json.dumps(manifest,indent=2))
