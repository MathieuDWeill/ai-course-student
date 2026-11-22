"""API pédagogique locale : contrat, artefact, versions et journal minimal."""
from pathlib import Path
import json,time
from contextlib import asynccontextmanager
import joblib,numpy as np
from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict,Field

ROOT=Path(__file__).resolve().parent

def train_artifact():
    from sklearn.datasets import load_iris
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    import sklearn
    X,y=load_iris(return_X_y=True)
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
    model=make_pipeline(StandardScaler(),LogisticRegression(C=1,max_iter=300)).fit(Xtr,ytr)
    artifact={'model':model,'version':'iris-v1','features':['sepal_length','sepal_width','petal_length','petal_width'],
              'classes':load_iris().target_names.tolist(),'reference_mean':Xtr.mean(axis=0).tolist(),
              'sklearn_version':sklearn.__version__,'heldout_accuracy':float(model.score(Xte,yte))}
    (ROOT/'runs').mkdir(exist_ok=True)
    joblib.dump(artifact,ROOT/'runs/model.joblib')
    return artifact

@asynccontextmanager
async def lifespan(app):
    path=ROOT/'runs/model.joblib'
    if not path.exists(): raise RuntimeError('Artefact absent : exécuter python api.py avant de démarrer le service.')
    # Charger uniquement son propre artefact de confiance, dans le même environnement.
    app.state.artifact=joblib.load(path)
    yield
app=FastAPI(title='Laboratoire Iris',lifespan=lifespan)
class Observation(BaseModel):
    model_config=ConfigDict(extra='forbid')
    sepal_length:float=Field(gt=0,le=20,allow_inf_nan=False)
    sepal_width:float=Field(gt=0,le=20,allow_inf_nan=False)
    petal_length:float=Field(gt=0,le=20,allow_inf_nan=False)
    petal_width:float=Field(gt=0,le=20,allow_inf_nan=False)
@app.get('/health')
def health(): return {'status':'ok','model_version':app.state.artifact['version']}
@app.post('/predict')
def predict(row:Observation):
    start=time.perf_counter(); a=app.state.artifact
    x=np.array([[getattr(row,f) for f in a['features']]])
    p=a['model'].predict_proba(x)[0]; idx=int(np.argmax(p))
    ms=(time.perf_counter()-start)*1000
    # Aucun identifiant utilisateur ni entrée brute dans ce journal de démonstration.
    record={'model_version':a['version'],'latency_ms':round(ms,3),'predicted_class':a['classes'][idx]}
    with (ROOT/'runs/requests.jsonl').open('a') as f:f.write(json.dumps(record)+'\n')
    return {**record,'probabilities':p.tolist(),'class_order':a['classes']}

def drift_report(reference,current,threshold=.5):
    reference=np.asarray(reference,float);current=np.asarray(current,float)
    scale=reference.std(axis=0)
    shift=np.abs(current.mean(axis=0)-reference.mean(axis=0))/np.maximum(scale,1e-8)
    return {'standardized_mean_shift':shift.tolist(),'alert':bool(np.any(shift>threshold)),
            'meaning':'Alerte heuristique sur les entrées ; ne mesure pas une baisse de performance.'}
if __name__=='__main__':
    a=train_artifact();print(json.dumps({k:v for k,v in a.items() if k!='model'},indent=2))
