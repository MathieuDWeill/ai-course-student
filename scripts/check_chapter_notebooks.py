"""Execute only the 17 small, data-free chapter notebooks, never competition runs."""
from pathlib import Path
import argparse,concurrent.futures,importlib.metadata,json,os,time
import nbformat
from nbclient import NotebookClient
ROOT=Path(__file__).resolve().parents[1]
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
def execute(item):
 f=ROOT/item['notebook'];n=nbformat.read(f,as_version=4);nbformat.validate(n)
 assert n.metadata.get('audience')=='student',f
 assert all(not c.get('outputs') for c in n.cells if c.cell_type=='code'),f
 assert len([c for c in n.cells if c.cell_type=='code'])==2,f
 started=time.monotonic();NotebookClient(n,timeout=120,kernel_name='python3',resources={'metadata':{'path':str(f.parent)}}).execute()
 assert not any(o.output_type=='error' for c in n.cells if c.cell_type=='code' for o in c.outputs),f
 return {'id':item['id'],'status':'PASS','seconds':round(time.monotonic()-started,2)}
def main():
 p=argparse.ArgumentParser();p.add_argument('--report',type=Path);a=p.parse_args();catalog=json.loads((ROOT/'course/catalogue.json').read_text());items=[i for i in catalog['sessions'] if i.get('socle_execute')]
 assert len(items)==17,'Expected the 17 guided chapters; do not silently run the large applications.'
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  results=list(pool.map(execute,items))
 for r in results:print(r['id'],r['status'])
 report={'results':results,'versions':{p:importlib.metadata.version(p) for p in ['numpy','pandas','scikit-learn','nbclient','nbformat']},'scope':'Guided chapter examples only; no external data, GPU or Kaggle execution.'}
 if a.report:a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
