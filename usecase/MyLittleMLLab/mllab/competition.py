"""Adaptateurs Kaggle réels. Aucun téléchargement ni aucune soumission implicite."""
from pathlib import Path
import copy,hashlib,json,re,time,uuid,zipfile
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler,OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier,RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_auc_score,f1_score,accuracy_score,log_loss,average_precision_score
from sklearn.model_selection import train_test_split,GroupShuffleSplit
from .core import ROOT,write_json,digest,source_hash,versions

SPECS={
 'fraud':{'slug':'playground-series-s6e11','id':'id','target':'is_fraud','metric':'roc_auc','direction':'maximize','url':'https://www.kaggle.com/competitions/playground-series-s6e11/overview','deadline_utc':'2026-11-30T23:59:00Z','status_checked':'2026-11-06','task':'tabular'},
 'tweets':{'slug':'nlp-getting-started','id':'id','target':'target','metric':'f1','direction':'maximize','url':'https://www.kaggle.com/competitions/nlp-getting-started','deadline_utc':None,'status_checked':'2026-11-06','task':'text'},
 'catsdogs':{'slug':'dogs-vs-cats-redux-kernels-edition','id':'id','target':'label','metric':'log_loss','direction':'minimize','url':'https://www.kaggle.com/competitions/dogs-vs-cats-redux-kernels-edition','deadline_utc':'2017-03-02','status_checked':'2026-11-06','task':'image'}
}

def get_folder(key,root=ROOT):
    if key not in SPECS:raise ValueError('Compétition inconnue')
    return Path(root)/'data/competitions'/SPECS[key]['slug']

def normalize_text(series):return series.fillna('').astype(str).str.lower().str.replace(r'\s+',' ',regex=True).str.strip()

def read_competition(key,root=ROOT):
    spec=SPECS[key];folder=get_folder(key,root)
    if spec['task']=='image':raise ValueError('Utiliser le module vision_competition pour les images')
    required=['train.csv','test.csv','sample_submission.csv']
    if not all((folder/x).exists() for x in required):
        raise FileNotFoundError(f'Données officielles manquantes dans {folder}. Télécharger après lecture/acceptation personnelle des règles ; ne pas remplacer par le jeu digits.')
    a=pd.read_csv(folder/'train.csv');b=pd.read_csv(folder/'test.csv');sample=pd.read_csv(folder/'sample_submission.csv')
    identifier,target=spec['id'],spec['target']
    if identifier not in a or identifier not in b or target not in a or target in b:raise ValueError('Schéma train/test invalide')
    if a[identifier].duplicated().any() or b[identifier].duplicated().any() or a[target].isna().any() or set(a[target].unique())!={0,1}:raise ValueError('IDs/cible invalides')
    if set(a[identifier])&set(b[identifier]):raise ValueError('IDs train/test partagés')
    if list(sample)!=[identifier,target] or not np.array_equal(sample[identifier],b[identifier]):raise ValueError('Sample submission non alignée au test')
    if set(a)-{target}!=set(b):raise ValueError('Variables train/test incohérentes')
    if key=='tweets' and 'text' not in a:raise ValueError('Colonne text absente')
    return a,b,sample

def protocol(key,root=ROOT,seed=2026):
    a,b,s=read_competition(key,root);spec=SPECS[key];folder=get_folder(key,root)
    path=Path(root)/'runs/protocols'/f'{key}_{seed}.json'
    fingerprints={x:digest(folder/x) for x in ['train.csv','test.csv','sample_submission.csv']}
    if path.exists():
        rec=json.loads(path.read_text())
        if rec['data_sha256']!=fingerprints:raise ValueError('Les données ont changé : ne pas réutiliser les anciens splits')
    else:
        ids=np.arange(len(a))
        if key=='tweets':
            # Séparer les textes identiques normalisés ; ne prétend pas identifier auteurs ou événements.
            groups=pd.factorize(normalize_text(a.text))[0]
            i,j=next(GroupShuffleSplit(n_splits=1,test_size=.2,random_state=seed).split(ids,a[spec['target']],groups))
            if len(np.unique(a.iloc[j][spec['target']]))!=2:raise ValueError('Validation sans deux classes')
        else:i,j=train_test_split(ids,test_size=.2,stratify=a[spec['target']],random_state=seed)
        rec={'schema':1,'key':key,'seed':seed,'train_indices':i.tolist(),'valid_indices':j.tolist(),'data_sha256':fingerprints,'warning':'Split de développement ; à revoir si des groupes, une chronologie ou une dérive sont présents.'}
        path.parent.mkdir(parents=True,exist_ok=True);write_json(path,rec)
    return a,b,s,rec

def subsets(key,root=ROOT,seed=2026,limit=10000):
    a,b,s,rec=protocol(key,root,seed);target=SPECS[key]['target'];i=np.array(rec['train_indices']);j=np.array(rec['valid_indices'])
    if limit and len(i)>limit:i=train_test_split(i,train_size=limit,stratify=a.iloc[i][target],random_state=seed)[0]
    if limit and len(j)>max(200,int(limit*.25)):j=train_test_split(j,train_size=max(200,int(limit*.25)),stratify=a.iloc[j][target],random_state=seed)[0]
    return a.iloc[i].copy(),a.iloc[j].copy(),b,s,rec

def make_model(key,train,model='linear',seed=2026,params=None):
    params=dict(params or {});spec=SPECS[key]
    if model=='dummy':return DummyClassifier(strategy='prior')
    if key=='tweets':
        if model!='linear':raise ValueError('Texte classique : linear ou dummy ; transformer dans text_competition')
        return make_pipeline(TfidfVectorizer(ngram_range=(1,2),min_df=1,max_features=30000),LogisticRegression(max_iter=400,random_state=seed,**params))
    features=train.drop(columns=[spec['id'],spec['target']]);num=features.select_dtypes(include='number').columns.tolist();cat=[x for x in features if x not in num]
    if model=='catboost':
        from catboost import CatBoostClassifier
        from sklearn.preprocessing import FunctionTransformer
        def normalize_frame(frame):
            frame=frame.copy()
            for col in cat:frame[col]=frame[col].fillna('__MISSING__').astype(str)
            return frame
        return make_pipeline(FunctionTransformer(normalize_frame),CatBoostClassifier(cat_features=cat,loss_function='Logloss',eval_metric='AUC',random_seed=seed,verbose=False,thread_count=2,**{'iterations':100,'depth':6,'learning_rate':.06,**params}))

    numeric=make_pipeline(SimpleImputer(strategy='median',keep_empty_features=True),StandardScaler())
    if model=='linear':
        categorical=make_pipeline(SimpleImputer(strategy='most_frequent',keep_empty_features=True),OneHotEncoder(handle_unknown='ignore',min_frequency=10,max_categories=64))
        prep=ColumnTransformer([('num',numeric,num),('cat',categorical,cat)])
        return make_pipeline(prep,LogisticRegression(max_iter=400,random_state=seed,**params))
    categorical=make_pipeline(SimpleImputer(strategy='most_frequent',keep_empty_features=True),OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1))
    prep=ColumnTransformer([('num',numeric,num),('cat',categorical,cat)])
    if model=='boosting':est=HistGradientBoostingClassifier(random_state=seed,**{'max_iter':80,'max_leaf_nodes':15,**params})
    elif model=='forest':est=RandomForestClassifier(random_state=seed,n_jobs=1,**{'n_estimators':80,'max_depth':12,**params})
    else:raise ValueError('Modèle inconnu')
    # Ici les codes ordinaux sont traités comme numériques : biais d’ordre à discuter ; pas un encodage catégoriel natif.
    return make_pipeline(prep,est)

def xy(frame,key):
    spec=SPECS[key]
    return frame.text.fillna('') if key=='tweets' else frame.drop(columns=[spec['id'],spec['target']],errors='ignore')

def binary_scores(y,p,threshold=.5):
    p=np.asarray(p,dtype=float);y=np.asarray(y)
    if p.shape!=y.shape or not np.isfinite(p).all() or (p<0).any() or (p>1).any() or set(y)!={0,1}:raise ValueError('Probabilités binaires/cibles invalides')
    return {'roc_auc':float(roc_auc_score(y,p)),'f1':float(f1_score(y,p>=threshold,zero_division=0)),'log_loss':float(log_loss(y,np.column_stack([1-p,p]),labels=[0,1])),'average_precision':float(average_precision_score(y,p)),'accuracy':float(accuracy_score(y,p>=threshold))}

def save_result(key,train,valid,rec,proba,config,seconds,root=ROOT,resources=None):
    spec=SPECS[key];identifier,target=spec['id'],spec['target'];run_id=key+'_'+uuid.uuid4().hex[:12];folder=Path(root)/'runs'/run_id;folder.mkdir(parents=True)
    pred=pd.DataFrame({'id':valid[identifier].to_numpy(),'target':valid[target].to_numpy(),'probability':proba});pred.to_csv(folder/'predictions.csv',index=False)
    scores=binary_scores(valid[target].to_numpy(),proba,config.get('threshold',.5))
    write_json(folder/'metrics.json',{**scores,'seconds':seconds,'resources':resources})
    write_json(folder/'config.json',config)
    write_json(folder/'manifest.json',{'schema':2,'key':key,'competition':spec,'run_id':run_id,'data_sha256':rec['data_sha256'],'source_sha256':source_hash(),'n_train':len(train),'n_valid':len(valid),'train_ids_sha256':hashlib.sha256(train[identifier].to_csv(index=False).encode()).hexdigest(),'valid_ids_sha256':hashlib.sha256(valid[identifier].to_csv(index=False).encode()).hexdigest(),'packages':versions(),'files':{name:digest(folder/name) for name in ['predictions.csv','config.json','metrics.json']}})
    return folder,scores

def run_competition(key,model='linear',params=None,seed=2026,limit=10000,threshold=.5,root=ROOT,hypothesis='Baseline de compétition, à justifier.'):
    from .resources import ResourceMonitor
    a,v,b,s,rec=subsets(key,root,seed,limit);target=SPECS[key]['target']
    with ResourceMonitor() as monitor:
        m=make_model(key,a,model,seed,params).fit(xy(a,key),a[target])
        assert np.array_equal(m.classes_,[0,1])
        p=m.predict_proba(xy(v,key))[:,1]
    seconds=monitor.elapsed
    cfg={'key':key,'model':model,'params':params or {},'seed':seed,'limit':limit,'threshold':threshold,'hypothesis':hypothesis}
    out,scores=save_result(key,a,v,rec,p,cfg,seconds,root,resources=monitor.result())
    return out,scores,m

def make_submission(key,model='linear',params=None,seed=2026,root=ROOT,limit=20000,threshold=.5):
    a,b,s,rec=protocol(key,root,seed);target=SPECS[key]['target']
    if limit and len(a)>limit:a=a.iloc[train_test_split(np.arange(len(a)),train_size=limit,stratify=a[target],random_state=seed)[0]]
    m=make_model(key,a,model,seed,params).fit(xy(a,key),a[target]);p=m.predict_proba(xy(b,key))[:,1]
    result=s.copy();result[target]=(p>=threshold).astype(int) if key=='tweets' else p
    out=Path(root)/'runs'/('submission_'+key+'_'+uuid.uuid4().hex[:8]);out.mkdir(parents=True)
    result.to_csv(out/'submission.csv',index=False)
    write_json(out/'release.json',{'competition':SPECS[key],'data_sha256':rec['data_sha256'],'source_sha256':source_hash(),'model':model,'params':params or {},'threshold':threshold,'train_limit':limit,'submission_sha256':digest(out/'submission.csv'),'note':'Fichier local ; aucune soumission ni acceptation des règles effectuée automatiquement.'})
    return out

def import_competition_result(archive,root=ROOT):
    required={'manifest.json','config.json','metrics.json','predictions.csv'}
    with zipfile.ZipFile(archive) as z:
        if set(z.namelist())!=required or len(z.namelist())!=4 or any(i.file_size>20_000_000 for i in z.infolist()):raise ValueError('Archive hors contrat')
        blobs={n:z.read(n) for n in required}
    manifest=json.loads(blobs['manifest.json'])
    if manifest.get('schema')==3:
        from .vision_competition import import_image_result
        return import_image_result(archive,root)
    key=manifest['key'];cfg=json.loads(blobs['config.json'])
    if manifest['schema']!=2:raise ValueError('Version incompatible')
    for n in ['config.json','metrics.json','predictions.csv']:
        if hashlib.sha256(blobs[n]).hexdigest()!=manifest['files'][n]:raise ValueError('Fichier modifié')
    a,v,b,s,rec=subsets(key,root,cfg['seed'],cfg['limit'])
    if manifest['data_sha256']!=rec['data_sha256']:raise ValueError('Données incompatibles')
    import io
    pred=pd.read_csv(io.BytesIO(blobs['predictions.csv']))
    if list(pred)!=['id','target','probability'] or not np.array_equal(pred.id,v[SPECS[key]['id']]) or not np.array_equal(pred.target,v[SPECS[key]['target']]):raise ValueError('Validation différente')
    scores=binary_scores(pred.target.to_numpy(),pred.probability.to_numpy(),cfg.get('threshold',.5));reported=json.loads(blobs['metrics.json'])
    if any(not np.isclose(scores[k],reported[k],atol=1e-9) for k in scores):raise ValueError('Scores incohérents')
    out=Path(root)/'runs'/('import_'+uuid.uuid4().hex[:12]);out.mkdir(parents=True)
    for n,b in blobs.items():(out/n).write_bytes(b)
    return out

def export_competition(key,destination,root=ROOT,model='linear',limit=10000):
    root=Path(root);read_competition(key,root);spec=SPECS[key]
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
        for p in (root/'mllab').glob('*.py'):z.write(p,'mllab/'+p.name)
        for name in ['train.csv','test.csv','sample_submission.csv']:z.write(get_folder(key,root)/name,f'data/competitions/{spec["slug"]}/{name}')
        z.write(root/'requirements.txt','requirements.txt')
        z.writestr('run.py',f"from mllab.competition import run_competition\nfrom mllab.core import pack_run\np,s,m=run_competition({key!r},model={model!r},limit={limit});print(s);pack_run(p,'result.zip')\n")
    return Path(destination)

def neural_competition(key='fraud',root=ROOT,limit=10000,epochs=8,lr=.001):
    if key!='fraud':raise ValueError('MLP tabulaire pour fraud uniquement')
    from .deep import setup,train_loop
    torch=setup();from torch import nn
    a,v,b,s,rec=subsets(key,root,2026,limit)
    prep=make_model(key,a,'boosting')[0];X=prep.fit_transform(xy(a,key));V=prep.transform(xy(v,key))
    # Codes de catégories ordinaux pédagogiques : préférer embeddings/catégories natives pour approfondir.
    model=nn.Sequential(nn.Linear(X.shape[1],48),nn.ReLU(),nn.Dropout(.2),nn.Linear(48,2))
    model,hist,prob,seconds=train_loop(model,X,a.is_fraud.to_numpy(),V,v.is_fraud.to_numpy(),epochs=epochs,lr=lr)
    config={'key':key,'model':'mlp','params':{'epochs':epochs,'lr':lr},'seed':2026,'limit':limit,'threshold':.5,'hypothesis':'Tester un réseau tabulaire contre les baselines sur le même split.'}
    out,scores=save_result(key,a,v,rec,prob[:,1],config,seconds,root)
    hist.to_csv(out/'learning_curve.csv',index=False)
    return out,scores,hist

def main():
    import argparse
    p=argparse.ArgumentParser(description='Compétitions Kaggle : run, export, import, soumission locale.')
    sub=p.add_subparsers(dest='action',required=True)
    for action in ['run','export','submission']:
        a=sub.add_parser(action);a.add_argument('--key',choices=['fraud','tweets'],required=True);a.add_argument('--model',choices=['dummy','linear','forest','boosting','catboost'],default='linear');a.add_argument('--limit',type=int,default=10000)
        if action=='export':a.add_argument('--output',type=Path,required=True)
        if action=='run':a.add_argument('--hypothesis',required=True)
    a=sub.add_parser('import');a.add_argument('archive',type=Path)
    args=p.parse_args()
    if args.action=='run':out,scores,_=run_competition(args.key,args.model,limit=args.limit,hypothesis=args.hypothesis);print(out);print(scores)
    elif args.action=='export':print(export_competition(args.key,args.output,model=args.model,limit=args.limit))
    elif args.action=='submission':print(make_submission(args.key,args.model,limit=args.limit))
    else:print(import_competition_result(args.archive))
if __name__=='__main__':main()
