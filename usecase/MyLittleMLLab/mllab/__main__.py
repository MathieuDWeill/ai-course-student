import argparse,json
from pathlib import Path
from .core import ROOT,load_config,run,compare,export_kaggle,import_run,pack_run,finalize
p=argparse.ArgumentParser(description='MyLittleMLLab : une hypothèse, une expérience, des preuves.')
s=p.add_subparsers(dest='cmd',required=True)
for name in ['run','export','finalize']:
 a=s.add_parser(name);a.add_argument('--config',required=True,type=Path)
 if name!='run':a.add_argument('--output',required=True,type=Path)
a=s.add_parser('compare');a.add_argument('--folder',type=Path,default=ROOT/'runs')
a=s.add_parser('import');a.add_argument('archive',type=Path)
a=s.add_parser('pack');a.add_argument('folder',type=Path);a.add_argument('--output',required=True,type=Path)
a=p.parse_args()
if a.cmd=='run':print(run(load_config(a.config)))
elif a.cmd=='compare':print(compare(a.folder).to_string(index=False))
elif a.cmd=='export':print(export_kaggle(a.config,a.output))
elif a.cmd=='import':print(import_run(a.archive))
elif a.cmd=='pack':print(pack_run(a.folder,a.output))
elif a.cmd=='finalize':print(finalize(load_config(a.config),a.output))
