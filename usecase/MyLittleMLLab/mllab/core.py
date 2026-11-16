from pathlib import Path
from datetime import datetime, timezone
import hashlib, importlib.metadata, json, platform, shutil, sys, time, uuid, zipfile
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import log_loss, accuracy_score

ROOT = Path(__file__).resolve().parents[1]
FEATURES = [f'p{i}' for i in range(64)]
CLASSES = np.arange(10)

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write_json(path, data): Path(path).write_text(json.dumps(data, indent=2, allow_nan=False),encoding='utf-8')
def read_data(name, root=ROOT):
    if name not in ('train','valid','test'): raise ValueError('Split inconnu')
    f = pd.read_csv(Path(root)/'data'/f'{name}.csv')
    needed = {'sample_id',*FEATURES} | ({'target'} if name != 'test' else set())
    if set(f) != needed or f.sample_id.duplicated().any() or f.isna().any().any(): raise ValueError('Schéma ou observations invalides')
    if not np.isfinite(f[FEATURES].to_numpy()).all(): raise ValueError('Pixels non finis')
    return f

def load_config(path):
    cfg=json.loads(Path(path).read_text())
    if set(cfg) != {'name','hypothesis','model','seed','params'}:raise ValueError('Configuration attendue : name, hypothesis, model, seed, params')
    if not cfg['hypothesis'].strip() or not isinstance(cfg['seed'],int): raise ValueError('Hypothèse et seed requises')
    return cfg

def estimator(cfg):
    name=cfg['model'];p=dict(cfg['params']);seed=cfg['seed']
    if name=='dummy':return DummyClassifier(strategy='prior',**p)
    if name=='logistic':return make_pipeline(StandardScaler(),LogisticRegression(max_iter=600,random_state=seed,**p))
    if name=='forest':return RandomForestClassifier(random_state=seed,n_jobs=1,**p)
    if name=='boosting':return HistGradientBoostingClassifier(random_state=seed,**p)
    raise ValueError('Modèle inconnu')

def probabilities(model,X):
    p=model.predict_proba(X)
    if not np.array_equal(model.classes_,CLASSES): raise ValueError('Classes non alignées')
    if p.shape!=(len(X),10) or not np.isfinite(p).all():raise ValueError('Prédictions invalides')
    return p

def evaluate(y,p):
    if np.asarray(p).ndim!=2 or p.shape!=(len(y),10) or not np.isfinite(p).all() or (p<0).any() or not np.allclose(p.sum(axis=1),1,atol=1e-5): raise ValueError('Probabilités invalides')
    return {'log_loss':float(log_loss(y,p,labels=CLASSES)), 'accuracy':float(accuracy_score(y,np.argmax(p,axis=1)))}

def source_hash():
    h=hashlib.sha256()
    for p in sorted((ROOT/'mllab').glob('*.py')):h.update(p.name.encode());h.update(p.read_bytes())
    return h.hexdigest()

def versions():
    return {k:importlib.metadata.version(k) for k in ['numpy','pandas','scikit-learn']}

def run(cfg, root=ROOT, output=None):
    root=Path(root);train=read_data('train',root);valid=read_data('valid',root)
    if set(train.sample_id)&set(valid.sample_id):raise ValueError('IDs partagés entre train et validation')
    run_id=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'_'+uuid.uuid4().hex[:8]
    out=Path(output or root/'runs')/run_id;out.mkdir(parents=True,exist_ok=False)
    start=time.perf_counter();model=estimator(cfg);model.fit(train[FEATURES],train.target)
    proba=probabilities(model,valid[FEATURES]);seconds=time.perf_counter()-start
    scores=evaluate(valid.target,proba)
    pred=pd.DataFrame(proba,columns=[f'prob_{i}' for i in CLASSES]);pred.insert(0,'sample_id',valid.sample_id.to_numpy());pred.to_csv(out/'predictions.csv',index=False)
    # Le modèle se reconstruit depuis la configuration ; aucun pickle à charger depuis un tiers.
    write_json(out/'config.json',cfg);write_json(out/'metrics.json',{**scores,'seconds':seconds})
    manifest={'schema':1,'run_id':run_id,'created_utc':datetime.now(timezone.utc).isoformat(),'dataset_sha256':{x:digest(root/'data'/f'{x}.csv') for x in ['train','valid']},'source_sha256':source_hash(),'python':platform.python_version(),'platform':platform.platform(),'packages':versions(),'files':{f:digest(out/f) for f in ['config.json','metrics.json','predictions.csv']}}
    write_json(out/'manifest.json',manifest)
    return out,{**scores,'seconds':seconds}

def compare(folder=ROOT/'runs'):
    rows=[]
    for f in sorted(Path(folder).glob('*/manifest.json')):
        m=json.loads(f.read_text())
        # Cette comparaison concerne uniquement le benchmark digits (schéma 1).
        # Les essais Kaggle conservés dans runs/ utilisent un autre contrat.
        if m.get('schema') != 1:
            continue
        cfg=json.loads((f.parent/'config.json').read_text());scores=json.loads((f.parent/'metrics.json').read_text())
        rows.append({'run_id':m['run_id'],'name':cfg['name'],'model':cfg['model'],'hypothesis':cfg['hypothesis'],'data_hash':m['dataset_sha256']['valid'],'source_hash':m['source_sha256'],**scores})
    return pd.DataFrame(rows).sort_values('log_loss') if rows else pd.DataFrame()

RUN_FILES={'manifest.json','config.json','metrics.json','predictions.csv'}
def pack_run(folder, destination):
    folder=Path(folder)
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
        for name in sorted(RUN_FILES):z.write(folder/name,name)
    return Path(destination)

def import_run(archive, root=ROOT):
    root=Path(root)
    with zipfile.ZipFile(archive) as z:
        if set(z.namelist())!=RUN_FILES or len(z.namelist())!=len(RUN_FILES):raise ValueError('Archive de résultats hors contrat')
        if any(x.file_size>5_000_000 for x in z.infolist()):raise ValueError('Archive trop grande')
        blobs={x:z.read(x) for x in RUN_FILES}
    manifest=json.loads(blobs['manifest.json'])
    for name in ['config.json','metrics.json','predictions.csv']:
        if hashlib.sha256(blobs[name]).hexdigest()!=manifest['files'][name]:raise ValueError('Résultat modifié')
    for split in ['train','valid']:
        if digest(root/'data'/f'{split}.csv')!=manifest['dataset_sha256'][split]:raise ValueError('Données/splits incompatibles')
    import io
    pred=pd.read_csv(io.BytesIO(blobs['predictions.csv']));valid=read_data('valid',root)
    if list(pred)!=['sample_id']+[f'prob_{i}' for i in CLASSES] or not np.array_equal(pred.sample_id,valid.sample_id):raise ValueError('IDs de prédiction incompatibles')
    scores=evaluate(valid.target,pred.drop(columns='sample_id').to_numpy());reported=json.loads(blobs['metrics.json'])
    if any(not np.isclose(scores[k],reported[k],atol=1e-9) for k in scores):raise ValueError('Métrique non reproductible')
    # Les empreintes détectent une modification accidentelle, pas une fraude signée.
    dest=root/'runs'/('import_'+uuid.uuid4().hex[:12]);dest.mkdir(parents=True)
    for name,raw in blobs.items():(dest/name).write_bytes(raw)
    return dest

def export_kaggle(cfg_path, destination, root=ROOT):
    """Paquet autoportant sans secrets, corrigés ni labels du test."""
    root=Path(root);cfg=load_config(cfg_path)
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted((root/'mllab').glob('*.py')):z.write(p,'mllab/'+p.name)
        for x in ['train','valid','test']:z.write(root/'data'/f'{x}.csv','data/'+x+'.csv')
        z.writestr('config.json',json.dumps(cfg,indent=2));z.write(root/'requirements.txt','requirements.txt')
        z.writestr('run.py',"from mllab.core import load_config, run, pack_run\np,s=run(load_config('config.json'));print(s);pack_run(p,'result.zip')\n")
    return Path(destination)

def finalize(cfg, destination, root=ROOT):
    """Choix fixés : réentraîner train+validation, produire une seule soumission finale."""
    root=Path(root);dest=Path(destination);dest.mkdir(parents=True,exist_ok=False)
    development=pd.concat([read_data('train',root),read_data('valid',root)],ignore_index=True);test=read_data('test',root)
    assert not set(development.sample_id)&set(test.sample_id)
    model=estimator(cfg).fit(development[FEATURES],development.target)
    p=probabilities(model,test[FEATURES]);f=pd.DataFrame(p,columns=[f'prob_{i}' for i in CLASSES]);f.insert(0,'sample_id',test.sample_id);f.to_csv(dest/'submission.csv',index=False)
    write_json(dest/'config.json',cfg);write_json(dest/'release.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':source_hash(),'data_sha256':{s:digest(root/'data'/f'{s}.csv') for s in ['train','valid','test']},'submission_sha256':digest(dest/'submission.csv'),'packages':versions()})
    return dest
