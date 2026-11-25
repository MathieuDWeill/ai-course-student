"""Contrat, rechargement et API locale pédagogique J6.
Charger uniquement un bundle créé et approuvé dans son propre environnement.
"""
from pathlib import Path
import argparse, importlib.metadata as md, json
import joblib
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype,is_bool_dtype
from .experiments_j56 import context, make, sha, versions

def validate_rows(rows,contract):
 if not isinstance(rows,list) or not 1<=len(rows)<=1000:raise ValueError('Entre 1 et 1000 lignes sont requises.')
 columns=contract['columns'];numeric=set(contract['numeric']);boolean=set(contract.get('boolean',[]))
 for i,row in enumerate(rows):
  if not isinstance(row,dict) or set(row)!=set(columns):raise ValueError(f'Ligne {i} : colonnes manquantes ou supplémentaires.')
  for k,v in row.items():
   if v is None:continue # Politique explicite : imputation apprise dans le pipeline.
   if k in boolean:
    if not isinstance(v,bool):raise ValueError(f'Ligne {i} : {k} doit être un booléen ou null.')
   elif k in numeric:
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not np.isfinite(v):raise ValueError(f'Ligne {i} : {k} doit être un nombre fini ou null.')
   elif not isinstance(v,str):raise ValueError(f'Ligne {i} : {k} doit être un texte ou null.')
 frame=pd.DataFrame(rows,columns=columns)
 for k in columns:
  if k in numeric:frame[k]=pd.to_numeric(frame[k],errors='raise').astype(float)
  else:frame[k]=frame[k].where(frame[k].notna(),np.nan)
 return frame

def positive_scores(bundle,frame):
 p=np.zeros(len(frame),float)
 for model,w in zip(bundle['models'],bundle['weights']):p+=w*model.predict_proba(frame)[:,list(model.classes_).index(1)]
 if not np.isfinite(p).all() or ((p<0)|(p>1)).any():raise ValueError('Sortie de probabilité invalide.')
 return p

def build_release(root,decision_path,folder):
 decision=json.loads(Path(decision_path).read_text());ctx=context(root,int(decision['limit']))
 if decision['train_ids_sha256']!=ctx['train_ids_sha256'] or decision['data_sha256']!=ctx['record']['data_sha256']:raise ValueError('Les données ou les identifiants diffèrent de J5. Refaire J5, sans réutiliser cette décision.')
 folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
 models=[make(ctx,k).fit(ctx['X'],ctx['y']) for k in decision['members']]
 assert len(models)==decision['refit_fits_j6']
 contract={'columns':ctx['X'].columns.tolist(),'numeric':[c for c in ctx['X'] if is_numeric_dtype(ctx['X'][c]) and not is_bool_dtype(ctx['X'][c])],'boolean':[c for c in ctx['X'] if is_bool_dtype(ctx['X'][c])],'classes':[0,1],'positive_class':1,'target':'is_fraud','missing_values':'Clés obligatoires ; valeurs null autorisées et imputées par le pipeline appris','unknown_categories':'Chaînes inconnues admises ; traitement du pipeline entraîné conservé','max_rows':1000,'probability':'Score estimé de la classe 1 ; calibration non démontrée'}
 bundle={'models':models,'weights':decision['weights'],'contract':contract,'selected':decision['selected']}
 joblib.dump(bundle,folder/'modele.joblib')
 metadata={'schema':1,'selected':decision['selected'],'members':decision['members'],'weights':decision['weights'],'refit_fits':len(models),'train_rows':len(ctx['X']),'train_ids_sha256':ctx['train_ids_sha256'],'data_sha256':ctx['record']['data_sha256'],'contract':contract,'versions':versions(),'artifact_sha256':sha(folder/'modele.joblib'),'score_public':None,'control_status':'contrôle de développement déjà consulté'}
 (folder/'manifest.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2))
 return ctx,bundle,metadata

def load_release(folder):
 folder=Path(folder);metadata=json.loads((folder/'manifest.json').read_text())
 if sha(folder/'modele.joblib')!=metadata['artifact_sha256']:raise ValueError('Empreinte du fichier modèle incorrecte.')
 if md.version('scikit-learn')!=metadata['versions']['scikit-learn']:raise ValueError('Version scikit-learn différente : reconstruire le bundle dans cet environnement ou utiliser les versions enregistrées.')
 # Empreinte = intégrité par rapport au manifeste, pas une preuve de confiance externe.
 return joblib.load(folder/'modele.joblib'),metadata

def predict_rows(folder,rows):
 bundle,metadata=load_release(folder);frame=validate_rows(rows,bundle['contract'])
 return {'selected':bundle['selected'],'model_sha256':metadata['artifact_sha256'],'positive_class':1,'scores':positive_scores(bundle,frame).tolist()}

def align_submission(sample,predictions):
 if list(sample)!=['id','is_fraud'] or list(predictions)!=['id','is_fraud']:raise ValueError('Colonnes attendues : id, is_fraud.')
 if sample.id.duplicated().any() or predictions.id.duplicated().any():raise ValueError('Identifiants dupliqués.')
 if len(sample)!=len(predictions) or set(sample.id)!=set(predictions.id):raise ValueError('Identifiants manquants ou supplémentaires.')
 out=sample[['id']].merge(predictions,on='id',how='left',validate='one_to_one',sort=False)
 if not np.array_equal(out.id,sample.id) or not np.isfinite(out.is_fraud).all() or not out.is_fraud.between(0,1).all():raise ValueError('Alignement ou probabilités invalides.')
 return out

def create_app(folder):
 from fastapi import FastAPI,HTTPException
 from pydantic import BaseModel,ConfigDict,Field
 from typing import Any
 folder=Path(folder);_,meta=load_release(folder)
 app=FastAPI(title='MyLittleMLLab — Inférence locale',version='1')
 class Batch(BaseModel):
  model_config=ConfigDict(extra='forbid')
  rows:list[dict[str,Any]]=Field(min_length=1,max_length=1000)
 @app.get('/health')
 def health():return {'status':'ready','selected':meta['selected'],'model_sha256':meta['artifact_sha256']}
 @app.post('/predictions')
 def predictions(payload:Batch):
  try:return predict_rows(folder,payload.rows)
  except ValueError as exc:raise HTTPException(status_code=422,detail=str(exc)) from exc
 return app

def monitoring(reference,current,probabilities):
 # Indicateurs descriptifs : ni test causal ni mesure de performance sans labels.
 rows=[]
 for col in reference.select_dtypes(include='number'):
  a=reference[col];b=current[col]
  rows.append({'variable':col,'moyenne_reference':float(a.mean()),'moyenne_courante':float(b.mean()),'taux_manquant_reference':float(a.isna().mean()),'taux_manquant_courant':float(b.isna().mean())})
 return pd.DataFrame(rows),{'lignes':len(current),'score_moyen':float(np.mean(probabilities)),'performance_sans_labels':'non mesurable'}

def main():
 p=argparse.ArgumentParser(description='Prédire avec un bundle local approuvé ; aucune connexion réseau.');p.add_argument('--bundle',required=True);p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 result=predict_rows(a.bundle,json.loads(Path(a.input).read_text())['rows']);Path(a.output).write_text(json.dumps(result,indent=2));print('Prédictions écrites ; aucune soumission.')
if __name__=='__main__':main()
