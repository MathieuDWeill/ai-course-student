"""Paquet de code pour CPU/GPU Kaggle ; données officielles jointes séparément."""
from pathlib import Path
import argparse,json,zipfile
from .core import ROOT
from .competition import SPECS

def export_runner(key,mode,output,limit=1000,epochs=2):
    allowed={'fraud':{'linear','boosting','neural'},'tweets':{'linear','frozen','finetune'},'catsdogs':{'head','partial'}}
    if key not in allowed or mode not in allowed[key]:raise ValueError('Mode incompatible avec la tâche')
    cfg={'key':key,'mode':mode,'limit':limit,'epochs':epochs,'slug':SPECS[key]['slug']}
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
        for p in (ROOT/'mllab').glob('*.py'):z.write(p,'mllab/'+p.name)
        for name in ['requirements.txt','requirements-deep.txt']:z.write(ROOT/name,name)
        z.writestr('remote_config.json',json.dumps(cfg,indent=2))
        z.writestr('run_remote.py',"""import json
from mllab.core import pack_run
from mllab.competition import run_competition,neural_competition
c=json.load(open('remote_config.json'));key=c['key'];mode=c['mode']
if key=='fraud' and mode=='neural':p,s,h=neural_competition(limit=c['limit'],epochs=c['epochs'])
elif key=='tweets' and mode in ('frozen','finetune'):
 from mllab.text_competition import run_text
 p,s,h=run_text(limit=c['limit'],mode=mode,epochs=c['epochs'],allow_download=False)
elif key=='catsdogs':
 from mllab.vision_competition import run_images
 p,s,h=run_images(limit=c['limit'],mode=mode,epochs=c['epochs'],augment=True,allow_download=False)
else:p,s,m=run_competition(key,model=mode,limit=c['limit'])
print(s);pack_run(p,'result.zip')
""")
    return Path(output)

def main():
    p=argparse.ArgumentParser();p.add_argument('--key',choices=SPECS,required=True);p.add_argument('--mode',required=True);p.add_argument('--limit',type=int,default=1000);p.add_argument('--epochs',type=int,default=2);p.add_argument('--output',type=Path,default=Path('runner.zip'));a=p.parse_args();print(export_runner(a.key,a.mode,a.output,a.limit,a.epochs))
if __name__=='__main__':main()
