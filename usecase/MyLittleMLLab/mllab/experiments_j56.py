"""Ateliers J5/J6 : expériences CPU bornées et prédictions hors fold.
Aucun accès réseau, aucune soumission et aucun choix sur le contrôle local.
"""
from pathlib import Path
import hashlib, importlib.metadata as md, json, platform, time
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from .competition import make_model, subsets, xy

CANDIDATES={
 'reference_C01':{'model':'linear','params':{'C':.1}},
 'regul_plus_C001':{'model':'linear','params':{'C':.01}},
 'regul_moins_C1':{'model':'linear','params':{'C':1.}},
 'boost_80':{'model':'boosting','params':{'early_stopping':False}},
}
def sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def versions():
 return {p:md.version(p) for p in ['numpy','pandas','scikit-learn','joblib']}
def ids_digest(ids):return hashlib.sha256(pd.Series(ids).to_csv(index=False).encode()).hexdigest()
def context(root,limit=15000):
 root=Path(root)
 if not isinstance(limit,int) or not 600<=limit<=15000:raise ValueError('LIMIT doit être un entier entre 600 et 15000 pour le budget de classe.')
 tr,control,test,sample,record=subsets('fraud',root=root,limit=limit)
 X,y=xy(tr,'fraud'),tr.is_fraud.astype(int)
 folds=list(StratifiedKFold(3,shuffle=True,random_state=2026).split(X,y))
 counts=np.zeros(len(X),int)
 for train,valid in folds:
  assert not set(tr.iloc[train].id)&set(tr.iloc[valid].id)
  assert y.iloc[valid].nunique()==2
  counts[valid]+=1
 assert (counts==1).all()
 return {'root':root,'train':tr,'control':control,'test':test,'sample':sample,'record':record,'X':X,'y':y,'folds':folds,'limit':limit,'train_ids_sha256':ids_digest(tr.id)}
def make(ctx,name):
 conf=CANDIDATES[name]
 return make_model('fraud',ctx['train'],conf['model'],seed=2026,params=conf['params'])
def fit_budget(configurations,folds,seeds=1):
 if min(configurations,folds,seeds)<1:raise ValueError('Budget strictement positif attendu')
 return configurations*folds*seeds

def tournament(ctx,folder):
 folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
 pred=pd.DataFrame({'id':ctx['train'].id.to_numpy(),'target':ctx['y'].to_numpy(),'fold':-1});rows=[];models={};fit_count=0
 for fold,(_,valid) in enumerate(ctx['folds'],1):pred.loc[valid,'fold']=fold
 for name in CANDIDATES:
  p=np.full(len(pred),np.nan);fits=[]
  for fold,(train,valid) in enumerate(ctx['folds'],1):
   est=clone(make(ctx,name));start=time.perf_counter()
   est.fit(ctx['X'].iloc[train],ctx['y'].iloc[train]);elapsed=time.perf_counter()-start
   p[valid]=est.predict_proba(ctx['X'].iloc[valid])[:,list(est.classes_).index(1)]
   rows.append({'candidat':name,'fold':fold,'auc':float(roc_auc_score(ctx['y'].iloc[valid],p[valid])),'fit_seconds':elapsed});fits.append(est);fit_count+=1
  assert np.isfinite(p).all() and ((p>=0)&(p<=1)).all()
  pred[name]=p;models[name]=fits
 assert fit_count==12
 scores=pd.DataFrame(rows)
 pred.to_csv(folder/'oof.csv',index=False);scores.to_csv(folder/'scores_folds.csv',index=False)
 protocol={'train_ids_sha256':ctx['train_ids_sha256'],'data_sha256':ctx['record']['data_sha256'],'seed':2026,'limit':ctx['limit'],'folds':3,'metric':'roc_auc','cv_fits':fit_count,'candidates':CANDIDATES,'versions':versions(),'machine':platform.platform(),'control':'déjà consulté ; non utilisé pour choisir ici'}
 (folder/'protocole.json').write_text(json.dumps(protocol,ensure_ascii=False,indent=2))
 return pred,scores,models

def add_blend(pred,scores):
 pred=pred.copy();pred['moyenne_50_50']=(pred.reference_C01+pred.boost_80)/2
 extra=[]
 for fold in sorted(pred.fold.unique()):
  part=pred[pred.fold==fold];extra.append({'candidat':'moyenne_50_50','fold':int(fold),'auc':float(roc_auc_score(part.target,part.moyenne_50_50)),'fit_seconds':0.})
 return pred,pd.concat([scores,pd.DataFrame(extra)],ignore_index=True)

def summary(scores):
 return scores.groupby('candidat').agg(auc_moyenne=('auc','mean'),dispersion_folds=('auc','std'),temps_fits_total_s=('fit_seconds','sum')).sort_values('auc_moyenne',ascending=False)

def freeze(ctx,pred,scores,folder):
 folder=Path(folder);table=summary(scores)
 # Règle fixée : meilleure moyenne des 3 folds, nom lexical pour départager une égalité exacte.
 selected=table.reset_index().sort_values(['auc_moyenne','candidat'],ascending=[False,True]).iloc[0].candidat
 members=['reference_C01','boost_80'] if selected=='moyenne_50_50' else [selected]
 weights=[.5,.5] if len(members)==2 else [1.]
 decision={'schema':1,'selected':selected,'members':members,'weights':weights,'selection_rule':'meilleure AUC moyenne CV ; égalité exacte départagée par nom','metric':'roc_auc','limit':ctx['limit'],'seed':2026,'train_ids_sha256':ctx['train_ids_sha256'],'data_sha256':ctx['record']['data_sha256'],'candidates':CANDIDATES,'cv_fits':12,'smoke_fits':2,'selection_fits_total':14,'refit_fits_j6':len(members),'score_public':None,'limits':['CV utilisée pour sélectionner : estimation optimiste possible','Contrôle local déjà consulté dans les journées précédentes','Ensemble exploratoire à poids fixes ; aucune preuve de gain universel']}
 pred.to_csv(folder/'oof.csv',index=False);scores.to_csv(folder/'scores_folds.csv',index=False);table.to_csv(folder/'comparaison.csv');(folder/'decision.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2))
 return decision
