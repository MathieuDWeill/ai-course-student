from fastapi.testclient import TestClient
from api import app,train_artifact,drift_report
import numpy as np

def test_contract_and_reload():
    a=train_artifact()
    with TestClient(app) as c:
        assert c.get('/health').json()['model_version']==a['version']
        row={'sepal_length':5.1,'sepal_width':3.5,'petal_length':1.4,'petal_width':.2}
        r=c.post('/predict',json=row)
        assert r.status_code==200
        assert abs(sum(r.json()['probabilities'])-1)<1e-7
        assert len(r.json()['class_order'])==3
        for invalid in [{},{**row,'petal_width':-1},{**row,'extra':1}]:
            assert c.post('/predict',json=invalid).status_code==422
    with TestClient(app) as c:
        r2=c.post('/predict',json=row).json()
    assert r.json()['probabilities']==r2['probabilities']

def test_drift_is_input_alert():
    x=np.array([[0.,0.],[1.,1.],[2.,2.]])
    assert not drift_report(x,x)['alert']
    assert drift_report(x,x+3)['alert']
