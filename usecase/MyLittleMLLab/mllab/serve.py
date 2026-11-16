"""Démo d'inférence locale ; pas de déploiement de production."""
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
import numpy as np,pandas as pd
from .core import read_data,load_config,ROOT,FEATURES,estimator

def validate_pixels(pixels):
    x=np.asarray(pixels,dtype=float)
    if x.shape!=(64,) or not np.isfinite(x).all() or (x<0).any() or (x>16).any():raise ValueError('64 pixels finis entre 0 et 16 requis')
    return pd.DataFrame([x],columns=FEATURES)

class Handler(BaseHTTPRequestHandler):
    def answer(self,data,status=200):
        payload=json.dumps(data).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(payload)));self.end_headers();self.wfile.write(payload)
    def do_GET(self):self.answer({'service':'MyLittleMLLab','usage':'POST /predict avec pixels : liste de 64 nombres entre 0 et 16'})
    def do_POST(self):
        if self.path!='/predict':return self.answer({'error':'route inconnue'},404)
        try:
            size=int(self.headers.get('Content-Length',0))
            if not 0<size<10000:raise ValueError('Taille invalide')
            record=json.loads(self.rfile.read(size));X=validate_pixels(record['pixels']);p=self.server.model.predict_proba(X)[0]
            self.answer({'digit':int(p.argmax()),'probabilities':p.tolist()})
        except Exception as e:self.answer({'error':str(e)},400)

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8770);args=parser.parse_args()
    train=read_data('train');model=estimator(load_config(ROOT/'configs/linear.json')).fit(train[FEATURES],train.target)
    server=HTTPServer(('127.0.0.1',args.port),Handler);server.model=model
    print(f'Démo locale : http://127.0.0.1:{args.port}',flush=True);server.serve_forever()
if __name__=='__main__':main()
